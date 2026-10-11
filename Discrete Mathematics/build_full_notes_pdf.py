import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

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
        
        # Running Header (Pages 2+)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A"))
            self.drawString(36, 762, "DISCRETE MATHEMATICS (3341) — MODULE 1: MATHEMATICAL LOGIC")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawRightString(576, 762, "Diploma in AI & ML | Complete Notes & PYQ Bank")
            
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 754, 576, 754)

        # Running Footer (All pages)
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1E3A8A"))
        self.drawString(36, 25, "STATE BOARD OF TECHNICAL EDUCATION, KERALA")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(280, 25, "Strictly Prescribed Textbooks (Rosen, Grimaldi, Koshy)")
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#1E3A8A"))
        self.drawRightString(576, 25, page_str)
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 36, 576, 36)
        
        self.restoreState()

def build_pdf():
    notes_dir = os.path.join(os.getcwd(), "Notes")
    os.makedirs(notes_dir, exist_ok=True)
    pdf_path = os.path.join(notes_dir, "Module_1_Discrete_Mathematics_Full_Notes.pdf")

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    # Color Palette
    C_PRIMARY = colors.HexColor("#1E3A8A")
    C_SECONDARY = colors.HexColor("#0D9488")
    C_TEXT = colors.HexColor("#0F172A")
    C_BG_BOX = colors.HexColor("#F0F9FF")
    C_BG_TIP = colors.HexColor("#FEF3C7")
    C_BG_PYQ = colors.HexColor("#FAF5FF")
    C_BORDER_BOX = colors.HexColor("#BAE6FD")
    C_BORDER_TIP = colors.HexColor("#FDE68A")
    C_BORDER_PYQ = colors.HexColor("#E9D5FF")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=C_PRIMARY,
        alignment=1,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=C_SECONDARY,
        alignment=1,
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'H1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=C_PRIMARY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=C_SECONDARY,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=C_TEXT,
        spaceAfter=5
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
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#7F1D1D"),
        backColor=colors.HexColor("#F8FAFC"),
        borderColor=colors.HexColor("#E2E8F0"),
        borderWidth=0.5,
        borderPadding=4,
        spaceAfter=5
    )

    callout_text = ParagraphStyle('CText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#0369A1"))
    tip_text = ParagraphStyle('TText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#92400E"))
    pyq_text = ParagraphStyle('PText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#6B21A8"))

    table_header_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.white, alignment=1)
    table_cell_style = ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=C_TEXT)
    table_cell_center = ParagraphStyle('TCC', parent=table_cell_style, alignment=1)
    table_cell_bold = ParagraphStyle('TCB', parent=table_cell_style, fontName='Helvetica-Bold')

    story = []

    def make_box(text, title="DEFINITION / CONCEPT", bg=C_BG_BOX, border=C_BORDER_BOX, txt_style=callout_text, title_clr="#075985"):
        p_title = Paragraph(f"<b>{title}</b>", ParagraphStyle('BTitle', parent=txt_style, fontName='Helvetica-Bold', fontSize=9, spaceAfter=2, textColor=colors.HexColor(title_clr)))
        p_body = Paragraph(text, txt_style)
        t = Table([[ [p_title, p_body] ]], colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg),
            ('BOX', (0,0), (-1,-1), 1, border),
            ('PADDING', (0,0), (-1,-1), 7),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return t

    # ---------------------------------------------------------
    # COVER / HEADER BANNER
    # ---------------------------------------------------------
    header_data = [
        [Paragraph("<b>STATE BOARD OF TECHNICAL EDUCATION, KERALA — DIPLOMA NOTES</b>", ParagraphStyle('H1', parent=table_header_style, fontSize=9.5, leading=12))],
        [Paragraph("<b>COURSE: DISCRETE MATHEMATICS (COURSE CODE: 3341)</b>", ParagraphStyle('H2', parent=table_header_style, fontSize=13, leading=16))],
        [Paragraph("SEMESTER III | DIPLOMA IN ARTIFICIAL INTELLIGENCE & MACHINE LEARNING", ParagraphStyle('H3', parent=table_header_style, fontSize=9, leading=11))]
    ]
    header_table = Table(header_data, colWidths=[540])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("MODULE 1: MATHEMATICAL LOGIC", title_style))
    story.append(Paragraph("Full Lecture Notes & Solved Previous Year University Exam Questions (PYQ Bank)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=1, spaceAfter=8))

    # Meta Info Card
    meta_text = (
        "<b>Course Outcome CO1:</b> Apply the basic concepts of mathematical logic to solve computational problems.<br/>"
        "<b>Duration:</b> 16 Hours | <b>Cognitive Level:</b> Applying<br/>"
        "<b>Prescribed Textbooks:</b> (1) Kenneth H. Rosen (7th Ed), (2) Ralph P. Grimaldi (5th Ed), (3) Thomas Koshy (2nd Ed).<br/>"
        "<b>Exam Alignment:</b> Includes exact solved 1-mark, 3-mark, and 7-mark PYQs from State Board Exams (Nov 2024 & Nov 2025)."
    )
    story.append(make_box(meta_text, "COURSE SYLLABUS & EXAM ALIGNMENT", C_BG_BOX, C_BORDER_BOX, callout_text, "#075985"))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 1: PROPOSITIONAL LOGIC
    # ---------------------------------------------------------
    story.append(Paragraph("1. Propositional Logic & Logical Operations (M1.01, M1.02)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))

    story.append(Paragraph("1.1 Definition & Classification of Propositions", h2_style))
    story.append(Paragraph(
        "<b>Definition (Proposition / Statement):</b> A declarative sentence that is either <b>True (T)</b> or <b>False (F)</b>, but not both.<br/>"
        "• <b>Atomic Proposition:</b> Simple statement that cannot be broken down (e.g., <i>p: '2 + 3 = 5'</i>).<br/>"
        "• <b>Compound Proposition:</b> Formed by combining propositions using <b>logical connectives</b>.",
        body_style
    ))

    # Connectives Table
    conn_data = [
        [Paragraph("<b>Connective</b>", table_header_style), Paragraph("<b>Symbol</b>", table_header_style), Paragraph("<b>Logical Name</b>", table_header_style), Paragraph("<b>Meaning / Truth Condition</b>", table_header_style)],
        [Paragraph("NOT", table_cell_center), Paragraph("¬ (or ~)", table_cell_center), Paragraph("Negation", table_cell_style), Paragraph("Reverses truth value. True when proposition is false.", table_cell_style)],
        [Paragraph("AND", table_cell_center), Paragraph("∧", table_cell_center), Paragraph("Conjunction", table_cell_style), Paragraph("True <b>ONLY when BOTH</b> <i>p</i> and <i>q</i> are True.", table_cell_style)],
        [Paragraph("OR", table_cell_center), Paragraph("∨", table_cell_center), Paragraph("Disjunction", table_cell_style), Paragraph("True when <b>AT LEAST ONE</b> of <i>p, q</i> is True.", table_cell_style)],
        [Paragraph("XOR", table_cell_center), Paragraph("⊕", table_cell_center), Paragraph("Exclusive-OR", table_cell_style), Paragraph("True when <b>EXACTLY ONE</b> of <i>p, q</i> is True.", table_cell_style)],
        [Paragraph("IF...THEN", table_cell_center), Paragraph("→", table_cell_center), Paragraph("Implication", table_cell_style), Paragraph("False <b>ONLY when</b> <i>p</i> is True and <i>q</i> is False.", table_cell_style)],
        [Paragraph("IFF", table_cell_center), Paragraph("↔", table_cell_center), Paragraph("Biconditional", table_cell_style), Paragraph("True when <i>p</i> and <i>q</i> have the <b>SAME</b> truth value.", table_cell_style)]
    ]
    t_conn = Table(conn_data, colWidths=[65, 65, 120, 290])
    t_conn.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_conn)
    story.append(Spacer(1, 6))

    # Master Truth Table
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
        ('PADDING', (0,0), (-1,-1), 4.5),
    ]))
    story.append(t_master)
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 2: IMPLICATION & TRUTH CLASSIFICATIONS
    # ---------------------------------------------------------
    story.append(Paragraph("2. Conditional Statements & Truth Classifications (M1.02, M1.03)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))

    story.append(Paragraph("2.1 Variants of Implication", h2_style))
    story.append(Paragraph(
        "For an implication statement <b>p → q</b>:<br/>"
        "• <b>Converse:</b> <i>q → p</i> &nbsp;&nbsp;&nbsp;&nbsp; • <b>Inverse:</b> <i>¬p → ¬q</i> &nbsp;&nbsp;&nbsp;&nbsp; • <b>Contrapositive:</b> <i>¬q → ¬p</i><br/>"
        "<b>CRITICAL FACT:</b> <i>p → q</i> is <b>STRICTLY LOGICALLY EQUIVALENT</b> to its Contrapositive <i>(¬q → ¬p)</i>!",
        body_style
    ))

    story.append(Paragraph("2.2 Truth Classifications & Normal Forms", h2_style))
    story.append(Paragraph(
        "• <b>Tautology (T):</b> Always True under all interpretations (e.g., <i>p ∨ ¬p</i>).<br/>"
        "• <b>Contradiction (F):</b> Always False under all interpretations (e.g., <i>p ∧ ¬p</i>).<br/>"
        "• <b>Contingency:</b> Neither a tautology nor a contradiction (e.g., <i>p → q</i>).<br/>"
        "• <b>Disjunctive Normal Form (DNF):</b> Disjunction (OR) of minterms (ANDs of literals).<br/>"
        "• <b>Conjunctive Normal Form (CNF):</b> Conjunction (AND) of maxterms (ORs of literals).",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 3: LOGICAL EQUIVALENCE & DUALITY
    # ---------------------------------------------------------
    story.append(Paragraph("3. Logical Equivalence & Duality Principle (M1.03)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))

    laws_data = [
        [Paragraph("<b>Law Category</b>", table_header_style), Paragraph("<b>Equivalence Statement 1</b>", table_header_style), Paragraph("<b>Equivalence Statement 2 (Dual Form)</b>", table_header_style)],
        [Paragraph("<b>Identity Laws</b>", table_cell_bold), Paragraph("p ∧ T ≡ p", table_cell_style), Paragraph("p ∨ F ≡ p", table_cell_style)],
        [Paragraph("<b>Domination Laws</b>", table_cell_bold), Paragraph("p ∨ T ≡ T", table_cell_style), Paragraph("p ∧ F ≡ F", table_cell_style)],
        [Paragraph("<b>Idempotent Laws</b>", table_cell_bold), Paragraph("p ∨ p ≡ p", table_cell_style), Paragraph("p ∧ p ≡ p", table_cell_style)],
        [Paragraph("<b>Double Negation Law</b>", table_cell_bold), Paragraph("¬(¬p) ≡ p", table_cell_style), Paragraph("—", table_cell_center)],
        [Paragraph("<b>Commutative Laws</b>", table_cell_bold), Paragraph("p ∨ q ≡ q ∨ p", table_cell_style), Paragraph("p ∧ q ≡ q ∧ p", table_cell_style)],
        [Paragraph("<b>Associative Laws</b>", table_cell_bold), Paragraph("(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)", table_cell_style), Paragraph("(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)", table_cell_style)],
        [Paragraph("<b>Distributive Laws</b>", table_cell_bold), Paragraph("p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)", table_cell_style), Paragraph("p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)", table_cell_style)],
        [Paragraph("<b>De Morgan's Laws</b>", table_cell_bold), Paragraph("<b>¬(p ∧ q) ≡ ¬p ∨ ¬q</b>", table_cell_style), Paragraph("<b>¬(p ∨ q) ≡ ¬p ∧ ¬q</b>", table_cell_style)],
        [Paragraph("<b>Absorption Laws</b>", table_cell_bold), Paragraph("p ∨ (p ∧ q) ≡ p", table_cell_style), Paragraph("p ∧ (p ∨ q) ≡ p", table_cell_style)],
        [Paragraph("<b>Negation Laws</b>", table_cell_bold), Paragraph("p ∨ ¬p ≡ T", table_cell_style), Paragraph("p ∧ ¬p ≡ F", table_cell_style)],
        [Paragraph("<b>Conditional Equivalences</b>", table_cell_bold), Paragraph("<b>p → q ≡ ¬p ∨ q</b>", table_cell_style), Paragraph("<b>p ↔ q ≡ (p → q) ∧ (q → p)</b>", table_cell_style)]
    ]
    t_laws = Table(laws_data, colWidths=[130, 205, 205])
    t_laws.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_laws)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Duality Principle:</b> Dual <b>s*</b> of a proposition <i>s</i> is formed by swapping <b>∧ ↔ ∨</b> and <b>T ↔ F</b> (negations remain unchanged!). If <i>s ≡ t</i>, then <b>s* ≡ t*</b>.", body_style))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 4: PREDICATE LOGIC & QUANTIFIERS
    # ---------------------------------------------------------
    story.append(Paragraph("4. Predicate Logic & Quantifiers (M1.04)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))

    story.append(Paragraph(
        "• <b>Predicate P(x):</b> Statement with variable <i>x</i> over domain <i>U</i>.<br/>"
        "• <b>Universal Quantifier (∀x P(x)):</b> True if <i>P(x)</i> holds for <b>EVERY</b> <i>x ∈ U</i>.<br/>"
        "• <b>Existential Quantifier (∃x P(x)):</b> True if <i>P(x)</i> holds for <b>AT LEAST ONE</b> <i>x ∈ U</i>.<br/>"
        "• <b>De Morgan's Laws for Quantifiers:</b> <b>¬(∀x P(x)) ≡ ∃x ¬P(x)</b> &nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp; <b>¬(∃x P(x)) ≡ ∀x ¬P(x)</b>.<br/>"
        "• <b>Nested Quantifiers Order Rule:</b> <b>∀x ∃y P(x, y)  ≢  ∃y ∀x P(x, y)</b> (Order matters!).",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 5: RULES OF INFERENCE
    # ---------------------------------------------------------
    story.append(Paragraph("5. Rules of Inference & Natural Deduction (M1.05)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))

    roi_data = [
        [Paragraph("<b>Rule Name</b>", table_header_style), Paragraph("<b>Premises</b>", table_header_style), Paragraph("<b>Conclusion</b>", table_header_style), Paragraph("<b>Tautology Form</b>", table_header_style)],
        [Paragraph("<b>Modus Ponens</b>", table_cell_bold), Paragraph("p<br/>p → q", table_cell_center), Paragraph("<b>∴ q</b>", table_cell_center), Paragraph("[p ∧ (p → q)] → q", table_cell_style)],
        [Paragraph("<b>Modus Tollens</b>", table_cell_bold), Paragraph("¬q<br/>p → q", table_cell_center), Paragraph("<b>∴ ¬p</b>", table_cell_center), Paragraph("[¬q ∧ (p → q)] → ¬p", table_cell_style)],
        [Paragraph("<b>Hypothetical Syllogism</b>", table_cell_bold), Paragraph("p → q<br/>q → r", table_cell_center), Paragraph("<b>∴ p → r</b>", table_cell_center), Paragraph("[(p → q) ∧ (q → r)] → (p → r)", table_cell_style)],
        [Paragraph("<b>Disjunctive Syllogism</b>", table_cell_bold), Paragraph("p ∨ q<br/>¬p", table_cell_center), Paragraph("<b>∴ q</b>", table_cell_center), Paragraph("[(p ∨ q) ∧ ¬p] → q", table_cell_style)],
        [Paragraph("<b>Addition</b>", table_cell_bold), Paragraph("p", table_cell_center), Paragraph("<b>∴ p ∨ q</b>", table_cell_center), Paragraph("p → (p ∨ q)", table_cell_style)],
        [Paragraph("<b>Simplification</b>", table_cell_bold), Paragraph("p ∧ q", table_cell_center), Paragraph("<b>∴ p</b>", table_cell_center), Paragraph("(p ∧ q) → p", table_cell_style)],
        [Paragraph("<b>Conjunction</b>", table_cell_bold), Paragraph("p<br/>q", table_cell_center), Paragraph("<b>∴ p ∧ q</b>", table_cell_center), Paragraph("[(p) ∧ (q)] → (p ∧ q)", table_cell_style)],
        [Paragraph("<b>Resolution</b>", table_cell_bold), Paragraph("p ∨ q<br/>¬p ∨ r", table_cell_center), Paragraph("<b>∴ q ∨ r</b>", table_cell_center), Paragraph("[(p ∨ q) ∧ (¬p ∨ r)] → (q ∨ r)", table_cell_style)]
    ]
    t_roi = Table(roi_data, colWidths=[130, 80, 70, 260])
    t_roi.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_roi)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Quantified Inference Rules:</b> UI (<i>∀x P(x) ∴ P(c)</i> for any <i>c</i>), UG (<i>P(c) ∴ ∀x P(x)</i> for arbitrary <i>c</i>), EI (<i>∃x P(x) ∴ P(c)</i> for new specific <i>c</i>), EG (<i>P(c) ∴ ∃x P(x)</i> for known <i>c</i>).", body_style))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 6: PROOF METHODS & RESOLUTION
    # ---------------------------------------------------------
    story.append(Paragraph("6. Methods of Proof & Resolution Principle (M1.05)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))
    story.append(Paragraph(
        "• <b>Direct Proof:</b> Assume <i>p</i>, show <i>q</i> directly.<br/>"
        "• <b>Proof by Contraposition:</b> Assume <i>¬q</i>, show <i>¬p</i>.<br/>"
        "• <b>Proof by Contradiction:</b> Assume <i>¬p</i>, derive contradiction <i>r ∧ ¬r (F)</i> (e.g., proof that √2 is irrational).<br/>"
        "• <b>Resolution Refutation Algorithm:</b> Convert premises to clause form (disjunctions), negate the conclusion, and apply resolvent rule <i>(A ∨ C) ∧ (¬A ∨ B) ⇒ (B ∨ C)</i> repeatedly until the <b>Empty Clause (□)</b> is derived.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ---------------------------------------------------------
    # SECTION 7: SOLVED PYQ BANK
    # ---------------------------------------------------------
    story.append(Paragraph("7. State Board Solved University Exam PYQ Bank (Revision 2021)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    # Part A Questions
    pyq_a = (
        "<b>PART-A: 1-MARK OBJECTIVE PYQS (WITH STEP-BY-STEP SOLUTIONS)</b><br/><br/>"
        "<b>Q1 [Nov 2025]:</b> Interpret the logical equivalence to the statement: <i>'I pass only if you pass'</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Let <i>p</i>: 'I pass', <i>q</i>: 'You pass'. 'p only if q' ≡ <b>p → q ≡ ¬p ∨ q ≡ ¬q → ¬p</b> (Contrapositive).<br/><br/>"
        "<b>Q2 [Nov 2025]:</b> Write the dual for <i>(p ∧ q) ∨ T</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Swap ∧ ↔ ∨ and T ↔ F. Dual = <b>(p ∨ q) ∧ F</b>.<br/><br/>"
        "<b>Q3 [Nov 2024]:</b> If <i>p</i> is a proposition, ¬(¬p) = ......?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> By Double Negation Law, ¬(¬p) = <b>p</b>.<br/><br/>"
        "<b>Q4 [Nov 2024]:</b> If <i>A</i> has <i>n</i> elements, then number of subsets of <i>A</i> = ......?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Number of subsets = |P(A)| = <b>2<sup>n</sup></b>."
    )
    story.append(make_box(pyq_a, "PART-A: 1-MARK SOLVED EXAM QUESTIONS", C_BG_PYQ, C_BORDER_PYQ, pyq_text, "#6B21A8"))
    story.append(Spacer(1, 8))

    # Part B Questions
    pyq_b = (
        "<b>PART-B: 3-MARK SHORT ANSWER PYQS (WITH STEP-BY-STEP SOLUTIONS)</b><br/><br/>"
        "<b>Q1 [Nov 2025]:</b> Show that the implication <i>[(p → q) ∧ (q → r)] → (p → r)</i> is a tautology.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Constructing 8-row truth table for <i>A = (p → q) ∧ (q → r)</i> and <i>B = (p → r)</i> shows all entries in <i>A → B</i> are <b>T</b>. Hence, it is a Tautology.<br/><br/>"
        "<b>Q2 [Nov 2025]:</b> Without constructing a truth table, prove that <i>¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬q</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> <i>¬(p ∨ (¬p ∧ q)) ≡ ¬p ∧ ¬(¬p ∧ q)</i> [De Morgan] <i>≡ ¬p ∧ (p ∨ ¬q)</i> [Double Negation] <i>≡ (¬p ∧ p) ∨ (¬p ∧ ¬q)</i> [Distributive] <i>≡ F ∨ (¬p ∧ ¬q)</i> [Negation] <i>≡ ¬p ∧ ¬q</i> [Identity]. <b>Q.E.D.</b><br/><br/>"
        "<b>Q3 [Nov 2024]:</b> Determine the truth value / truth table of conjunction table <i>(p ∧ q)</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> <i>p ∧ q</i> is True ONLY when both <i>p = T</i> and <i>q = T</i>. Rows: (T,T)→T, (T,F)→F, (F,T)→F, (F,F)→F."
    )
    story.append(make_box(pyq_b, "PART-B: 3-MARK SOLVED EXAM QUESTIONS", C_BG_PYQ, C_BORDER_PYQ, pyq_text, "#6B21A8"))
    story.append(Spacer(1, 8))

    # Part C Questions
    pyq_c = (
        "<b>PART-C: 7-MARK LONG ANSWER PYQS (WITH STEP-BY-STEP SOLUTIONS)</b><br/><br/>"
        "<b>Q1 [Nov 2025]:</b> Construct the truth table for <i>(p ∨ q) ∧ (¬p → ¬q)</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Row 1 (T,T): T ∧ T = <b>T</b>; Row 2 (T,F): T ∧ T = <b>T</b>; Row 3 (F,T): T ∧ F = <b>F</b>; Row 4 (F,F): F ∧ T = <b>F</b>.<br/><br/>"
        "<b>Q2 [Nov 2025 - OR]:</b> Write converse, inverse, contrapositive for: <i>'If 2 < 3 and 3+7=10, then √4 = 2'</i> and find their truth values.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Let <i>p: (2<3 ∧ 3+7=10)</i> [True], <i>q: √4=2</i> [True].<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Original (p → q):</b> If 2<3 and 3+7=10, then √4=2. Truth Value = <b>T</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Converse (q → p):</b> If √4=2, then 2<3 and 3+7=10. Truth Value = <b>T</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Inverse (¬p → ¬q):</b> If not(2<3 ∧ 3+7=10), then √4 ≠ 2. Truth Value = <b>T</b>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• <b>Contrapositive (¬q → ¬p):</b> If √4 ≠ 2, then not(2<3 ∧ 3+7=10). Truth Value = <b>T</b>.<br/><br/>"
        "<b>Q3 [Nov 2025]:</b> Prove argument validity: Premises: <i>1. p → q</i>, <i>2. q → (r ∧ s)</i>, <i>3. ¬r ∨ (¬t ∨ u)</i>, <i>4. p ∧ t</i>. Conclusion: <i>u</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> From 4: <i>p</i> (Simp) & <i>t</i> (Simp). From 1 & <i>p</i>: <i>q</i> (MP). From 2 & <i>q</i>: <i>r ∧ s</i> (MP) ⇒ <i>r</i> (Simp). From 3 & <i>r</i>: <i>¬t ∨ u</i> (DS). From <i>t</i> & <i>¬t ∨ u</i>: <b>u</b> (DS). <b>Q.E.D.</b><br/><br/>"
        "<b>Q4 [Nov 2024]:</b> Construct truth table for <i>¬(p ∨ q) → ¬p</i>.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Evaluating all 4 rows yields <b>T</b> in every row. Hence it is a <b>Tautology</b>.<br/><br/>"
        "<b>Q5 [Nov 2024 - OR]:</b> Use truth table to show that <i>¬(p → q) → ¬q</i> is a logical implication.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> Evaluating <i>¬(p → q) → ¬q</i> yields <b>T</b> in all 4 rows. Since it is a Tautology, it is a valid <b>logical implication</b>."
    )
    story.append(make_box(pyq_c, "PART-C: 7-MARK SOLVED EXAM QUESTIONS", C_BG_PYQ, C_BORDER_PYQ, pyq_text, "#6B21A8"))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Full Notes PDF successfully generated at: {pdf_path}")

if __name__ == '__main__':
    build_pdf()
