from dataclasses import dataclass

@dataclass
class Payment:

    month: int

    opening_balance: float

    emi: float

    interest: float

    principal: float

    closing_balance: float