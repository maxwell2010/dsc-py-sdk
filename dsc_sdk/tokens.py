from typing import Optional, List, Dict, Any
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient


class TokenService:
    def __init__(self, client: DecimalClient):
        self.client = client

    def get_token_info(self, token_address: str) -> Dict[str, Any]:
        url = f"{self.client.rpc_url}/decimal/tokens/v1/tokens/{token_address}"
        response = requests.get(url)
        return response.json()

    def get_token_balance(self, address: str, token_address: str) -> Dict[str, Any]:
        url = f"{self.client.rpc_url}/decimal/tokens/v1/balances/{address}/{token_address}"
        response = requests.get(url)
        return response.json()

    def transfer_token(
        self,
        from_address: str,
        to_address: str,
        amount: str,
        token_address: str
    ) -> str:
        # Перевод токена
        pass

    def approve_token(
        self,
        owner: str,
        spender: str,
        amount: str,
        token_address: str
    ) -> str:
        # Одобрение токена
        pass
