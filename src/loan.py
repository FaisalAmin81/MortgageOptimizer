from dataclasses import dataclass


@dataclass
class Loan:

    principal: float

    annual_rate: float

    term_months: int

    emi: float

    @property
    def monthly_rate(self):

        return self.annual_rate / 12