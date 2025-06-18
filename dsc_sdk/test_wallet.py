import pytest
from dsc_sdk.wallet import Wallet


def test_wallet_from_mnemonic():
    mnemonic = "gasp history river forget aware wide dance velvet weather rain rail dry cliff"
    wallet = Wallet(mnemonic=mnemonic)
    assert wallet.address.startswith("0x")


def test_wallet_generate_new():
    wallet = Wallet.generate_new()
    assert wallet.address.startswith("0x")
