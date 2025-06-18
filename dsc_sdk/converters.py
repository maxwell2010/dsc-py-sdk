from typing import Optional, List, Dict, Any
from decimal import Decimal


def convert_balance(balance: str) -> Decimal:
    return Decimal(balance) / Decimal(10**18)


def convert_gas_limit(gas_estimate: int) -> int:
    return int(gas_estimate * 1.1)


def parse_tx_receipt(receipt: dict) -> Dict[str, Any]:
    result = {
        "tx_hash": receipt["transactionHash"].hex(),
        "block_number": receipt["blockNumber"],
        "status": "success" if receipt["status"] == 1 else "failed"
    }
    return result
