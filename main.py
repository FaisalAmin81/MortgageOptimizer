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

print("Mortgage Optimizer")
print("-" * 50)

print(f"Principal      : ₦{loan.principal:,.2f}")
print(f"Annual Rate    : {loan.annual_rate:.2%}")
print(f"Loan Term      : {loan.term_months} months")
print(f"Bank EMI       : ₦{loan.emi:,.2f}")
print(f"Calculated EMI : ₦{calculated_emi:,.2f}")

difference = calculated_emi - loan.emi

print(f"Difference     : ₦{difference:,.2f}")
print("\nDebug Information")
print("-" * 50)

print(f"Monthly Rate : {loan.monthly_rate:.10f}")

print(f"Total Months : {loan.term_months}")