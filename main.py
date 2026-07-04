from src.config.app_config import AppConfig
from src.core.formatter import format_money
from src.models.loan import Loan

loan = Loan(
    principal=8_000_000,
    annual_rate=0.05,
    term_months=156,
    emi=69_845
)

print(
    format_money(
        loan.principal,
        AppConfig.DEFAULT_CURRENCY,
    )
)