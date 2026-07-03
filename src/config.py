from dataclasses import dataclass

@dataclass
class LoanConfig:

    principal: float

    annual_rate: float

    term_months: int

    emi: float