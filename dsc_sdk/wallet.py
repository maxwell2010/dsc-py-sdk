import os
import json
from typing import Optional
from eth_account import Account as EthAccount
from eth_keys import keys
from eth_utils import to_checksum_address
from bech32 import bech32_encode, convertbits


class Wallet:
    def __init__(self, mnemonic: str = None, private_key: str = None):
        if mnemonic:
            self.mnemonic = mnemonic
            self.account = self._derive_from_mnemonic(mnemonic)
        elif private_key:
            self.private_key = private_key
            self.account = EthAccount.from_key(private_key)
        else:
            raise ValueError("Either mnemonic or private key must be provided")

    def _derive_from_mnemonic(self, mnemonic):
        # Здесь будет логика генерации аккаунта из мнемоники
        return EthAccount.from_key(keys.PrivateKey.generate().to_hex())

    @classmethod
    def generate_new(cls, password: Optional[str] = None) -> "Wallet":
        priv_key = keys.PrivateKey.generate().to_hex()
        return cls(private_key=priv_key)

    @property
    def address(self) -> str:
        return to_checksum_address(self.account.address)

    def bech32_address(self) -> str:
        data = convertbits(bytes.fromhex(self.address[2:]), 8, 5)
        return bech32_encode('d0', data)

    def sign_transaction(self, tx_data: dict) -> dict:
        signed_tx = self.account.sign_transaction(tx_data)
        return {
            "raw_tx": signed_tx.rawTransaction.hex(),
            "hash": signed_tx.hash.hex(),
        }
