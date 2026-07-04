from dataclasses import dataclass


@dataclass
class Payment:
    month: int

    opening_balance: float

    emi: float

    interest: float

    principal: float

    closing_balance: float

    @property
    def total_payment(self) -> float:
        return self.interest + self.principal
    @property
    def remaining_balance(self) -> float:
        return self.closing_balance 