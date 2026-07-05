# from unittest import result


from src.config.app_config import AppConfig
from src.core.simulation import SimulationEngine
from src.models.loan import Loan
from src.models.mortgage_context import MortgageContext
from src.models.settlement_rule import SettlementRule
from src.services.statistics_service import StatisticsService
from src.exporters.excel_exporter import ExcelExporter


def main() -> None:
    """
    Mortgage Optimizer demo.
    """

    # -------------------------------------------------
    # Loan
    # -------------------------------------------------

    loan = Loan(
        principal=8_000_000,
        annual_rate=0.05,
        term_months=156,
        emi=69_845,
    )

    # -------------------------------------------------
    # Settlement rule (Bank rules)
    # -------------------------------------------------

    settlement_rule = SettlementRule(
        minimum_amount=500_000,
        reduce_emi=True,
    )

    # -------------------------------------------------
    # Build simulation context
    # -------------------------------------------------

    context = MortgageContext.create(
        loan=loan,
        currency=AppConfig.DEFAULT_CURRENCY,
        settlement_rule=settlement_rule,
    )
    print(context)
    print(type(context))
    print(hasattr(context, "monthly_snapshots"))

    # -------------------------------------------------
    # Run simulation
    # -------------------------------------------------

    result = SimulationEngine.run(context)

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    print("\n" + "=" * 60)
    print("MORTGAGE SIMULATION SUMMARY")
    print("=" * 60)
    print(f"Settlements executed    : {context.settlement_history.count}")
    print(f"Loan balance            : {context.state.balance:,.2f}")
    print(f"Current EMI             : {context.state.current_emi:,.2f}")
    print(f"Savings balance         : {context.savings.balance:,.2f}")
    print(f"Interest paid           : {context.state.total_interest_paid:,.2f}")
    print(f"Principal paid          : {context.state.total_principal_paid:,.2f}")

    print()

    # -------------------------------------------------
    # Settlement History
    # -------------------------------------------------

    if context.settlement_history.count:

        print("=" * 60)
        print("SETTLEMENT HISTORY")
        print("=" * 60)

        for settlement in context.settlement_history.settlements:

            print(
                f"Settlement #{settlement.number}"
                f" | Month {settlement.month}"
                f" | Amount {settlement.amount:,.2f}"
                f" | Balance {settlement.balance_before:,.2f}"
                f" -> {settlement.balance_after:,.2f}"
                f" | EMI {settlement.emi_before:,.2f}"
                f" -> {settlement.emi_after:,.2f}"
            )

    print()

    # -------------------------------------------------
    # First few monthly snapshots
    # -------------------------------------------------

    print("=" * 60)
    print("FIRST 5 MONTHLY SNAPSHOTS")
    print("=" * 60)

    for snapshot in context.monthly_snapshots[:5]:
        print(snapshot)

    print()

    print("=" * 60)
    print("LAST 5 MONTHLY SNAPSHOTS")
    print("=" * 60)

    for snapshot in context.monthly_snapshots[-5:]:
        print(snapshot)

    print(result.snapshots)

    print(result.settlement_history)

    print(result.savings)

    print(StatisticsService.total_interest(result))

    print(StatisticsService.total_months(result))

    print(StatisticsService.total_settlements(result))

    ExcelExporter.export(result)


if __name__ == "__main__":
    main()
