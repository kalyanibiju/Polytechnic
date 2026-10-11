import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

# Define NumberedCanvas for Running Header and Footer (Page X of Y)
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        self.saveState()
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A")) # Primary Dark Blue
            self.drawString(36, 762, "DIPLOMA IN AI & ML — DISCRETE MATHEMATICS (3341)")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawRightString(576, 762, "MODULE 1: MATHEMATICAL LOGIC | SHORT NOTES")
            
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 754, 576, 754)

        # Footer (All pages)
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1E3A8A"))
        self.drawString(36, 25, "DEPARTMENT OF TECHNICAL EDUCATION — POLYTECHNIC COLLEGE")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(310, 25, "Strictly Prescribed Textbooks (Rosen, Grimaldi, Koshy)")
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1E3A8A"))
        self.drawRightString(576, 25, page_str)
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 36, 576, 36)
        
        self.restoreState()


def build_pdf():
    output_dir = os.path.join(os.getcwd(), "Short Notes")
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "Module_1_Discrete_Mathematics_Short_Notes.pdf")

    # Document setup: 0.5 in margins = 36 pt
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    C_PRIMARY = colors.HexColor("#1E3A8A")    # Deep Blue
    C_SECONDARY = colors.HexColor("#0D9488")  # Teal
    C_TEXT = colors.HexColor("#0F172A")       # Dark Slate
    C_MUTED = colors.HexColor("#475569")      # Muted Slate
    C_BG_BOX = colors.HexColor("#F0F9FF")     # Soft Blue Callout
    C_BG_TIP = colors.HexColor("#FEF3C7")     # Soft Amber Tip Box
    C_BORDER = colors.HexColor("#BAE6FD")     # Border color for callouts
    C_BORDER_TIP = colors.HexColor("#FDE68A")

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=C_PRIMARY,
        alignment=1, # Center
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=C_SECONDARY,
        alignment=1,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=C_PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=C_SECONDARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=C_TEXT,
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'Body_Bold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#991B1B"), # Dark red
        backColor=colors.HexColor("#F8FAFC"),
        borderColor=colors.HexColor("#E2E8F0"),
        borderWidth=0.5,
        borderPadding=4,
        spaceAfter=6
    )

    callout_text = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#0369A1")
    )

    tip_text = ParagraphStyle(
        'TipText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#92400E")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=C_TEXT
    )

    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=table_cell_style,
        alignment=1
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=table_cell_style,
        fontName='Helvetica-Bold'
    )

    story = []

    def make_callout(text, title="DEFINITION / LECTURER NOTE"):
        p_title = Paragraph(f"<b>{title}</b>", ParagraphStyle('CTitle', parent=callout_text, fontName='Helvetica-Bold', fontSize=9.5, spaceAfter=3, textColor=colors.HexColor("#075985")))
        p_body = Paragraph(text, callout_text)
        t = Table([[ [p_title, p_body] ]], colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), C_BG_BOX),
            ('BOX', (0,0), (-1,-1), 1, C_BORDER),
            ('PADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return t

    def make_tip(text, title="EXAM TIP & COMMON PITFALLS"):
        p_title = Paragraph(f"<b>{title}</b>", ParagraphStyle('TTitle', parent=tip_text, fontName='Helvetica-Bold', fontSize=9.5, spaceAfter=3, textColor=colors.HexColor("#B45309")))
        p_body = Paragraph(text, tip_text)
        t = Table([[ [p_title, p_body] ]], colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), C_BG_TIP),
            ('BOX', (0,0), (-1,-1), 1, C_BORDER_TIP),
            ('PADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return t

    # ---------------------------------------------------------
    # COVER / HEADER BANNER
    # ---------------------------------------------------------
    header_data = [
        [Paragraph("<b>STATE BOARD OF TECHNICAL EDUCATION — DIPLOMA COURSE NOTES</b>", ParagraphStyle('H1', parent=table_header_style, fontSize=10, leading=12))],
        [Paragraph("<b>COURSE: DISCRETE MATHEMATICS (COURSE CODE: 3341)</b>", ParagraphStyle('H2', parent=table_header_style, fontSize=14, leading=17))],
        [Paragraph("SEMESTER III | DIPLOMA IN ARTIFICIAL INTELLIGENCE & MACHINE LEARNING", ParagraphStyle('H3', parent=table_header_style, fontSize=9.5, leading=12))]
    ]
    header_table = Table(header_data, colWidths=[540])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("MODULE 1: MATHEMATICAL LOGIC", title_style))
    story.append(Paragraph("Comprehensive Senior Lecturer Short Notes & Exam Preparation Guide", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=2, spaceAfter=10))

    # Meta Info Card
    meta_text = (
        "<b>Course Outcome CO1:</b> Apply the basic concepts of mathematical logic to solve problems.<br/>"
        "<b>Duration:</b> 16 Hours | <b>Cognitive Level:</b> Applying<br/>"
        "<b>Prescribed Textbooks:</b> (1) Kenneth H. Rosen (7th Ed), (2) Ralph P. Grimaldi (5th Ed), (3) Thomas Koshy (2nd Ed)."
    )
    story.append(make_callout(meta_text, "COURSE SYLLABUS ALIGNMENT & OBJECTIVES"))
    story.append(Spacer(1, 12))

    # ---------------------------------------------------------
    # SECTION 1: PROPOSITIONAL LOGIC & OPERATIONS
    # ---------------------------------------------------------
    story.append(Paragraph("1. Propositional Logic & Logical Operations", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("1.1 Concept of Propositional Logic (M1.01)", h2_style))
    story.append(Paragraph(
        "<b>Definition (Proposition / Statement):</b> A <i>proposition</i> (or statement) is a declarative sentence that is either <b>True (T)</b> or <b>False (F)</b>, but not both. The truth value of a proposition is denoted by T (or 1) for true and F (or 0) for false.",
        body_style
    ))
    
    # Examples Table
    eg_data = [
        [Paragraph("<b>Sentence</b>", table_header_style), Paragraph("<b>Is it a Proposition?</b>", table_header_style), Paragraph("<b>Reason / Truth Value</b>", table_header_style)],
        [Paragraph("Kerala is a state in India.", table_cell_style), Paragraph("<b>YES</b>", table_cell_center), Paragraph("Declarative sentence; Truth Value = <b>T</b>", table_cell_style)],
        [Paragraph("2 + 3 = 7", table_cell_style), Paragraph("<b>YES</b>", table_cell_center), Paragraph("Declarative sentence; Truth Value = <b>F</b>", table_cell_style)],
        [Paragraph("What time is it?", table_cell_style), Paragraph("<b>NO</b>", table_cell_center), Paragraph("Interrogative sentence (Question)", table_cell_style)],
        [Paragraph("Solve this equation immediately!", table_cell_style), Paragraph("<b>NO</b>", table_cell_center), Paragraph("Imperative sentence (Command)", table_cell_style)],
        [Paragraph("x + 5 = 12", table_cell_style), Paragraph("<b>NO</b>", table_cell_center), Paragraph("Open sentence; value depends on variable <i>x</i>", table_cell_style)]
    ]
    t_eg = Table(eg_data, colWidths=[180, 110, 250])
    t_eg.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_eg)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Atomic vs. Compound Propositions:</b>", body_bold))
    story.append(Paragraph(
        "• <b>Atomic (Primitive) Proposition:</b> A simple proposition that cannot be broken down into simpler propositions (e.g., <i>p: 'It is raining'</i>).<br/>"
        "• <b>Compound Proposition:</b> Formed by combining two or more atomic propositions using <b>logical connectives</b> (e.g., <i>p ∧ q: 'It is raining AND it is cold'</i>).",
        body_style
    ))

    story.append(Paragraph("1.2 Logical Connectives & Fundamental Truth Tables (M1.02)", h2_style))
    story.append(Paragraph(
        "Logical connectives combine propositions. Let <i>p</i> and <i>q</i> be propositions:",
        body_style
    ))

    # Connectives Table
    conn_data = [
        [Paragraph("<b>Connective</b>", table_header_style), Paragraph("<b>Symbol</b>", table_header_style), Paragraph("<b>Logical Name</b>", table_header_style), Paragraph("<b>Meaning / Condition for Truth</b>", table_header_style)],
        [Paragraph("NOT", table_cell_center), Paragraph("¬  (or ~)", table_cell_center), Paragraph("Negation", table_cell_style), Paragraph("Reverses truth value. True when proposition is false.", table_cell_style)],
        [Paragraph("AND", table_cell_center), Paragraph("∧", table_cell_center), Paragraph("Conjunction", table_cell_style), Paragraph("True <b>ONLY when BOTH</b> <i>p</i> and <i>q</i> are True.", table_cell_style)],
        [Paragraph("OR", table_cell_center), Paragraph("∨", table_cell_center), Paragraph("Disjunction (Inclusive)", table_cell_style), Paragraph("True when <b>AT LEAST ONE</b> of <i>p, q</i> is True.", table_cell_style)],
        [Paragraph("XOR", table_cell_center), Paragraph("⊕", table_cell_center), Paragraph("Exclusive-OR", table_cell_style), Paragraph("True when <b>EXACTLY ONE</b> of <i>p, q</i> is True (differs).", table_cell_style)],
        [Paragraph("IF...THEN", table_cell_center), Paragraph("→", table_cell_center), Paragraph("Implication / Conditional", table_cell_style), Paragraph("False <b>ONLY when</b> <i>p</i> is True and <i>q</i> is False.", table_cell_style)],
        [Paragraph("IFF", table_cell_center), Paragraph("↔", table_cell_center), Paragraph("Biconditional", table_cell_style), Paragraph("True when <i>p</i> and <i>q</i> have the <b>SAME</b> truth value.", table_cell_style)]
    ]
    t_conn = Table(conn_data, colWidths=[70, 70, 130, 270])
    t_conn.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_conn)
    story.append(Spacer(1, 10))

    # Complete Combined Truth Table
    story.append(Paragraph("<b>Master Truth Table for All Basic Logical Connectives:</b>", body_bold))
    tt_data = [
        [Paragraph("<b>p</b>", table_header_style), Paragraph("<b>q</b>", table_header_style), 
         Paragraph("<b>¬p</b>", table_header_style), Paragraph("<b>p ∧ q</b>", table_header_style), 
         Paragraph("<b>p ∨ q</b>", table_header_style), Paragraph("<b>p ⊕ q</b>", table_header_style), 
         Paragraph("<b>p → q</b>", table_header_style), Paragraph("<b>p ↔ q</b>", table_header_style)],
        [Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<font color='#DC2626'><b>F</b></font>", table_cell_center), Paragraph("F", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("F", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
    ]
    t_master = Table(tt_data, colWidths=[67.5]*8)
    t_master.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#94A3B8")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F1F5F9")]),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_master)
    story.append(Spacer(1, 8))

    story.append(make_tip(
        "<b>Understanding Implication (p → q):</b><br/>"
        "• <i>p</i> is called the <b>Hypothesis (Antecedent)</b>; <i>q</i> is called the <b>Conclusion (Consequent)</b>.<br/>"
        "• The statement <i>p → q</i> is False <b>ONLY</b> when a True hypothesis leads to a False conclusion (Row 2).<br/>"
        "• When <i>p</i> is False (Rows 3 & 4), the implication <i>p → q</i> is automatically <b>TRUE</b> regardless of <i>q</i>. This is called a <b>vacuous truth</b> in mathematics!",
        "LECTURER'S DEEP DIVE ON IMPLICATION"
    ))
    story.append(Spacer(1, 10))

    # Step-by-Step Truth Table Construction Example
    story.append(Paragraph("1.3 Step-by-Step Problem Solving: Truth Table Construction", h2_style))
    story.append(Paragraph(
        "<b>Problem 1:</b> Construct the truth table for the compound proposition <i>(p ∨ ¬q) → (p ∧ q)</i>.",
        body_bold
    ))
    story.append(Paragraph(
        "<b>Methodology:</b> For <i>n</i> variables, construct a table with 2<sup><i>n</i></sup> rows (here <i>n</i>=2, so 4 rows). Evaluate sub-expressions column by column from inside out.",
        body_style
    ))

    sol1_data = [
        [Paragraph("<b>Row</b>", table_header_style), Paragraph("<b>p</b>", table_header_style), Paragraph("<b>q</b>", table_header_style), Paragraph("<b>¬q</b>", table_header_style), Paragraph("<b>p ∨ ¬q</b> (A)", table_header_style), Paragraph("<b>p ∧ q</b> (B)", table_header_style), Paragraph("<b>A → B</b>", table_header_style)],
        [Paragraph("1", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("2", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<font color='#DC2626'><b>F</b></font>", table_cell_center)],
        [Paragraph("3", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("4", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<font color='#DC2626'><b>F</b></font>", table_cell_center)],
    ]
    t_sol1 = Table(sol1_data, colWidths=[40, 60, 60, 70, 110, 100, 100])
    t_sol1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sol1)
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 2: IMPLICATION VARIANTS & TRUTH CLASSIFICATIONS
    # ---------------------------------------------------------
    story.append(Paragraph("2. Implication Variants, Truth Classifications & Normal Forms", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("2.1 Variants of Conditional Statements (M1.03)", h2_style))
    story.append(Paragraph(
        "Given an implication <b>p → q</b>, three related conditional statements can be formed:",
        body_style
    ))

    # Conditional variants table
    var_data = [
        [Paragraph("<b>Statement Name</b>", table_header_style), Paragraph("<b>Symbolic Form</b>", table_header_style), Paragraph("<b>English Translation</b>", table_header_style), Paragraph("<b>Logical Equivalence</b>", table_header_style)],
        [Paragraph("<b>Original Implication</b>", table_cell_style), Paragraph("<b>p → q</b>", table_cell_center), Paragraph("If p, then q", table_cell_style), Paragraph("Equivalence baseline", table_cell_style)],
        [Paragraph("<b>Converse</b>", table_cell_style), Paragraph("<b>q → p</b>", table_cell_center), Paragraph("If q, then p", table_cell_style), Paragraph("Equivalent to Inverse (<b>¬p → ¬q</b>)", table_cell_style)],
        [Paragraph("<b>Inverse</b>", table_cell_style), Paragraph("<b>¬p → ¬q</b>", table_cell_center), Paragraph("If not p, then not q", table_cell_style), Paragraph("Equivalent to Converse (<b>q → p</b>)", table_cell_style)],
        [Paragraph("<b>Contrapositive</b>", table_cell_style), Paragraph("<b>¬q → ¬p</b>", table_cell_center), Paragraph("If not q, then not p", table_cell_style), Paragraph("<b>STRICTLY EQUIVALENT to p → q</b>", table_cell_style)]
    ]
    t_var = Table(var_data, colWidths=[130, 90, 150, 170])
    t_var.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_var)
    story.append(Spacer(1, 8))

    story.append(make_callout(
        "<b>CRITICAL LECTURER RULE:</b><br/>"
        "An implication <i>p → q</i> and its <b>Contrapositive (¬q → ¬p)</b> ALWAYS have identical truth values in every row of a truth table! Hence, <b>p → q ≡ ¬q → ¬p</b>.<br/>"
        "However, the Converse (<i>q → p</i>) and Inverse (<i>¬p → ¬q</i>) are NOT logically equivalent to the original implication!",
        "KEY EXAMINATION FACT"
    ))
    story.append(Spacer(1, 10))

    # Worked Example Converse/Inverse/Contrapositive
    story.append(Paragraph("<b>Worked Example:</b> Write the Converse, Inverse, and Contrapositive of the statement:<br/>"
                           "<i>'If a polygon is a square (p), then it is a rectangle (q).'</i>", body_bold))
    story.append(Paragraph(
        "• <b>Converse (q → p):</b> If a polygon is a rectangle, then it is a square. (False)<br/>"
        "• <b>Inverse (¬p → ¬q):</b> If a polygon is not a square, then it is not a rectangle. (False)<br/>"
        "• <b>Contrapositive (¬q → ¬p):</b> If a polygon is not a rectangle, then it is not a square. (True)",
        body_style
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("2.2 Tautology, Contradiction, and Contingency (M1.03)", h2_style))
    story.append(Paragraph(
        "Based on their final truth values across all possible truth assignments, compound propositions are classified into three mutually exclusive categories:",
        body_style
    ))

    # Tautology table
    class_data = [
        [Paragraph("<b>Classification</b>", table_header_style), Paragraph("<b>Definition</b>", table_header_style), Paragraph("<b>Standard Example</b>", table_header_style), Paragraph("<b>Truth Table Characteristic</b>", table_header_style)],
        [Paragraph("<b>Tautology (T)</b>", table_cell_style), Paragraph("A compound proposition that is <b>ALWAYS TRUE</b> under all truth assignments.", table_cell_style), Paragraph("<i>p ∨ ¬p</i>", table_cell_center), Paragraph("Final column contains <b>ONLY T</b>", table_cell_style)],
        [Paragraph("<b>Contradiction (F)</b>", table_cell_style), Paragraph("A compound proposition that is <b>ALWAYS FALSE</b> under all truth assignments.", table_cell_style), Paragraph("<i>p ∧ ¬p</i>", table_cell_center), Paragraph("Final column contains <b>ONLY F</b>", table_cell_style)],
        [Paragraph("<b>Contingency</b>", table_cell_style), Paragraph("A compound proposition that is <b>NEITHER</b> a tautology nor a contradiction.", table_cell_style), Paragraph("<i>p → q</i>", table_cell_center), Paragraph("Final column has a <b>MIX of T and F</b>", table_cell_style)]
    ]
    t_class = Table(class_data, colWidths=[110, 180, 100, 150])
    t_class.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_class)
    story.append(Spacer(1, 8))

    # Proof of Tautology Example
    story.append(Paragraph("<b>Problem 2:</b> Prove that <i>(p ∧ (p → q)) → q</i> is a Tautology using a Truth Table.", body_bold))
    sol2_data = [
        [Paragraph("<b>p</b>", table_header_style), Paragraph("<b>q</b>", table_header_style), Paragraph("<b>p → q</b>", table_header_style), Paragraph("<b>p ∧ (p → q)</b>", table_header_style), Paragraph("<b>[p ∧ (p → q)] → q</b>", table_header_style)],
        [Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
    ]
    t_sol2 = Table(sol2_data, colWidths=[70, 70, 120, 140, 140])
    t_sol2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_sol2)
    story.append(Paragraph("<i>Conclusion: Since all entries in the final column are T, (p ∧ (p → q)) → q is a Tautology. (This is the basis of Modus Ponens!).</i>", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2.3 Normal Forms: DNF and CNF", h2_style))
    story.append(Paragraph(
        "In propositional logic, any compound proposition can be represented in standardized canonical forms:<br/>"
        "• <b>Literal:</b> A variable <i>p</i> or its negation <i>¬p</i>.<br/>"
        "• <b>Disjunctive Normal Form (DNF / Sum-of-Products):</b> A disjunction (OR) of minterms, where each minterm is a conjunction (AND) of literals. Formed by selecting rows where the output is <b>TRUE (T)</b>.<br/>"
        "• <b>Conjunctive Normal Form (CNF / Product-of-Sums):</b> A conjunction (AND) of maxterms, where each maxterm is a disjunction (OR) of literals. Formed by taking negated literals for rows where output is <b>FALSE (F)</b>.",
        body_style
    ))
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 3: LOGICAL EQUIVALENCE & DUALITY PRINCIPLE
    # ---------------------------------------------------------
    story.append(Paragraph("3. Logical Equivalence & Duality Principle", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("3.1 Fundamental Laws of Logical Equivalences (M1.03)", h2_style))
    story.append(Paragraph(
        "Two propositions <i>A</i> and <i>B</i> are <b>logically equivalent (A ≡ B or A ⇔ B)</b> if <i>A ↔ B</i> is a tautology. The fundamental algebraic laws of logic (prescribed in Rosen & Grimaldi) allow simplification of logic circuits and algebraic proofs without truth tables.",
        body_style
    ))

    # Laws Table
    laws_data = [
        [Paragraph("<b>Law Category</b>", table_header_style), Paragraph("<b>Equivalence Statement 1 (AND / OR)</b>", table_header_style), Paragraph("<b>Equivalence Statement 2 (Dual Form)</b>", table_header_style)],
        [Paragraph("<b>Identity Laws</b>", table_cell_bold), Paragraph("p ∧ T ≡ p", table_cell_style), Paragraph("p ∨ F ≡ p", table_cell_style)],
        [Paragraph("<b>Domination Laws</b>", table_cell_bold), Paragraph("p ∨ T ≡ T", table_cell_style), Paragraph("p ∧ F ≡ F", table_cell_style)],
        [Paragraph("<b>Idempotent Laws</b>", table_cell_bold), Paragraph("p ∨ p ≡ p", table_cell_style), Paragraph("p ∧ p ≡ p", table_cell_style)],
        [Paragraph("<b>Double Negation Law</b>", table_cell_bold), Paragraph("¬(¬p) ≡ p", table_cell_style), Paragraph("—", table_cell_center)],
        [Paragraph("<b>Commutative Laws</b>", table_cell_bold), Paragraph("p ∨ q ≡ q ∨ p", table_cell_style), Paragraph("p ∧ q ≡ q ∧ p", table_cell_style)],
        [Paragraph("<b>Associative Laws</b>", table_cell_bold), Paragraph("(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)", table_cell_style), Paragraph("(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)", table_cell_style)],
        [Paragraph("<b>Distributive Laws</b>", table_cell_bold), Paragraph("p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)", table_cell_style), Paragraph("p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)", table_cell_style)],
        [Paragraph("<b>De Morgan's Laws</b>", table_cell_bold), Paragraph("<b>¬(p ∧ q) ≡ ¬p ∨ ¬q</b>", table_cell_style), Paragraph("<b>¬(p ∨ q) ≡ ¬p ∧ ¬q</b>", table_cell_style)],
        [Paragraph("<b>Absorption Laws</b>", table_cell_bold), Paragraph("p ∨ (p ∧ q) ≡ p", table_cell_style), Paragraph("p ∧ (p ∨ q) ≡ p", table_cell_style)],
        [Paragraph("<b>Negation / Inverse Laws</b>", table_cell_bold), Paragraph("p ∨ ¬p ≡ T", table_cell_style), Paragraph("p ∧ ¬p ≡ F", table_cell_style)],
        [Paragraph("<b>Conditional Equivalences</b>", table_cell_bold), Paragraph("<b>p → q ≡ ¬p ∨ q</b>", table_cell_style), Paragraph("<b>p ↔ q ≡ (p → q) ∧ (q → p)</b>", table_cell_style)]
    ]
    t_laws = Table(laws_data, colWidths=[140, 200, 200])
    t_laws.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_laws)
    story.append(Spacer(1, 10))

    # Problem 3: Algebraic Proof
    story.append(Paragraph("<b>Problem 3 (Algebraic Proof without Truth Table):</b> Prove that <i>¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q</i>.", body_bold))
    proof_text = (
        "<b>Proof:</b><br/>"
        "1. <i>¬(p ∨ (¬p ∧ q))</i> &nbsp;&nbsp;≡&nbsp;&nbsp; <i>¬p ∧ ¬(¬p ∧ q)</i> &nbsp;&nbsp;&nbsp;&nbsp;[By De Morgan's Law]<br/>"
        "2. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≡&nbsp;&nbsp; <i>¬p ∧ (¬(¬p) ∨ ¬q)</i> &nbsp;&nbsp;[By De Morgan's Law]<br/>"
        "3. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≡&nbsp;&nbsp; <i>¬p ∧ (p ∨ ¬q)</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[By Double Negation Law]<br/>"
        "4. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≡&nbsp;&nbsp; <i>(¬p ∧ p) ∨ (¬p ∧ ¬q)</i> &nbsp;&nbsp;[By Distributive Law]<br/>"
        "5. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≡&nbsp;&nbsp; <i>F ∨ (¬p ∧ ¬q)</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[By Negation Law (¬p ∧ p ≡ F)]<br/>"
        "6. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≡&nbsp;&nbsp; <i>¬p ∧ ¬q</i> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[By Identity Law (F ∨ A ≡ A)] <b>Q.E.D.</b>"
    )
    story.append(Paragraph(proof_text, code_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3.2 Duality Principle", h2_style))
    story.append(Paragraph(
        "<b>Definition (Dual of a Proposition):</b> Let <i>s</i> be a compound proposition containing only connectives ∧, ∨, and ¬. The <b>dual of s</b>, denoted by <b>s*</b>, is obtained by replacing:<br/>"
        "• Every <b>∧</b> with <b>∨</b>, and every <b>∨</b> with <b>∧</b>.<br/>"
        "• Every <b>T (Tautology)</b> with <b>F (Contradiction)</b>, and every <b>F</b> with <b>T</b>.<br/>"
        "• <i>Note:</i> Negations (¬) remain completely UNCHANGED!",
        body_style
    ))
    story.append(Paragraph(
        "<b>Principle of Duality:</b> If two compound propositions <i>s</i> and <i>t</i> are logically equivalent (<i>s ≡ t</i>), then their duals are also logically equivalent (<b>s* ≡ t*</b>).",
        body_style
    ))
    
    dual_eg = (
        "<b>Examples of Duality:</b><br/>"
        "1. Statement: <i>(p ∧ q) ∨ T</i> &nbsp;⇒&nbsp; Dual: <b>(p ∨ q) ∧ F</b><br/>"
        "2. Identity: <i>p ∨ (p ∧ q) ≡ p</i> &nbsp;⇒&nbsp; Dual Identity: <b>p ∧ (p ∨ q) ≡ p</b> (Absorption Law dual!)"
    )
    story.append(make_callout(dual_eg, "DUALITY WORKED EXAMPLES"))
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 4: PREDICATE LOGIC & QUANTIFIERS
    # ---------------------------------------------------------
    story.append(Paragraph("4. Predicate Logic & Quantifiers", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("4.1 Predicates & Propositional Functions (M1.04)", h2_style))
    story.append(Paragraph(
        "Propositional logic cannot express statements like <i>'All prime numbers are odd except 2'</i>. Predicate logic extends propositional logic by introducing variables and predicates.<br/>"
        "• <b>Predicate:</b> A statement of the form <i>P(x)</i> where <i>x</i> is the subject variable and <i>P</i> is the predicate property assigned to <i>x</i>.<br/>"
        "• <b>Domain (Universe of Discourse U):</b> The set of all possible values that variable <i>x</i> can take.<br/>"
        "• <b>Well-Formed Formula (WFF):</b> A syntactically correct expression constructed using predicates, variables, connectives, and quantifiers.",
        body_style
    ))

    story.append(Paragraph("4.2 Quantifiers (Universal & Existential)", h2_style))
    story.append(Paragraph(
        "Quantifiers express the extent to which a predicate applies over a domain <i>U</i>:",
        body_style
    ))

    # Quantifiers Table
    quant_data = [
        [Paragraph("<b>Quantifier Name</b>", table_header_style), Paragraph("<b>Symbolic Form</b>", table_header_style), Paragraph("<b>Meaning in English</b>", table_header_style), Paragraph("<b>When is it TRUE?</b>", table_header_style), Paragraph("<b>When is it FALSE?</b>", table_header_style)],
        [Paragraph("<b>Universal Quantifier</b>", table_cell_bold), Paragraph("<b>∀x P(x)</b>", table_cell_center), Paragraph("For all x, P(x)<br/>For every x in U...", table_cell_style), Paragraph("<i>P(x)</i> is True for <b>EVERY</b> <i>x ∈ U</i>.", table_cell_style), Paragraph("There exists <b>AT LEAST ONE</b> <i>x</i> where <i>P(x)</i> is False (Counterexample).", table_cell_style)],
        [Paragraph("<b>Existential Quantifier</b>", table_cell_bold), Paragraph("<b>∃x P(x)</b>", table_cell_center), Paragraph("There exists an x...<br/>For at least one x...", table_cell_style), Paragraph("<i>P(x)</i> is True for <b>AT LEAST ONE</b> <i>x ∈ U</i>.", table_cell_style), Paragraph("<i>P(x)</i> is False for <b>EVERY SINGLE</b> <i>x ∈ U</i>.", table_cell_style)]
    ]
    t_quant = Table(quant_data, colWidths=[110, 80, 110, 120, 120])
    t_quant.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_quant)
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.3 Negation of Quantified Statements (De Morgan's Laws for Quantifiers)", h2_style))
    story.append(Paragraph(
        "To negate a quantified statement, change the quantifier type and negate the predicate statement:",
        body_style
    ))
    
    neg_quant_box = (
        "1. <b>¬(∀x P(x)) ≡ ∃x ¬P(x)</b> &nbsp;&nbsp;&nbsp;&nbsp; <i>('Not all x satisfy P' is equivalent to 'There exists an x that does NOT satisfy P')</i><br/>"
        "2. <b>¬(∃x P(x)) ≡ ∀x ¬P(x)</b> &nbsp;&nbsp;&nbsp;&nbsp; <i>('There is no x satisfying P' is equivalent to 'Every x fails to satisfy P')</i>"
    )
    story.append(make_callout(neg_quant_box, "QUANTIFIER NEGATION RULES"))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Worked Example:</b> Negate the statement: <i>'Every computer science student loves Discrete Mathematics.'</i>", body_bold))
    story.append(Paragraph(
        "• Let <i>C(x)</i>: 'x is a CS student', <i>M(x)</i>: 'x loves Discrete Mathematics'.<br/>"
        "• Symbolic Form: <b>∀x (C(x) → M(x))</b><br/>"
        "• Negation: <i>¬[∀x (C(x) → M(x))] ≡ ∃x ¬(C(x) → M(x)) ≡ <b>∃x (C(x) ∧ ¬M(x))</b></i><br/>"
        "• English Translation: <i><b>'There exists a computer science student who does NOT love Discrete Mathematics.'</b></i>",
        body_style
    ))
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 5: RULES OF INFERENCE & NATURAL DEDUCTION
    # ---------------------------------------------------------
    story.append(Paragraph("5. Rules of Inference & Natural Deduction", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("5.1 Logical Arguments & Validity (M1.05)", h2_style))
    story.append(Paragraph(
        "An <b>argument</b> in propositional logic is a sequence of propositions ending with a conclusion. The initial propositions are called <b>premises</b> (<i>P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>k</sub></i>) and the final proposition is the <b>conclusion (C)</b>.<br/>"
        "<b>Definition of Valid Argument:</b> An argument form with premises <i>P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>k</sub></i> and conclusion <i>C</i> is <b>VALID</b> if and only if the conditional statement <b>(P<sub>1</sub> ∧ P<sub>2</sub> ∧ ... ∧ P<sub>k</sub>) → C</b> is a <b>Tautology</b>.",
        body_style
    ))

    story.append(Paragraph("5.2 Rules of Inference for Propositional Logic", h2_style))
    story.append(Paragraph(
        "Rules of inference are standard valid argument forms used as building blocks in natural deduction proofs:",
        body_style
    ))

    # Rules of Inference Table
    roi_data = [
        [Paragraph("<b>Rule of Inference</b>", table_header_style), Paragraph("<b>Premises</b>", table_header_style), Paragraph("<b>Conclusion</b>", table_header_style), Paragraph("<b>Name / Tautology Form</b>", table_header_style)],
        [Paragraph("<b>Modus Ponens</b> (Mode of Affirming)", table_cell_bold), Paragraph("p<br/>p → q", table_cell_center), Paragraph("<b>∴ q</b>", table_cell_center), Paragraph("[p ∧ (p → q)] → q", table_cell_style)],
        [Paragraph("<b>Modus Tollens</b> (Mode of Denying)", table_cell_bold), Paragraph("¬q<br/>p → q", table_cell_center), Paragraph("<b>∴ ¬p</b>", table_cell_center), Paragraph("[¬q ∧ (p → q)] → ¬p", table_cell_style)],
        [Paragraph("<b>Hypothetical Syllogism</b>", table_cell_bold), Paragraph("p → q<br/>q → r", table_cell_center), Paragraph("<b>∴ p → r</b>", table_cell_center), Paragraph("[(p → q) ∧ (q → r)] → (p → r)", table_cell_style)],
        [Paragraph("<b>Disjunctive Syllogism</b>", table_cell_bold), Paragraph("p ∨ q<br/>¬p", table_cell_center), Paragraph("<b>∴ q</b>", table_cell_center), Paragraph("[(p ∨ q) ∧ ¬p] → q", table_cell_style)],
        [Paragraph("<b>Addition</b>", table_cell_bold), Paragraph("p", table_cell_center), Paragraph("<b>∴ p ∨ q</b>", table_cell_center), Paragraph("p → (p ∨ q)", table_cell_style)],
        [Paragraph("<b>Simplification</b>", table_cell_bold), Paragraph("p ∧ q", table_cell_center), Paragraph("<b>∴ p</b>", table_cell_center), Paragraph("(p ∧ q) → p", table_cell_style)],
        [Paragraph("<b>Conjunction</b>", table_cell_bold), Paragraph("p<br/>q", table_cell_center), Paragraph("<b>∴ p ∧ q</b>", table_cell_center), Paragraph("[(p) ∧ (q)] → (p ∧ q)", table_cell_style)],
        [Paragraph("<b>Resolution</b>", table_cell_bold), Paragraph("p ∨ q<br/>¬p ∨ r", table_cell_center), Paragraph("<b>∴ q ∨ r</b>", table_cell_center), Paragraph("[(p ∨ q) ∧ (¬p ∨ r)] → (q ∨ r)", table_cell_style)]
    ]
    t_roi = Table(roi_data, colWidths=[140, 80, 70, 250])
    t_roi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_roi)
    story.append(Spacer(1, 10))

    story.append(Paragraph("5.3 Rules of Inference for Quantified Statements", h2_style))
    
    # Quantified ROI Table
    qroi_data = [
        [Paragraph("<b>Rule Name</b>", table_header_style), Paragraph("<b>Premise</b>", table_header_style), Paragraph("<b>Conclusion</b>", table_header_style), Paragraph("<b>Condition / Restriction</b>", table_header_style)],
        [Paragraph("<b>Universal Instantiation (UI)</b>", table_cell_bold), Paragraph("∀x P(x)", table_cell_center), Paragraph("<b>∴ P(c)</b>", table_cell_center), Paragraph("<i>c</i> is ANY element in the domain <i>U</i>.", table_cell_style)],
        [Paragraph("<b>Universal Generalization (UG)</b>", table_cell_bold), Paragraph("P(c) for arbitrary c", table_cell_center), Paragraph("<b>∴ ∀x P(x)</b>", table_cell_center), Paragraph("<i>c</i> MUST be an <b>arbitrary</b> (not specific) element.", table_cell_style)],
        [Paragraph("<b>Existential Instantiation (EI)</b>", table_cell_bold), Paragraph("∃x P(x)", table_cell_center), Paragraph("<b>∴ P(c)</b>", table_cell_center), Paragraph("<i>c</i> is a <b>SOME specific</b> element (must be new!).", table_cell_style)],
        [Paragraph("<b>Existential Generalization (EG)</b>", table_cell_bold), Paragraph("P(c) for known c", table_cell_center), Paragraph("<b>∴ ∃x P(x)</b>", table_cell_center), Paragraph("Holds if <i>P(c)</i> is true for a known element <i>c</i>.", table_cell_style)]
    ]
    t_qroi = Table(qroi_data, colWidths=[150, 90, 80, 220])
    t_qroi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_qroi)
    story.append(Spacer(1, 10))

    # Two-Column Formal Proof Example
    story.append(Paragraph("<b>Problem 4 (Formal Natural Deduction Proof):</b><br/>"
                           "Given premises: <i>1. p → q</i>, <i>2. q → r</i>, <i>3. ¬r</i>, and <i>4. p ∨ s</i>.<br/>"
                           "Prove the conclusion: <b>s</b>.", body_bold))
    
    proof2_data = [
        [Paragraph("<b>Step</b>", table_header_style), Paragraph("<b>Proposition / Statement</b>", table_header_style), Paragraph("<b>Justification / Rule Used</b>", table_header_style)],
        [Paragraph("1", table_cell_center), Paragraph("p → q", table_cell_style), Paragraph("Premise 1", table_cell_style)],
        [Paragraph("2", table_cell_center), Paragraph("q → r", table_cell_style), Paragraph("Premise 2", table_cell_style)],
        [Paragraph("3", table_cell_center), Paragraph("p → r", table_cell_style), Paragraph("<b>Hypothetical Syllogism</b> on Steps 1 and 2", table_cell_style)],
        [Paragraph("4", table_cell_center), Paragraph("¬r", table_cell_style), Paragraph("Premise 3", table_cell_style)],
        [Paragraph("5", table_cell_center), Paragraph("¬p", table_cell_style), Paragraph("<b>Modus Tollens</b> on Steps 3 and 4", table_cell_style)],
        [Paragraph("6", table_cell_center), Paragraph("p ∨ s", table_cell_style), Paragraph("Premise 4", table_cell_style)],
        [Paragraph("7", table_cell_center), Paragraph("<b>s</b>", table_cell_bold), Paragraph("<b>Disjunctive Syllogism</b> on Steps 5 and 6 (Conclusion Proven!)", table_cell_style)]
    ]
    t_proof2 = Table(proof2_data, colWidths=[50, 160, 330])
    t_proof2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_proof2)
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 6: PROOF METHODS & RESOLUTION PRINCIPLE
    # ---------------------------------------------------------
    story.append(Paragraph("6. Methods of Proof & Resolution Principle", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("6.1 Standard Methods of Proof (M1.05)", h2_style))
    story.append(Paragraph(
        "Direct and indirect proof strategies for proving mathematical theorems of form <i>p → q</i>:",
        body_style
    ))

    # Proof methods summary table
    pm_data = [
        [Paragraph("<b>Proof Method</b>", table_header_style), Paragraph("<b>Assumption Made</b>", table_header_style), Paragraph("<b>Goal to Demonstrate</b>", table_header_style), Paragraph("<b>Key Strategy / Logic</b>", table_header_style)],
        [Paragraph("<b>Direct Proof</b>", table_cell_bold), Paragraph("Assume <i>p</i> is True", table_cell_style), Paragraph("Show <i>q</i> is True", table_cell_style), Paragraph("Use axioms, definitions, and logic directly.", table_cell_style)],
        [Paragraph("<b>Proof by Contraposition</b>", table_cell_bold), Paragraph("Assume <i>¬q</i> is True", table_cell_style), Paragraph("Show <i>¬p</i> is True", table_cell_style), Paragraph("Uses logical equivalence <i>(p → q) ≡ (¬q → ¬p)</i>.", table_cell_style)],
        [Paragraph("<b>Proof by Contradiction</b> (Reductio ad Absurdum)", table_cell_bold), Paragraph("Assume <i>¬p</i> (or <i>p ∧ ¬q</i>)", table_cell_style), Paragraph("Derive a contradiction <i>r ∧ ¬r</i> (F)", table_cell_style), Paragraph("If assumption leads to nonsense, original statement must be True!", table_cell_style)],
        [Paragraph("<b>Proof by Cases</b>", table_cell_bold), Paragraph("Assume <i>p = p<sub>1</sub> ∨ p<sub>2</sub> ∨ ... ∨ p<sub>k</sub></i>", table_cell_style), Paragraph("Show <i>p<sub>i</sub> → q</i> for all <i>i</i>", table_cell_style), Paragraph("Exhaustive evaluation of all distinct scenarios.", table_cell_style)]
    ]
    t_pm = Table(pm_data, colWidths=[120, 110, 130, 180])
    t_pm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pm)
    story.append(Spacer(1, 8))

    # Classical Proof Example: Proof by Contradiction
    story.append(Paragraph("<b>Classic Exam Proof (Proof by Contradiction):</b> Prove that √2 is an Irrational Number.", body_bold))
    sqrt2_text = (
        "<b>Proof:</b><br/>"
        "1. Assume for contradiction that <b>√2 is rational</b>. Then √2 can be written as a fraction <i>a / b</i> in lowest terms, where <i>a</i> and <i>b</i> are integers with <b>gcd(a, b) = 1</b>.<br/>"
        "2. Squaring both sides: <i>2 = a<sup>2</sup> / b<sup>2</sup>  ⇒  <b>a<sup>2</sup> = 2b<sup>2</sup></b></i>.<br/>"
        "3. Since <i>a<sup>2</sup></i> is a multiple of 2, <i>a<sup>2</sup></i> is EVEN, which implies <b><i>a</i> is EVEN</b>. Let <i>a = 2k</i>.<br/>"
        "4. Substitute <i>a = 2k</i> into equation: <i>(2k)<sup>2</sup> = 2b<sup>2</sup>  ⇒  4k<sup>2</sup> = 2b<sup>2</sup>  ⇒  <b>b<sup>2</sup> = 2k<sup>2</sup></b></i>.<br/>"
        "5. This implies <i>b<sup>2</sup></i> is EVEN, so <b><i>b</i> is also EVEN</b>.<br/>"
        "6. If both <i>a</i> and <i>b</i> are even, they share a common factor of 2, contradicting our assumption that <i>gcd(a, b) = 1</i>!<br/>"
        "7. ∴ Our initial assumption that √2 is rational is FALSE. Thus, <b>√2 is IRRATIONAL</b>. <b>Q.E.D.</b>"
    )
    story.append(Paragraph(sqrt2_text, code_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("6.2 Resolution Principle & Resolution Refutation", h2_style))
    story.append(Paragraph(
        "The <b>Resolution Principle</b> (introduced by J.A. Robinson) is an algorithmic inference rule widely used in automated theorem proving and AI logic programming (e.g., Prolog).<br/>"
        "• <b>Clause:</b> A disjunction (OR) of literals, e.g., <i>C<sub>1</sub> = p ∨ ¬q ∨ r</i>.<br/>"
        "• <b>Resolution Rule:</b> Given two clauses containing complementary literals (<i>p</i> and <i>¬p</i>):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Clause 1: <b>p ∨ C</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Clause 2: <b>¬p ∨ D</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>∴ Resolvent: C ∨ D</b><br/>"
        "• <b>Resolution Refutation Proof Procedure (Proof by Contradiction):</b><br/>"
        "&nbsp;&nbsp; 1. Convert all premises into Clause Form (CNF disjunctions).<br/>"
        "&nbsp;&nbsp; 2. Negate the conclusion to be proven and convert it into clause form.<br/>"
        "&nbsp;&nbsp; 3. Add the negated conclusion clause to the set of premise clauses.<br/>"
        "&nbsp;&nbsp; 4. Iteratively apply the resolution rule to pairs of clauses to generate new resolvent clauses.<br/>"
        "&nbsp;&nbsp; 5. If the <b>Empty Clause (□ or FALSE)</b> is derived, a contradiction is established, proving the original conclusion VALID!",
        body_style
    ))
    story.append(Spacer(1, 8))

    # Resolution Worked Example
    story.append(Paragraph("<b>Problem 5 (Resolution Refutation Proof):</b><br/>"
                           "Use the Resolution Principle to prove that the premises <i>p → q</i> and <i>p</i> entail conclusion <i>q</i>.", body_bold))
    res_text = (
        "<b>Step 1: Convert Premises to Clause Form:</b><br/>"
        "• Premise 1: <i>p → q  ≡  <b>¬p ∨ q</b></i>  ⇒  <b>Clause 1: (¬p ∨ q)</b><br/>"
        "• Premise 2: <i>p</i>  ⇒  <b>Clause 2: (p)</b><br/><br/>"
        "<b>Step 2: Negate the Conclusion:</b><br/>"
        "• Conclusion to prove: <i>q</i>  ⇒  Negated Conclusion: <b>Clause 3: (¬q)</b><br/><br/>"
        "<b>Step 3: Perform Resolution Steps:</b><br/>"
        "• Resolve Clause 1 <i>(¬p ∨ q)</i> and Clause 2 <i>(p)</i> on literal <i>p</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; <b>Clause 4 (Resolvent): (q)</b><br/>"
        "• Resolve Clause 4 <i>(q)</i> and Clause 3 <i>(¬q)</i> on literal <i>q</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; <b>Clause 5 (Resolvent): □ (EMPTY CLAUSE / CONTRADICTION)</b><br/><br/>"
        "<b>Conclusion:</b> Since the empty clause □ was derived, the argument is <b>VALID</b>! <b>Q.E.D.</b>"
    )
    story.append(Paragraph(res_text, code_style))
    story.append(Spacer(1, 14))

    # ---------------------------------------------------------
    # SECTION 7: REVISION & SOLVED EXAMINATION PROBLEMS
    # ---------------------------------------------------------
    story.append(Paragraph("7. Senior Lecturer's Exam Revision & Problem Kit", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    story.append(Paragraph("7.1 Selected Polytechnic Model Question Set", h2_style))

    # Question 1
    story.append(Paragraph("<b>Q1 (5 Marks):</b> Construct the truth table for <i>(p ↔ q) ⊕ (p ∨ q)</i> and state whether it is a tautology, contradiction, or contingency.", body_bold))
    q1_table = [
        [Paragraph("<b>p</b>", table_header_style), Paragraph("<b>q</b>", table_header_style), Paragraph("<b>p ↔ q</b> (A)", table_header_style), Paragraph("<b>p ∨ q</b> (B)", table_header_style), Paragraph("<b>A ⊕ B</b>", table_header_style)],
        [Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("T", table_cell_center), Paragraph("<b>F</b>", table_cell_center)],
        [Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
        [Paragraph("F", table_cell_center), Paragraph("F", table_cell_center), Paragraph("T", table_cell_center), Paragraph("F", table_cell_center), Paragraph("<b>T</b>", table_cell_center)],
    ]
    t_q1 = Table(q1_table, colWidths=[60, 60, 120, 120, 100])
    t_q1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_q1)
    story.append(Paragraph("<i>Ans: Final column contains both T and F. Therefore, the compound proposition is a <b>CONTINGENCY</b>.</i>", body_style))
    story.append(Spacer(1, 8))

    # Question 2
    story.append(Paragraph("<b>Q2 (5 Marks):</b> Express the statement <i>'For every real number x, if x > 2 then x<sup>2</sup> > 4'</i> in predicate logic and write its contrapositive and negation.", body_bold))
    q2_text = (
        "<b>Solution:</b><br/>"
        "• Let domain <i>U</i> be ℝ (real numbers). Let <i>P(x)</i>: 'x > 2', <i>Q(x)</i>: 'x<sup>2</sup> > 4'.<br/>"
        "• <b>Symbolic Form:</b> <b>∀x (P(x) → Q(x))</b><br/>"
        "• <b>Contrapositive:</b> <b>∀x (¬Q(x) → ¬P(x))</b>  ⇒  <i>'For every real number x, if x<sup>2</sup> ≤ 4 then x ≤ 2.'</i><br/>"
        "• <b>Negation:</b> <b>∃x (P(x) ∧ ¬Q(x))</b>  ⇒  <i>'There exists a real number x such that x > 2 and x<sup>2</sup> ≤ 4.'</i>"
    )
    story.append(Paragraph(q2_text, body_style))
    story.append(Spacer(1, 8))

    # Question 3
    story.append(Paragraph("<b>Q3 (5 Marks):</b> Prove using Duality and De Morgan's laws that <i>¬(p ∧ q) ≡ ¬p ∨ ¬q</i>.", body_bold))
    story.append(Paragraph("<i>Ans: Refer to Section 3.1 & 3.2 for the step-by-step law applications.</i>", body_style))
    story.append(Spacer(1, 10))

    # Quick Summary Box
    summary_box = (
        "<b>POLYTECHNIC LECTURER'S FINAL CHECKLIST FOR MODULE 1 EXAM:</b><br/>"
        "✔ Always state the number of rows (2<sup>n</sup>) when constructing truth tables.<br/>"
        "✔ Remember that <i>p → q</i> is False ONLY when T → F. In all other cases, it is True.<br/>"
        "✔ Contrapositive <i>(¬q → ¬p)</i> is logically equivalent to original implication <i>(p → q)</i>.<br/>"
        "✔ In algebraic proofs, explicitly mention the name of the law used at every single step.<br/>"
        "✔ To negate a quantifier, swap <b>∀ ↔ ∃</b> and negate the inner predicate statement.<br/>"
        "✔ In Resolution Refutation proofs, ALWAYS negate the conclusion first!"
    )
    story.append(make_tip(summary_box, "HIGH-YIELD REVISION SUMMARY"))

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {pdf_path}")

if __name__ == '__main__':
    build_pdf()
