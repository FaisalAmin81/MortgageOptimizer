from dataclasses import dataclass


@dataclass
class MonthlySnapshot:
    """
    Complete financial picture for one simulation month.
    """

    month: int

    # Loan
    opening_balance: float
    emi: float
    interest: float
    principal: float
    closing_balance: float

    # Contributions
    ceiling_contribution: float
    salary_contribution: float
    total_contribution: float

    # Savings
    surplus: float
    savings_balance: float

    # Settlement
    settlement_amount: float = 0.0
    settlement_executed: bool = False

    # Running totals
    cumulative_interest: float = 0.0
    cumulative_principal: float = 0.0
