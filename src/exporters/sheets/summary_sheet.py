from openpyxl import Workbook
from datetime import datetime
from src.config.app_config import AppConfig
from src.exporters.base_sheet import BaseSheet
from src.exporters.models.report_field import ReportField
from src.exporters.models.value_type import ValueType
from src.exporters.styles.workbook_style import WorkbookStyle
from src.models.simulation_result import SimulationResult
from src.services.statistics_service import StatisticsService
from src.exporters.base_sheet import BaseSheet


class SummarySheet:
    """
    Creates the Summary worksheet.
    """

    @staticmethod
    def build(
        workbook: Workbook,
        result: SimulationResult,
    ) -> None:

        sheet = workbook["Summary"]

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        sheet.merge_cells("A1:B1")

        title = sheet["A1"]
        title.value = "Mortgage Optimization Summary"
        title.font = WorkbookStyle.TITLE_FONT
        title.alignment = WorkbookStyle.CENTER

        # -------------------------------------------------
        # Generated Timestamp
        # -------------------------------------------------

        sheet["A2"] = "Generated"
        sheet["B2"] = datetime.now().strftime("%d-%b-%Y %H:%M")

        rows = [
            ReportField(
                "Original Loan",
                result.loan.principal,
                ValueType.CURRENCY,
            ),
            ReportField(
                "Interest Rate",
                result.loan.annual_rate,
                ValueType.PERCENT,
            ),
            ReportField(
                "Original EMI",
                result.loan.emi,
                ValueType.CURRENCY,
            ),
            ReportField(
                "Loan Term (Months)",
                result.loan.term_months,
                ValueType.INTEGER,
            ),
            ReportField(
                "Months Simulated",
                StatisticsService.total_months(result),
                ValueType.INTEGER,
            ),
            ReportField(
                "Final Balance",
                StatisticsService.final_balance(result),
                ValueType.CURRENCY,
            ),
            ReportField(
                "Principal Paid",
                StatisticsService.total_principal(result),
                ValueType.CURRENCY,
            ),
            ReportField(
                "Interest Paid",
                StatisticsService.total_interest(result),
                ValueType.CURRENCY,
            ),
            ReportField(
                "Settlements",
                StatisticsService.total_settlements(result),
                ValueType.INTEGER,
            ),
            ReportField(
                "Remaining Savings",
                StatisticsService.total_savings(result),
                ValueType.CURRENCY,
            ),
        ]

        BaseSheet.write_fields(
            sheet=sheet,
            fields=rows,
            currency=AppConfig.DEFAULT_CURRENCY,
        )
