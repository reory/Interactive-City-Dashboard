"""PDF report generation utilities."""

from datetime import UTC, datetime
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def generate_dashboard_report(
    city_name: str,
    city_data: dict,
    summary: str,
    chart_png: bytes,
    map_png: bytes,
) -> bytes:
    """Generate a dashboard PDF report."""

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    styles["Heading2"].textColor = colors.darkblue

    content = []

    generated_time = datetime.now(UTC).strftime(
        "%Y-%m-%d %H:%M UTC"
    )

    # Header

    content.append(
        Paragraph(
            "🌍 Interactive City Dashboard",
            styles["Title"],
        )
    )

    content.append(
        Paragraph(
            city_name,
            styles["Heading1"],
        )
    )

    content.append(Spacer(1, 4))

    # City information table

    stats_table = Table(
        [
            ["City", city_name],
            ["Continent", city_data["continent"]],
            ["Population", f"{city_data['pop']:,}"],
            ["Latitude", str(city_data["lat"])],
            ["Longitude", str(city_data["lon"])],
        ],
        colWidths=[100, 220],
    )

    stats_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ]
        )
    )

    content.append(stats_table)

    content.append(Spacer(1, 6))

    # Population chart

    content.append(HRFlowable())

    content.append(
        Paragraph(
            "Population Chart",
            styles["Heading2"],
        )
    )

    content.append(Spacer(1, 4))

    chart_image = Image(BytesIO(chart_png))
    chart_image.drawWidth = 5 * inch
    chart_image.drawHeight = 3 * inch

    content.append(chart_image)

    content.append(Spacer(1, 6))

    # Map

    content.append(HRFlowable())

    content.append(
        Paragraph(
            "City Map",
            styles["Heading2"],
        )
    )

    content.append(Spacer(1, 4))

    map_image = Image(BytesIO(map_png))
    map_image.drawWidth = 5 * inch
    map_image.drawHeight = 3 * inch

    content.append(map_image)

    content.append(Spacer(1, 6))

    # Wikipedia

    content.append(HRFlowable())

    content.append(
        Paragraph(
            "Wikipedia Summary",
            styles["Heading2"],
        )
    )

    content.append(Spacer(1, 4))

    content.append(
        Paragraph(
            summary.replace("\n", "<br/>"),
            styles["BodyText"],
        )
    )

    content.append(Spacer(1, 6))

    # Footer

    content.append(HRFlowable())

    content.append(
        Paragraph(
            f"Generated: {generated_time}",
            styles["Italic"],
        )
    )

    doc.build(content)

    pdf_bytes = buffer.getvalue()

    buffer.close()

    return pdf_bytes