from dotenv import load_dotenv
import os
import subprocess
import json
from constants import *
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

load_dotenv()
mnemonic = os.getenv("mnemonic")

def derive_wallets(coin):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=address,index,path,privkey,pubkey --coin="{coin}" --numderive=3 --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

coins = {
    ETH: derive_wallets(ETH),
    BTCTEST: derive_wallets(BTCTEST)
}

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas({"from": account.address, "to": to, "value": amount})
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return print(result.hex())
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed_tx)

#btctest_account_one = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])
#btctest_address_two = coins[BTCTEST][1]['address']   
#send_tx(BTCTEST, btctest_account_one, btctest_address_two, 0.002)

#eth_account_one = priv_key_to_account(ETH, coins[ETH][0]['privkey'])
#eth_address_two = coins[ETH][1]['address']
#send_tx(ETH, eth_account_one, eth_address_two, 100000000000000000)