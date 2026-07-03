from src.loan import Loan


loan = Loan(
    principal=8_000_000,
    annual_rate=0.05,
    term_months=156,
    emi=69_845
)

print("Loan Information")

print("----------------")

print(f"Principal : ${loan.principal:,.0f}")

print(f"Interest  : {loan.annual_rate*100:.2f}%")

print(f"Months    : {loan.term_months}")

print(f"EMI        : ${loan.emi:,.2f}")

print(f"Monthly Rate : {loan.monthly_rate:.8f}")