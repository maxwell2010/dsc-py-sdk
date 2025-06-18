from typing import Optional, Dict, Any, List
from web3 import Web3, HTTPProvider
from web3.exceptions import TransactionNotFound
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient


class EVMContract:
    def __init__(self, client: DecimalClient, abi: Dict[str, Any], address: str = None):
        self.client = client
        self.w3 = Web3(HTTPProvider(client.rpc_url))
        self.abi = abi
        self.address = address
        self.contract = self.w3.eth.contract(address=address, abi=abi)

    @classmethod
    def from_abi_file(cls, client: DecimalClient, abi_path: str, address: str = None) -> "EVMContract":
        with open(abi_path, "r") as f:
            abi = json.load(f)
        return cls(client, abi, address)

    def call(self, function_name: str, *args) -> Any:
        func = self.contract.functions[function_name]
        return func(*args).call()

    def send_transaction(
        self,
        function_name: str,
        *args,
        value: int = 0,
        gas: int = 200000
    ) -> str:
        func = self.contract.functions[function_name]
        tx = func(*args).build_transaction({
            "from": self.client.wallet.address,
            "value": value,
            "gas": gas,
            "nonce": self.w3.eth.get_transaction_count(self.client.wallet.address),
            "chainId": int(self.client.chain_id)
        })
        signed_tx = self.client.wallet.sign_transaction(tx)
        return self.client.send_transaction(signed_tx)

    def deploy(self, constructor_args: list, value: int = 0, gas: int = 2000000) -> str:
        contract = self.w3.eth.contract(abi=self.abi)
        transaction = contract.constructor(*constructor_args).build_transaction({
            "from": self.client.wallet.address,
            "value": value,
            "gas": gas,
            "nonce": self.w3.eth.get_transaction_count(self.client.wallet.address),
            "chainId": int(self.client.chain_id)
        })
        signed_tx = self.client.wallet.sign_transaction(transaction)
        tx_hash = self.client.send_transaction(signed_tx)
        self.address = self.w3.eth.wait_for_transaction_receipt(tx_hash)["contractAddress"]
        return tx_hash

    def wait_for_transaction(self, tx_hash: str, timeout: int = 120) -> Dict[str, Any]:
        try:
            receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
            return {
                "tx_hash": tx_hash,
                "block_number": receipt["blockNumber"],
                "status": "success" if receipt["status"] == 1 else "failed"
            }
        except TransactionNotFound:
            raise Exception("Transaction not found or timed out")

    def event_filter(self, event_name: str, from_block: int = 0, to_block: int = "latest") -> List[Any]:
        event = self.contract.events[event_name]
        filter = event.createFilter(fromBlock=from_block, toBlock=to_block)
        return filter.get_all_entries()
