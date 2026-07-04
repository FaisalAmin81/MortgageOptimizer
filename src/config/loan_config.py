from dataclasses import dataclass


@dataclass(frozen=True)
class LoanConfig:

    principal: float

    annual_rate: float

    term_months: int

    original_emi: float