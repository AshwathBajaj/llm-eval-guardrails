"""Render docs/PROJECT_EXPLAINER.md to docs/PROJECT_EXPLAINER.pdf.

The Markdown file is the source. This script is the print layout: headings,
paragraphs, lists, tables, and fenced code. It uses DejaVu so the PDF does
not depend on a system viewer substituting fonts.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "PROJECT_EXPLAINER.md"
TARGET = ROOT / "docs" / "PROJECT_EXPLAINER.pdf"

_FONT_CANDIDATES = (
    Path("/usr/share/fonts/truetype/dejavu"),
    Path("/usr/share/fonts/dejavu"),
)


def _fonts() -> tuple[Path, Path, Path]:
    for directory in _FONT_CANDIDATES:
        regular = directory / "DejaVuSans.ttf"
        bold = directory / "DejaVuSans-Bold.ttf"
        mono = directory / "DejaVuSansMono.ttf"
        if regular.is_file() and bold.is_file() and mono.is_file():
            return regular, bold, mono
    raise FileNotFoundError("DejaVu Sans fonts were not found")


class Explainer(FPDF):
    def __init__(self, fonts: tuple[Path, Path, Path]) -> None:
        super().__init__(format="A4", unit="mm")
        regular, bold, mono = fonts
        self.add_font("Body", "", str(regular))
        self.add_font("Body", "B", str(bold))
        self.add_font("Mono", "", str(mono))
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)
        self.add_page()

    def footer(self) -> None:
        self.set_y(-12)
        self.set_font("Body", "", 8)
        self.set_text_color(110, 100, 88)
        self.cell(0, 6, f"llmeval  ·  {self.page_no()}", align="C")
        self.set_text_color(28, 23, 18)


def _blocks(markdown: str) -> list[tuple]:
    lines = markdown.splitlines()
    index = 0
    blocks: list[tuple] = []
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith("```"):
            index += 1
            body: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                body.append(lines[index])
                index += 1
            index += 1
            blocks.append(("code", body))
            continue
        if line.startswith("|"):
            rows: list[str] = []
            while index < len(lines) and lines[index].startswith("|"):
                rows.append(lines[index])
                index += 1
            blocks.append(("table", rows))
            continue
        if line.startswith("!["):
            blocks.append(("image", line.strip()))
            index += 1
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            blocks.append(("heading", level, line[level:].strip()))
            index += 1
            continue
        if line.startswith("- "):
            items: list[str] = []
            while index < len(lines) and lines[index].startswith("- "):
                items.append(lines[index][2:].strip())
                index += 1
            blocks.append(("bullets", items))
            continue
        if re.match(r"\d+\. ", line):
            items = []
            while index < len(lines) and re.match(r"\d+\. ", lines[index]):
                items.append(re.sub(r"^\d+\. ", "", lines[index]).strip())
                index += 1
            blocks.append(("numbers", items))
            continue
        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and _continues_paragraph(lines[index]):
            paragraph.append(lines[index].strip())
            index += 1
        blocks.append(("paragraph", " ".join(paragraph)))
    return blocks


def _continues_paragraph(line: str) -> bool:
    if not line.strip():
        return False
    if line.startswith(("#", "-", "|", "`", "!")):
        return False
    return re.match(r"\d+\. ", line) is None


def _code_line(line: str) -> str:
    indent = len(line) - len(line.lstrip(" "))
    # Non-breaking spaces keep the indent. The mono font has no zero-width space.
    return ("\u00a0" * indent) + line.lstrip(" ")


def _soft_breaks(text: str) -> str:
    return text.replace("/", "/\u200b").replace("_", "_\u200b").replace(".", ".\u200b")


def _write_inline(pdf: Explainer, text: str, size: float, height: float) -> None:
    pieces = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for piece in pieces:
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**") and len(piece) >= 4:
            pdf.set_font("Body", "B", size)
            pdf.write(height, piece[2:-2])
            continue
        if piece.startswith("`") and piece.endswith("`") and len(piece) >= 2:
            # Stay on the body font. Switching to monospace mid-line makes
            # fpdf wrap the surrounding word with stray spaces. Zero-width
            # spaces let long identifiers break after _ / . instead of mid-token.
            pdf.set_text_color(122, 42, 16)
            pdf.set_font("Body", "", size)
            pdf.write(height, _soft_breaks(piece[1:-1]))
            pdf.set_text_color(28, 23, 18)
            continue
        pdf.set_font("Body", "", size)
        pdf.write(height, piece)


def _heading(pdf: Explainer, level: int, text: str) -> None:
    if pdf.get_y() > 250 and level > 1:
        pdf.add_page()
    space = {1: 4, 2: 6, 3: 4}.get(level, 3)
    pdf.ln(space)
    size = {1: 20, 2: 14, 3: 12}.get(level, 12)
    pdf.set_font("Body", "B", size)
    pdf.set_text_color(28, 23, 18)
    _write_inline(pdf, text, size, size * 0.45)
    pdf.ln(size * 0.45 + 1)
    if level == 1:
        pdf.set_draw_color(154, 52, 18)
        pdf.set_line_width(0.6)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(3)


def _paragraph(pdf: Explainer, text: str) -> None:
    pdf.set_text_color(28, 23, 18)
    _write_inline(pdf, text, 10.5, 5.2)
    pdf.ln(6.2)


def _list(pdf: Explainer, items: list[str], numbered: bool) -> None:
    for index, item in enumerate(items, start=1):
        marker = f"{index}." if numbered else "•"
        pdf.set_font("Body", "", 10.5)
        pdf.set_text_color(154, 52, 18)
        pdf.write(5.2, f"{marker}  ")
        pdf.set_text_color(28, 23, 18)
        _write_inline(pdf, item, 10.5, 5.2)
        pdf.ln(6)


def _code(pdf: Explainer, lines: list[str]) -> None:
    pdf.ln(1)
    pdf.set_fill_color(244, 239, 230)
    pdf.set_text_color(28, 23, 18)
    pdf.set_font("Mono", "", 8)
    width = pdf.w - pdf.l_margin - pdf.r_margin
    for line in lines or [""]:
        if pdf.get_y() > pdf.page_break_trigger - 6:
            pdf.add_page()
        visible = _code_line(line) if line else " "
        pdf.multi_cell(
            width,
            4.2,
            visible,
            align="L",
            fill=True,
            new_x="LMARGIN",
            new_y="NEXT",
        )
    pdf.ln(2)


def _table(pdf: Explainer, raw_rows: list[str]) -> None:
    parsed: list[list[str]] = []
    for raw in raw_rows:
        cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        parsed.append(cells)
    if not parsed:
        return
    columns = max(len(row) for row in parsed)
    parsed = [row + [""] * (columns - len(row)) for row in parsed]
    usable = pdf.w - pdf.l_margin - pdf.r_margin
    weights = [4.0] * columns
    for row in parsed:
        for index, cell in enumerate(row):
            weights[index] = max(weights[index], min(len(cell), 48) + 2)
    total = sum(weights)
    widths = [usable * weight / total for weight in weights]
    pdf.ln(1)
    for row_index, row in enumerate(parsed):
        _table_row(pdf, row, widths, header=row_index == 0)
    pdf.ln(3)


def _table_row(pdf: Explainer, cells: list[str], widths: list[float], *, header: bool) -> None:
    pdf.set_font("Body", "B" if header else "", 9)
    line_height = 4.4
    heights: list[float] = []
    for cell, width in zip(cells, widths, strict=True):
        lines = pdf.multi_cell(
            width - 2,
            line_height,
            cell,
            dry_run=True,
            output="LINES",
        )
        heights.append(max(line_height, line_height * len(lines)) + 1.6)
    row_height = max(heights)
    if pdf.get_y() + row_height > pdf.page_break_trigger:
        pdf.add_page()
    x_pos = pdf.l_margin
    y_pos = pdf.get_y()
    pdf.set_fill_color(236, 224, 206) if header else pdf.set_fill_color(255, 250, 243)
    pdf.set_draw_color(224, 211, 191)
    for cell, width in zip(cells, widths, strict=True):
        pdf.rect(x_pos, y_pos, width, row_height, style="FD")
        pdf.set_xy(x_pos + 1, y_pos + 0.8)
        pdf.multi_cell(width - 2, line_height, cell)
        x_pos += width
    pdf.set_xy(pdf.l_margin, y_pos + row_height)


def _image(pdf: Explainer, line: str) -> None:
    match = re.search(r"\(([^)]+)\)", line)
    if match is None:
        return
    path = ROOT / match.group(1)
    if not path.is_file():
        _paragraph(pdf, f"(missing image {match.group(1)})")
        return
    width = pdf.w - pdf.l_margin - pdf.r_margin
    if pdf.get_y() > 200:
        pdf.add_page()
    pdf.image(str(path), x=pdf.l_margin, w=width)
    pdf.ln(3)


def render(source: Path, target: Path) -> None:
    pdf = Explainer(_fonts())
    for block in _blocks(source.read_text(encoding="utf-8")):
        kind = block[0]
        if kind == "heading":
            _heading(pdf, block[1], block[2])
        elif kind == "paragraph":
            _paragraph(pdf, block[1])
        elif kind == "bullets":
            _list(pdf, block[1], numbered=False)
        elif kind == "numbers":
            _list(pdf, block[1], numbered=True)
        elif kind == "code":
            _code(pdf, block[1])
        elif kind == "table":
            _table(pdf, block[1])
        elif kind == "image":
            _image(pdf, block[1])
    target.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(target))


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing {SOURCE}", file=sys.stderr)
        return 1
    render(SOURCE, TARGET)
    print(f"wrote {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
