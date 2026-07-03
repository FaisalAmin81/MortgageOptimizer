from dataclasses import dataclass


@dataclass
class Loan:

    principal: float

    annual_rate: float

    term_months: int

    emi: float

    @property
    def monthly_rate(self) -> float:

        return self.annual_rate / 12

    def monthly_interest(self, balance: float) -> float:

        return balance * self.monthly_rate