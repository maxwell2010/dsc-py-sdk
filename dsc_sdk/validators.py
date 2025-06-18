from typing import Optional, List, Dict, Any
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient


class ValidatorService:
    def __init__(self, client: DecimalClient):
        self.client = client

    def get_validators(self) -> List[Dict[str, Any]]:
        url = f"{self.client.rpc_url}/decimal/staking/v1/validators"
        response = requests.get(url)
        return response.json()

    def get_validator_info(self, validator_addr: str) -> Dict[str, Any]:
        url = f"{self.client.rpc_url}/decimal/staking/v1/validators/{validator_addr}"
        response = requests.get(url)
        return response.json()

    def delegate_to_validator(
        self,
        validator_addr: str,
        amount: str
    ) -> str:
        # Делегирование средств валидатору
        pass

    def undelegate_from_validator(
        self,
        validator_addr: str,
        amount: str
    ) -> str:
        # Отделегирование средств
        pass
