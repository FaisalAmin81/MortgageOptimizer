"""
EMI calculation module.

This module contains functions for calculating the fixed monthly
payment (EMI) for an amortizing loan.
"""

from math import pow


def calculate_emi(
    principal: float,
    annual_rate: float,
    term_months: int
) -> float:
    """
    Calculate the Equated Monthly Installment (EMI).

    Args:
        principal: Loan amount.
        annual_rate: Annual interest rate (e.g. 0.05 for 5%).
        term_months: Total repayment period in months.

    Returns:
        Monthly EMI as a float.
    """

    monthly_rate = annual_rate / 12

    factor = pow(1 + monthly_rate, term_months)

    emi = (
        principal
        * monthly_rate
        * factor
        / (factor - 1)
    )

    return emi