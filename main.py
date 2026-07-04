from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.savings import Savings
from src.models.settlement_rule import SettlementRule
from src.services.savings_service import SavingsService
from src.services.settlement_service import SettlementService
from src.models.settlement_history import SettlementHistory
from src.config.app_config import AppConfig
from src.models.mortgage_context import MortgageContext
from src.models.settlement_rule import SettlementRule

loan = Loan(
    principal=8_000_000,
    annual_rate=0.05,
    term_months=156,
    emi=69_845,
)

context = MortgageContext.create(
    loan=loan,
    currency=AppConfig.DEFAULT_CURRENCY,
    settlement_rule=SettlementRule(),
)



SavingsService.deposit(
    savings=context.savings,
    month=48,
    description="Accumulated Savings",
    amount=650_000,
)

SettlementService.apply(context)