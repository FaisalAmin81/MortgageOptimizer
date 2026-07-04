from dataclasses import dataclass

from src.models.currency import Currency
from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.savings import Savings
from src.models.settlement_history import SettlementHistory
from src.models.settlement_rule import SettlementRule


@dataclass
class MortgageContext:
    """
    Holds all information required to simulate a mortgage.
    """

    loan: Loan
    state: LoanState
    savings: Savings
    settlement_history: SettlementHistory
    settlement_rule: SettlementRule
    currency: Currency

    @classmethod
    def create(
        cls,
        loan: Loan,
        currency: Currency,
        settlement_rule: SettlementRule,
    ) -> "MortgageContext":
        return cls(
            loan=loan,
            state=LoanState.from_loan(loan),
            savings=Savings(),
            settlement_history=SettlementHistory(),
            settlement_rule=settlement_rule,
            currency=currency,
        )