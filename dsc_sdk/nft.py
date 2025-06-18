from typing import Optional, List, Dict, Any
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient


class NFTService:
    def __init__(self, client: DecimalClient):
        self.client = client

    def get_nft_info(self, nft_id: int, nft_collection: str) -> Dict[str, Any]:
        url = f"{self.client.rpc_url}/decimal/nft/v1/nfts/{nft_collection}/{nft_id}"
        response = requests.get(url)
        return response.json()

    def get_nft_balance(self, address: str) -> List[Dict[str, Any]]:
        url = f"{self.client.rpc_url}/decimal/nft/v1/balances/{address}"
        response = requests.get(url)
        return response.json()

    def mint_nft(self, token_uri: str, creator: str) -> str:
        # Логика майна NFT
        pass

    def transfer_nft(
        self,
        from_address: str,
        to_address: str,
        token_id: int,
        nft_collection: str
    ) -> str:
        # Перевод NFT
        pass
