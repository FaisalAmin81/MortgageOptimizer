from src.logging.logger import logger
from src.models.savings import Savings
from src.models.transaction import Transaction


class SavingsService:
    """Service for managing savings deposits and withdrawals."""

    @staticmethod
    def deposit(
        savings: Savings,
        month: int,
        description: str,
        amount: float,
    ) -> None:
        """Deposit money into savings."""

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        savings.balance += amount

        savings.transactions.append(
            Transaction(
                month=month,
                description=description,
                deposit=amount,
                withdrawal=0.0,
                balance=savings.balance,
            )
        )

        logger.info(
            "Deposit | Month=%d | Description=%s | Amount=%.2f | Balance=%.2f",
            month,
            description,
            amount,
            savings.balance,
        )

    @staticmethod
    def withdraw(
        savings: Savings,
        month: int,
        description: str,
        amount: float,
    ) -> None:
        """Withdraw money from savings."""

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > savings.balance:
            raise ValueError("Insufficient savings.")

        savings.balance -= amount

        savings.transactions.append(
            Transaction(
                month=month,
                description=description,
                deposit=0.0,
                withdrawal=amount,
                balance=savings.balance,
            )
        )

        logger.info(
            "Withdrawal | Month=%d | Description=%s | Amount=%.2f | Balance=%.2f",
            month,
            description,
            amount,
            savings.balance,
        )