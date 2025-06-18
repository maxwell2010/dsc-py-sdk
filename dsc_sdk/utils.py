import math
from typing import Optional, Any
from decimal import Decimal


def calculate_fee(gas_used: int, gas_price: int) -> int:
    return gas_used * gas_price


def format_amount(amount: str) -> Decimal:
    return Decimal(amount) / Decimal(10**18)


def to_hex(value: int) -> str:
    return hex(value)[2:] if value >= 0 else "0x0"


def is_valid_address(address: str) -> bool:
    return address.startswith("0x") and len(address) == 42
