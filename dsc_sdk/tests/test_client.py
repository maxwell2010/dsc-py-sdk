import pytest
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient
from dsc_sdk.evm_service import EVMService


def test_get_balance():
    wallet = Wallet.generate_new()
    client = DecimalClient(
        rpc_url="https://rpc.decimalchain.org", 
        chain_id="decimal-1",
        wallet=wallet
    )
    balance = client.get_balance(wallet.address)
    assert isinstance(balance, dict)
