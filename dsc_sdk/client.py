import requests
from typing import Dict, Any, List
from .wallet import Wallet


class DecimalClient:
    def __init__(
        self,
        rpc_url: str,
        chain_id: str,
        wallet: Wallet,
        logger=None
    ):
        self.rpc_url = rpc_url
        self.chain_id = chain_id
        self.wallet = wallet
        self.logger = logger or print

    def get_balance(self, address: str) -> Dict[str, Any]:
        url = f"{self.rpc_url}/cosmos/bank/v1beta1/balances/{address}"
        response = requests.get(url)
        return response.json()

    def calculate_fee(self, tx_bytes: bytes, denom: str) -> Dict[str, Any]:
        url = f"{self.rpc_url}/decimal/fee/v1/calculate_commission"
        payload = {
            "tx_bytes": tx_bytes.hex(),
            "denom": denom
        }
        response = requests.post(url, json=payload)
        return response.json()

    def send_transaction(self, tx_data: dict) -> str:
        signed_tx = self.wallet.sign_transaction(tx_data)
        url = f"{self.rpc_url}/txs"
        response = requests.post(url, json={"tx": signed_tx})
        return response.json()["hash"]
