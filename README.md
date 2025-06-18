# Decimal Python SDK

Python SDK for interacting with the Decimal blockchain and EVM smart contracts.

## 📦 Installation

```bash
pip install dsc-py-sdk
```

Or install from source:
```bash
git clone https://github.com/yourusername/dsc-py-sdk.git 
cd dsc-py-sdk
pip install -e .
```
## 🧪 Example Usage
#### 🔐 Create Wallet from Mnemonic
```bash
from dsc_sdk.wallet import Wallet

wallet = Wallet.from_mnemonic("gasp history river forget aware wide dance velvet weather rain rail dry cliff")
print(f"Address: {wallet.address}")
print(f"Bech32 Address: {wallet.bech32_address()}")
```
#### 💰 Send DEL Tokens
```bash
from dsc_sdk.client import DecimalClient
from dsc_sdk.evm_service import send_del_tokens

client = DecimalClient(
    rpc_url="https://rpc.decimalchain.org", 
    chain_id="decimal-1",
    wallet=wallet
)

tx_hash = send_del_tokens(client, "0x1w98j4vk6dkpyndjnv5dn2eemesq6a2c2j9depy", "1000")
print(f"TX Hash: {tx_hash}")
```

#### 🔄 Subscribe to ERC-20 Transfer Events
```bash
from dsc_sdk.evm_contract import EVMContract
from dsc_sdk.subscriptions import EventSubscription
import asyncio

async def on_transfer_event(event):
    print("New Transfer event:", event)

def main():
    client = DecimalClient(rpc_url="https://rpc.decimalchain.org",  chain_id="decimal-1", wallet=wallet)
    contract = EVMContract.from_abi_file(client, "./erc20.abi.json", address="0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B")

    sub = EventSubscription(client, "Transfer", contract.address, on_transfer_event)
    asyncio.run(sub.start())

if __name__ == "__main__":
    main()
```

#### 🏗️ Deploy and Call Smart Contract
```bash
from dsc_sdk.evm_contract import EVMContract

contract = EVMContract.from_abi_file(client, "MyToken.abi", address=None)
tx_hash = contract.deploy(["MyToken", "MTK", 18, 1000000])
print(f"Contract deployed at hash: {tx_hash}")

result = contract.call("balanceOf", wallet.address)
print(f"Balance: {result}")
```
#### 🧱 Read blocks
```bash
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
```
### 🚀 Features
#### ✅ Create and manage wallets (mnemonic, private key)
#### ✅ Interact with Decimal API
#### ✅ Send and burn DEL tokens
#### ✅ Delegate to validators
#### ✅ Mint and transfer NFTs (ERC721/ERC1155)
#### ✅ Work with ERC-20/ERC-721/ERC-1155 tokens
#### ✅ Support for MultiSig wallets
#### ✅ REST API helpers and error handling
#### ✅ Web3 integration for EVM contract interaction
#### ✅ Event subscriptions (e.g., track new blocks or Transfer events)


### 📜 License
MIT License

### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
