# Decimal Python SDK

Python SDK for interacting with the Decimal blockchain and EVM smart contracts.

## Installation

```bash
pip install dsc-py-sdk


Or install from source:
git clone https://github.com/yourusername/dsc-py-sdk.git 
cd dsc-py-sdk
pip install -e .

### Usage

```bash
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient
from dsc_sdk.evm_service import send_del_tokens, delegate_del

wallet = Wallet.from_mnemonic("gasp history river forget aware wide dance velvet weather rain rail dry cliff")
client = DecimalClient(rpc_url="https://rpc.decimalchain.org",  chain_id="decimal-1", wallet=wallet)

balance = client.get_balance(wallet.address)
print(f"Balance: {balance}")

tx_hash = send_del_tokens(client, "0x1w98j4vk6dkpyndjnv5dn2eemesq6a2c2j9depy", "1000")
print(f"TX Hash: {tx_hash}")

Пример: подписка на событие Transfer ERC-20
```bash
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient
from dsc_sdk.evm_contract import EVMContract
from dsc_sdk.subscriptions import EventSubscription
import asyncio


async def on_transfer_event(event):
    print("New Transfer event:", event)


def main():
    wallet = Wallet.from_mnemonic("gasp history river forget aware wide dance velvet weather rain rail dry cliff")
    client = DecimalClient(rpc_url="https://rpc.decimalchain.org",  chain_id="decimal-1", wallet=wallet)

    erc20_abi = "./erc20.abi.json"
    contract = EVMContract.from_abi_file(client, erc20_abi, address="0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B")

    # Создаем подписку
    sub = EventSubscription(client, "Transfer", contract.address, on_transfer_event)
    asyncio.run(sub.start())

Пример: отслеживание новых блоков
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient
from dsc_sdk.subscriptions import BlockSubscription
import asyncio


async def on_new_block(block):
    print("New block:", block.number)


def main():
    wallet = Wallet.generate_new()
    client = DecimalClient(rpc_url="https://rpc.decimalchain.org",  chain_id="decimal-1", wallet=wallet)
    sub = BlockSubscription(client, on_new_block)
    asyncio.run(sub.start())

## Features
Create and manage wallets (mnemonic, private key)
Interact with Decimal API
Send DEL tokens
Delegate to validators
NFT minting and delegation
ERC-20/ERC-721/ERC-1155 support
REST API helpers and error handling
