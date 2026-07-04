from dataclasses import dataclass


@dataclass
class Transaction:

    month: int

    description: str

    deposit: float

    withdrawal: float

    balance: float