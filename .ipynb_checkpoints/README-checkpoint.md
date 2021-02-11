# Multi-Blockchain Wallet in Python

For this assignment, I have built a wallet using `hd-wallet-derive` that can manage billions of addresses across 300+ coins. This assignment will focus on 2 coins: Ethereum and Bitcoin Testnet.

---

## Dependencies

- PHP must be installed

- Clone the [`hd-wallet-derive`](https://github.com/dan-da/hd-wallet-derive) tool, create a symlink called `derive` for the `hd-wallet-derive/hd-wallet-derive.php` script into the top level project
  directory like so: `ln -s hd-wallet-derive/hd-wallet-derive.php derive`. For Window users, you need to first run `export MSYS=winsymlinks:nativestrict`

- [`bit`](https://ofek.github.io/bit/) Python Bitcoin library

- [`web3.py`](https://github.com/ethereum/web3.py) Python Ethereum library

- Download [MyCrypto](https://www.mycrypto.com/) Desktop App to manage ethereum wallets and make transactions in the blockchain

- Local POA ethereum network, instructions on how to set it up can be found at https://github.com/githb21/blockchain_homework

---

## Instructions

### Generate a Mnemonic

- Generate a new 12 word mnemonic using `hd-wallet-derive` or by using [this tool](https://iancoleman.io/bip39/).

- Set this mnemonic as an environment variable

### Bitcoin Testnet Transaction

- Fund a `BTCTEST` address using [this testnet faucet](https://testnet-faucet.mempool.co/)

- Open up a new terminal window inside of `wallet`, then run `python`. Within the Python shell, run `from wallet import *` 

![btctest](images/btc_function.png)

- Use a [block explorer](https://tbtc.bitaps.com/) to watch transactions on the address.

![btc_account](images/btctest_accout_one.PNG)

![btc_tx](images/btctest_tx.PNG)

### Local PoA Ethereum Transaction

- Add one of the `ETH` addresses to the pre-allocated accounts in your `networkname.json`.

- Open up a new terminal window inside of `wallet`, then run `python`. Within the Python shell, run `from wallet import *` 

![eth](images/eth_function.PNG)

- Copy the `txid` into MyCrypto's TX Status to check the status

![eth_tx](images/eth_tx.PNG)