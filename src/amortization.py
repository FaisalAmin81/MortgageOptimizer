from src.models import Payment


def generate_schedule(loan):

    schedule = []

    balance = loan.principal

    for month in range(1, loan.term_months + 1):

        opening_balance = balance

        interest = loan.monthly_interest(opening_balance)

        principal = loan.emi - interest

        closing_balance = opening_balance - principal

        if closing_balance < 0:
            closing_balance = 0

        payment = Payment(
            month=month,
            opening_balance=opening_balance,
            emi=loan.emi,
            interest=interest,
            principal=principal,
            closing_balance=closing_balance
        )

        schedule.append(payment)

        balance = closing_balance

        if balance == 0:
            break

    return schedule