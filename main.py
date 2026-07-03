from src.loan import Loan
from src.emi import calculate_emi

loan = Loan(
    principal=8_000_000,
    annual_rate=0.05,
    term_months=156,
    emi=69_845
)

calculated_emi = calculate_emi(
    principal=loan.principal,
    annual_rate=loan.annual_rate,
    term_months=loan.term_months,
)

from src.amortization import generate_schedule

schedule = generate_schedule(loan)

print()

print("First 12 Payments")

print("-" * 90)

print(
    f"{'M':<4}"
    f"{'Opening':>15}"
    f"{'Interest':>15}"
    f"{'Principal':>15}"
    f"{'Closing':>15}"
)

for payment in schedule[:12]:

    print(
        f"{payment.month:<4}"
        f"{payment.opening_balance:>15,.2f}"
        f"{payment.interest:>15,.2f}"
        f"{payment.principal:>15,.2f}"
        f"{payment.closing_balance:>15,.2f}"
    )