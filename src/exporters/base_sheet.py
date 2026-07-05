from openpyxl.worksheet.worksheet import Worksheet

from src.exporters.models.report_field import ReportField
from src.exporters.models.value_type import ValueType
from src.exporters.styles.workbook_style import WorkbookStyle
from src.models.currency import Currency


class BaseSheet:
    """
    Base renderer for report worksheets.
    Handles formatting, borders, alignment and number formats.
    """

    @staticmethod
    def write_fields(
        sheet: Worksheet,
        fields: list[ReportField],
        currency: Currency,
        start_row: int = 3,
    ) -> None:

        for row_number, field in enumerate(fields, start=start_row):

            label_cell = sheet.cell(row=row_number, column=1)
            value_cell = sheet.cell(row=row_number, column=2)

            label_cell.value = field.label
            value_cell.value = field.value

            # ----------------------------
            # Fonts
            # ----------------------------

            label_cell.font = WorkbookStyle.HEADER_FONT
            value_cell.font = WorkbookStyle.NORMAL_FONT

            # ----------------------------
            # Borders
            # ----------------------------

            label_cell.border = WorkbookStyle.THIN_BORDER
            value_cell.border = WorkbookStyle.THIN_BORDER

            # ----------------------------
            # Alignment
            # ----------------------------

            label_cell.alignment = WorkbookStyle.LEFT
            value_cell.alignment = WorkbookStyle.RIGHT

            # ----------------------------
            # Fill
            # ----------------------------

            label_cell.fill = WorkbookStyle.HEADER_FILL

            if row_number % 2 == 0:
                value_cell.fill = WorkbookStyle.LIGHT_GRAY_FILL

            # ----------------------------
            # Number Formatting
            # ----------------------------

            BaseSheet.apply_number_format(
                value_cell,
                field.value_type,
                currency,
            )

        sheet.freeze_panes = f"A{start_row}"

        sheet.auto_filter.ref = f"A{start_row}:B{start_row + len(fields) - 1}"

        sheet.column_dimensions["A"].width = 30
        sheet.column_dimensions["B"].width = 22

    @staticmethod
    def apply_number_format(
        cell,
        value_type: str,
        currency: Currency,
    ) -> None:

        if value_type == ValueType.CURRENCY:

            decimals = "0" * currency.decimal_places

            cell.number_format = f'"{currency.symbol}"#,##0.{decimals}'

        elif value_type == ValueType.PERCENT:

            cell.number_format = WorkbookStyle.PERCENT

        elif value_type == ValueType.INTEGER:

            cell.number_format = WorkbookStyle.INTEGER
