import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

# ------------------------------------------------------------------------------
# 1. GENERATE LATEX FILE FOR MODULE 2
# ------------------------------------------------------------------------------
def create_module2_latex():
    notes_dir = os.path.join(os.getcwd(), "Notes")
    os.makedirs(notes_dir, exist_ok=True)
    tex_path = os.path.join(notes_dir, "Module_2_Discrete_Mathematics.tex")

    latex_content = r"""\documentclass[11pt,a4paper]{article}

% --- Essential Packages ---
\usepackage[utf8]{utf8}
\usepackage[margin=0.75in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs,array,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{titlesec}

% --- Color Definitions ---
\definecolor{primaryblue}{RGB}{30, 58, 138}    % Deep Navy
\definecolor{secondaryteal}{RGB}{13, 148, 136}  % Teal Accent
\definecolor{darkslate}{RGB}{15, 23, 42}       % Body text
\definecolor{boxbg}{RGB}{240, 249, 255}        % Light Blue Box
\definecolor{tipbg}{RGB}{254, 243, 199}        % Light Amber Box
\definecolor{pyqbg}{RGB}{243, 232, 255}        % Light Purple Box

% --- Hyperref Setup ---
\hypersetup{
    colorlinks=true,
    linkcolor=primaryblue,
    citecolor=secondaryteal,
    urlcolor=primaryblue
}

% --- Header and Footer Setup ---
\pagestyle{fancy}
\fancyhf{}
\rhead{\small \textcolor{primaryblue}{\textbf{MODULE 2: SETS, RELATIONS \& FUNCTIONS | DISCRETE MATH (3341)}}}
\lhead{\small \textcolor{gray}{Diploma in AI \& ML — Semester III}}
\rfoot{\small Page \thepage}
\lfoot{\small \textcolor{gray}{State Board of Technical Education, Kerala}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.6pt}

% --- Custom Colored Boxes ---
\newtcolorbox{lecturnote}[1]{
    colback=boxbg,
    colframe=primaryblue,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt
}

\newtcolorbox{examtip}[1]{
    colback=tipbg,
    colframe=orange!85!black,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt
}

\newtcolorbox{pyqbox}[1]{
    colback=pyqbg,
    colframe=purple!75!black,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt
}

% --- Title Formatting ---
\titleformat{\section}{\large\bfseries\color{primaryblue}}{\thesection.}{0.5em}{}[\titlerule]
\titleformat{\subsection}{\bfseries\color{secondaryteal}}{\thesubsection}{0.5em}{}

\begin{document}

% ==============================================================================
% TITLE & HEADER BANNER
% ==============================================================================
\begin{center}
    \tcbset{colback=primaryblue,colframe=primaryblue,arc=0pt,top=10pt,bottom=10pt}
    \begin{tcolorbox}[halign=center]
        \color{white}
        {\large \textbf{STATE BOARD OF TECHNICAL EDUCATION, KERALA}}\\[4pt]
        {\Large \textbf{DIPLOMA EXAMINATION IN ENGINEERING \& TECHNOLOGY}}\\[4pt]
        {\large \textbf{COURSE: DISCRETE MATHEMATICS (COURSE CODE: 3341)}}\\[2pt]
        {\small SEMESTER III --- DIPLOMA IN ARTIFICIAL INTELLIGENCE \& MACHINE LEARNING}
    \end{tcolorbox}
\end{center}

\vspace{10pt}

\begin{center}
    {\huge \textbf{\textcolor{primaryblue}{MODULE 2: SETS, RELATIONS \& FUNCTIONS}}}\\[6pt]
    {\large \textbf{\textcolor{secondaryteal}{Complete Lecture Notes \& Solved University Exam Question (PYQ) Bank}}}\\[4pt]
    \textit{Strictly Prescribed Textbooks: Kenneth H. Rosen (7th Ed), Ralph P. Grimaldi (5th Ed), Thomas Koshy (2nd Ed)}
\end{center}

\vspace{10pt}

\begin{lecturnote}{MODULE OUTCOMES \& SYLLABUS SCOPE (Course Outcome CO2)}
\textbf{Course Outcome CO2:} Demonstrate sets, relations and functions to solve computational problems. (Duration: 16 Hours | Cognitive Level: Applying)\\[4pt]
\textbf{Module Sub-Outcomes:}
\begin{itemize}[leftmargin=1.5em, itemsep=1pt]
    \item \textbf{M2.01:} Outline the basic principles of set. (2 Hours, Understanding)
    \item \textbf{M2.02:} Demonstrate the operations on sets. (2 Hours, Applying)
    \item \textbf{M2.03:} Apply inclusion-exclusion principle. (2 Hours, Applying)
    \item \textbf{M2.04:} Demonstrate the concept of relations. (2 Hours, Understanding)
    \item \textbf{M2.05:} Identify the equivalence relations. (2 Hours, Applying)
    \item \textbf{M2.06:} Illustrate the equivalence classes from equivalence relation. (3 Hours, Applying)
    \item \textbf{M2.07:} Demonstrate the concept of functions. (3 Hours, Applying)
\end{itemize}
\end{lecturnote}

\vspace{10pt}
\tableofcontents
\newpage

% ==============================================================================
% SECTION 1: SET THEORY & ALGEBRA OF SETS
% ==============================================================================
\section{Set Theory \& Algebra of Sets}

\subsection{Basic Definitions \& Set Representation (M2.01)}

\begin{definition}[\textbf{Set}]
A \textbf{set} is an unordered collection of distinct, well-defined objects called \textbf{elements} or \textbf{members} of the set.
\end{definition}

\subsubsection*{Methods of Set Representation}
\begin{enumerate}
    \item \textbf{Roster (Tabular) Form:} Listing all elements explicitly enclosed in curly braces, e.g., $A = \{1, 2, 3, 4, 5\}$.
    \item \textbf{Set-Builder Form:} Stating the characteristic property that all elements must satisfy, e.g., $A = \{x \in \mathbb{Z} \mid 1 \le x \le 5\}$.
\end{enumerate}

\subsubsection*{Standard Number Sets}
\begin{itemize}
    \item $\mathbb{N} = \{1, 2, 3, \dots\}$ --- Natural numbers.
    \item $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$ --- Integers.
    \item $\mathbb{Q} = \{p/q \mid p, q \in \mathbb{Z}, q \ne 0\}$ --- Rational numbers.
    \item $\mathbb{R}$ --- Real numbers.
\end{itemize}

\subsubsection*{Types of Sets}
\begin{itemize}
    \item \textbf{Empty (Null/Void) Set ($\emptyset$ or $\{\}$):} A set containing no elements. $|\emptyset| = 0$.
    \item \textbf{Universal Set ($U$):} The set containing all possible objects under consideration.
    \item \textbf{Finite vs. Infinite Set:} A set is finite if its cardinality $|A| = n$ for some non-negative integer $n$; otherwise, it is infinite.
    \item \textbf{Subset ($A \subseteq B$):} $A$ is a subset of $B$ if every element of $A$ is also an element of $B$. ($\forall x (x \in A \rightarrow x \in B)$).
    \item \textbf{Proper Subset ($A \subset B$):} $A \subseteq B$ and $A \ne B$.
    \item \textbf{Power Set ($P(A)$):} The set of all subsets of $A$. If $|A| = n$, then $|P(A)| = 2^n$.
\end{itemize}

\subsection{Set Operations \& Venn Diagrams (M2.02)}

Let $A$ and $B$ be subsets of a Universal Set $U$:

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|l|p{6.5cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Operation} & \color{white}\textbf{Symbol} & \color{white}\textbf{Set-Builder Definition} & \color{white}\textbf{Meaning in Words} \\ \hline
\textbf{Union} & $A \cup B$ & $\{x \mid x \in A \lor x \in B\}$ & Elements in $A$, or $B$, or both. \\ \hline
\textbf{Intersection} & $A \cap B$ & $\{x \mid x \in A \land x \in B\}$ & Elements common to \textbf{BOTH} $A$ and $B$. \\ \hline
\textbf{Difference} & $A \setminus B$ (or $A - B$) & $\{x \mid x \in A \land x \notin B\}$ & Elements in $A$ that are \textbf{NOT} in $B$. \\ \hline
\textbf{Complement} & $A'$ (or $\overline{A}$) & $\{x \in U \mid x \notin A\} = U \setminus A$ & Elements in $U$ outside of $A$. \\ \hline
\textbf{Symmetric Diff.} & $A \oplus B$ & $(A \setminus B) \cup (B \setminus A)$ & Elements in $A$ or $B$, but \textbf{NOT BOTH}. \\ \hline
\end{tabular}
\caption{Fundamental Operations on Sets}
\end{table}

\subsubsection*{Fundamental Laws of Set Algebra}
Set operations satisfy algebraic laws isomorphic to propositional logic:
\begin{itemize}
    \item \textbf{Identity Laws:} $A \cup \emptyset = A, \quad A \cap U = A$
    \item \textbf{Domination Laws:} $A \cup U = U, \quad A \cap \emptyset = \emptyset$
    \item \textbf{Idempotent Laws:} $A \cup A = A, \quad A \cap A = A$
    \item \textbf{Complementation Law:} $(A')' = A$
    \item \textbf{Commutative Laws:} $A \cup B = B \cup A, \quad A \cap B = B \cap A$
    \item \textbf{Associative Laws:} $(A \cup B) \cup C = A \cup (B \cup C), \quad (A \cap B) \cap C = A \cap (B \cap C)$
    \item \textbf{Distributive Laws:} $A \cup (B \cap C) = (A \cup B) \cap (A \cup C), \quad A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
    \item \textbf{De Morgan's Laws:} $(A \cup B)' = A' \cap B', \quad (A \cap B)' = A' \cup B'$
\end{itemize}

\subsection{Principle of Inclusion-Exclusion (M2.03)}

The \textbf{Inclusion-Exclusion Principle} counts the number of elements in the union of sets without double-counting overlaps:

\begin{theorem}[\textbf{Inclusion-Exclusion for 2 Sets}]
$$|A \cup B| = |A| + |B| - |A \cap B|$$
\end{theorem}

\begin{theorem}[\textbf{Inclusion-Exclusion for 3 Sets}]
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|$$
\end{theorem}

\newpage

% ==============================================================================
% SECTION 2: RELATIONS & EQUIVALENCE CLASSES
% ==============================================================================
\section{Relations \& Equivalence Classes}

\subsection{Cartesian Product \& Definition of Relation (M2.04)}

\begin{definition}[\textbf{Cartesian Product \& Relation}]
The \textbf{Cartesian Product} of sets $A$ and $B$, denoted $A \times B$, is the set of all ordered pairs:
$$A \times B = \{(a, b) \mid a \in A \land b \in B\}$$
If $|A| = m$ and $|B| = n$, then $|A \times B| = m \cdot n$.\\
A \textbf{binary relation} $R$ from $A$ to $B$ is a subset of the Cartesian product: $R \subseteq A \times B$. If $(a, b) \in R$, we write $a R b$.
\end{definition}

\subsubsection*{Representation of Relations}
1. \textbf{Matrix Representation ($M_R$):} For finite sets $A=\{a_1, \dots, a_m\}$ and $B=\{b_1, \dots, b_n\}$, $M_R = [m_{ij}]$ where $m_{ij} = 1$ if $(a_i, b_j) \in R$ and $0$ otherwise.
2. \textbf{Directed Graph (Digraph):} Nodes represent elements of set $A$; a directed edge points from $x$ to $y$ iff $(x, y) \in R$.

\subsection{Properties of Binary Relations (M2.05)}

Let $R$ be a binary relation on set $A$:

\begin{table}[h!]
\centering
\begin{tabular}{|l|l|p{6cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Property} & \color{white}\textbf{Formal Mathematical Condition} & \color{white}\textbf{Matrix / Digraph Meaning} \\ \hline
\textbf{Reflexive} & $\forall x \in A, \quad (x, x) \in R$ & Main diagonal of $M_R$ is all $1$s; self-loops at every vertex. \\ \hline
\textbf{Irreflexive} & $\forall x \in A, \quad (x, x) \notin R$ & Main diagonal of $M_R$ is all $0$s; no self-loops. \\ \hline
\textbf{Symmetric} & $\forall x, y \in A, \quad (x, y) \in R \rightarrow (y, x) \in R$ & $M_R$ is a symmetric matrix ($M_R = M_R^T$); edges are bidirectional. \\ \hline
\textbf{Antisymmetric} & $\forall x, y \in A, \quad ((x, y) \in R \land (y, x) \in R) \rightarrow x = y$ & No pair of opposite directed edges between distinct vertices. \\ \hline
\textbf{Transitive} & $\forall x, y, z \in A, \quad ((x, y) \in R \land (y, z) \in R) \rightarrow (x, z) \in R$ & Whenever path $x \to y \to z$ exists, shortcut edge $x \to z$ exists. \\ \hline
\end{tabular}
\caption{Properties of Binary Relations}
\end{table}

\subsection{Equivalence Relations \& Equivalence Classes (M2.05, M2.06)}

\begin{definition}[\textbf{Equivalence Relation}]
A relation $R$ on a set $A$ is an \textbf{Equivalence Relation} if and only if $R$ is \textbf{Reflexive}, \textbf{Symmetric}, and \textbf{Transitive}.
\end{definition}

\begin{definition}[\textbf{Equivalence Class}]
Let $R$ be an equivalence relation on set $A$. The \textbf{equivalence class} of an element $a \in A$, denoted $[a]$ or $\overline{a}$, is the set of all elements related to $a$:
$$[a] = \{x \in A \mid (a, x) \in R\}$$
\end{definition}

\begin{theorem}[\textbf{Partition Theorem}]
The equivalence classes of an equivalence relation on $A$ form a \textbf{partition} of $A$:
1. For all $a \in A$, $[a] \ne \emptyset$.
2. Any two equivalence classes are either identical or disjoint: $[a] \cap [b] = \emptyset$ if $[a] \ne [b]$.
3. The union of all equivalence classes equals $A$: $\bigcup_{a \in A} [a] = A$.
\end{theorem}

\newpage

% ==============================================================================
% SECTION 3: FUNCTIONS & COMPOSITION
% ==============================================================================
\section{Functions, Types \& Composition}

\subsection{Definition \& Basic Concepts (M2.07)}

\begin{definition}[\textbf{Function / Mapping}]
Let $A$ and $B$ be non-empty sets. A \textbf{function} $f$ from $A$ to $B$, written $f: A \to B$, is a rule that assigns to \textbf{each} element $x \in A$ \textbf{exactly one} element $y = f(x) \in B$.
\begin{itemize}
    \item $A$ is called the \textbf{Domain} of $f$.
    \item $B$ is called the \textbf{Codomain} of $f$.
    \item The \textbf{Range (Image)} of $f$ is $f(A) = \{f(x) \mid x \in A\} \subseteq B$.
\end{itemize}
\end{definition}

\subsection{Types of Functions (Injectivity, Surjectivity, Bijectivity)}

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|l|p{5.5cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Function Type} & \color{white}\textbf{Name} & \color{white}\textbf{Formal Definition} & \color{white}\textbf{How to Prove in Exams} \\ \hline
\textbf{One-to-One} & \textbf{Injective} & $f(x_1) = f(x_2) \implies x_1 = x_2$ & Assume $f(x_1) = f(x_2)$ and deduce $x_1 = x_2$. \\ \hline
\textbf{Onto} & \textbf{Surjective} & $\forall y \in B, \; \exists x \in A$ s.t. $f(x) = y$ & For arbitrary $y \in B$, solve $y = f(x)$ for $x \in A$. \\ \hline
\textbf{One-to-One Correspondence} & \textbf{Bijective} & Both \textbf{Injective AND Surjective} & Prove both one-to-one and onto conditions. \\ \hline
\end{tabular}
\caption{Classifications of Functions}
\end{table}

\subsection{Composition of Functions \& Inverse Functions}

\subsubsection*{Composition of Functions}
Let $f: A \to B$ and $g: B \to C$. The \textbf{composition function} $g \circ f: A \to C$ is defined as:
$$(g \circ f)(x) = g(f(x)) \quad \forall x \in A$$

\subsubsection*{Inverse Function}
A function $f: A \to B$ has an \textbf{inverse function} $f^{-1}: B \to A$ if and only if $f$ is \textbf{Bijective}.
$$(f^{-1} \circ f)(x) = x \quad \text{and} \quad (f \circ f^{-1})(y) = y$$

\newpage

% ==============================================================================
% SECTION 4: SOLVED UNIVERSITY EXAM QUESTION BANK (MODULE 2)
% ==============================================================================
\section{University Exam Question Bank \& Solved PYQs (Module 2)}

\begin{pyqbox}{DIPLOMA EXAMINATION PREVIOUS YEAR QUESTION BANK (REVISION 2021)}
Exact solved questions from State Board Diploma Examinations (November 2024 \& November 2025) for Module 2.
\end{pyqbox}

\subsection{Part A: 1-Mark Objective PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} Give an example of a finite set.
    \begin{sol}
    $A = \{1, 2, 3, 4, 5\}$ (or set of vowels $V = \{a, e, i, o, u\}$).
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2025]} If $(x^2 - 1, y + 3) = (3, 4)$, find the values of $x$ and $y$.
    \begin{sol}
    Equating corresponding components of ordered pairs: \\
    1) $x^2 - 1 = 3 \implies x^2 = 4 \implies \mathbf{x = \pm 2}$. \\
    2) $y + 3 = 4 \implies \mathbf{y = 1}$.
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2025]} Define injective function.
    \begin{sol}
    A function $f: A \to B$ is injective (one-to-one) if distinct elements in $A$ have distinct images in $B$, i.e., $f(x_1) = f(x_2) \implies x_1 = x_2$.
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2024]} If $|A| = m$ and $|B| = n$, then $n(A \times B) = \dots$?
    \begin{sol}
    $n(A \times B) = |A \times B| = m \cdot n = \mathbf{mn}$.
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2024]} If $f: A \to B$ is a function from $A$ to $B$, then $A$ is called $\dots$?
    \begin{sol}
    $A$ is called the \textbf{Domain} of $f$.
    \end{sol}
\end{enumerate}

\subsection{Part B: 3-Mark Short Answer PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} If $A = \{1, 2, 3, 4\}$, give an example of a relation on $A$ which is reflexive and transitive, but not symmetric.
    \begin{sol}
    Let $R = \{(1,1), (2,2), (3,3), (4,4), (1,2)\}$. \\
    • \textbf{Reflexive:} Contains $(1,1), (2,2), (3,3), (4,4)$. \\
    • \textbf{Transitive:} Vacuously holds for all pairs. \\
    • \textbf{Not Symmetric:} $(1,2) \in R$ but $(2,1) \notin R$.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025]} Find all subsets of the set $\{1, 2, 3\}$.
    \begin{sol}
    For $n=3$, there are $2^3 = 8$ subsets: \\
    $\emptyset$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1,2\}$, $\{1,3\}$, $\{2,3\}$, $\{1,2,3\}$.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025]} If $f: \mathbb{R} \to \mathbb{R}$ and $g: \mathbb{R} \to \mathbb{R}$ are given by $f(x) = \sin x$ and $g(x) = x^2$, find $(g \circ f)(x)$.
    \begin{sol}
    $(g \circ f)(x) = g(f(x)) = g(\sin x) = (\sin x)^2 = \mathbf{\sin^2 x}$.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} Let $f: \mathbb{R} \to \mathbb{R}$ where $f(x) = 3x + 7$ for all $x \in \mathbb{R}$. Prove that $f$ is one-one.
    \begin{sol}
    Assume $f(x_1) = f(x_2)$. \\
    $3x_1 + 7 = 3x_2 + 7 \implies 3x_1 = 3x_2 \implies x_1 = x_2$. \\
    Therefore, $f$ is \textbf{one-one (injective)}. ($\qed$)
    \end{sol}
\end{enumerate}

\subsection{Part C: 7-Mark Long Answer PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} \\
    a) Among a group of students, 49 study Physics ($P$), 37 study English ($E$), and 21 study Biology ($B$). If 9 study Physics and English, 5 study English and Biology, 4 study Physics and Biology, and 3 study Physics, English and Biology, find the total number of students in the group. \\
    b) Find the inverse for $f(x) = 6x + 3$. Verify your inverse by computing the composition.
    \begin{sol}
    \textbf{Part (a):} By the Inclusion-Exclusion Principle for 3 sets:
    \begin{align*}
    |P \cup E \cup B| &= |P| + |E| + |B| - |P \cap E| - |E \cap B| - |P \cap B| + |P \cap E \cap B| \\
    &= 49 + 37 + 21 - 9 - 5 - 4 + 3 \\
    &= 107 - 18 = \mathbf{89 \text{ students}}.
    \end{align*}
    \textbf{Part (b):} Let $y = f(x) = 6x + 3 \implies 6x = y - 3 \implies x = \frac{y - 3}{6}$. \\
    Thus, $f^{-1}(y) = \frac{y - 3}{6} \implies \mathbf{f^{-1}(x) = \frac{x - 3}{6}}$. \\
    \textbf{Verification:} \\
    $(f \circ f^{-1})(x) = f\left(\frac{x - 3}{6}\right) = 6\left(\frac{x - 3}{6}\right) + 3 = x - 3 + 3 = x$. ($\qed$)
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} If $A$ and $B$ are two sets such that $A \cup B$ has 50 elements, $A$ has 28 elements and $B$ has 32 elements, how many elements does $A \cap B$ have?
    \begin{sol}
    By the Inclusion-Exclusion Principle:
    $$|A \cup B| = |A| + |B| - |A \cap B|$$
    $$50 = 28 + 32 - |A \cap B| \implies 50 = 60 - |A \cap B| \implies |A \cap B| = 60 - 50 = \mathbf{10}.$$
    \end{sol}
\end{enumerate}

\end{document}
"""

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_content)
    print(f"Module 2 LaTeX file written to: {tex_path}")

# ------------------------------------------------------------------------------
# 2. GENERATE COMPILED PDF FOR MODULE 2
# ------------------------------------------------------------------------------
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
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#1E3A8A"))
            self.drawString(36, 762, "DISCRETE MATHEMATICS (3341) — MODULE 2: SETS, RELATIONS & FUNCTIONS")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawRightString(576, 762, "Diploma in AI & ML | Complete Notes & PYQ Bank")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(36, 754, 576, 754)

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

def create_module2_pdf():
    notes_dir = os.path.join(os.getcwd(), "Notes")
    os.makedirs(notes_dir, exist_ok=True)
    pdf_path = os.path.join(notes_dir, "Module_2_Discrete_Mathematics_Full_Notes.pdf")

    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=48, bottomMargin=48)
    styles = getSampleStyleSheet()

    C_PRIMARY = colors.HexColor("#1E3A8A")
    C_SECONDARY = colors.HexColor("#0D9488")
    C_TEXT = colors.HexColor("#0F172A")
    C_BG_BOX = colors.HexColor("#F0F9FF")
    C_BG_PYQ = colors.HexColor("#FAF5FF")
    C_BORDER_BOX = colors.HexColor("#BAE6FD")
    C_BORDER_PYQ = colors.HexColor("#E9D5FF")

    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=C_PRIMARY, alignment=1, spaceAfter=4)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=C_SECONDARY, alignment=1, spaceAfter=10)
    h1_style = ParagraphStyle('H1_Custom', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=C_PRIMARY, spaceBefore=14, spaceAfter=6, keepWithNext=True)
    h2_style = ParagraphStyle('H2_Custom', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=C_SECONDARY, spaceBefore=10, spaceAfter=4, keepWithNext=True)
    body_style = ParagraphStyle('Body_Custom', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=C_TEXT, spaceAfter=5)
    callout_text = ParagraphStyle('CText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#0369A1"))
    pyq_text = ParagraphStyle('PText', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#6B21A8"))

    table_header_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.white, alignment=1)
    table_cell_style = ParagraphStyle('TC', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=11, textColor=C_TEXT)

    story = []

    def make_box(text, title="DEFINITION", bg=C_BG_BOX, border=C_BORDER_BOX, txt_style=callout_text, title_clr="#075985"):
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

    # Header Banner
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

    story.append(Paragraph("MODULE 2: SETS, RELATIONS & FUNCTIONS", title_style))
    story.append(Paragraph("Full Lecture Notes & Solved Previous Year University Exam Questions (PYQ Bank)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_SECONDARY, spaceBefore=1, spaceAfter=8))

    meta_text = (
        "<b>Course Outcome CO2:</b> Demonstrate sets, relations and functions to solve computational problems.<br/>"
        "<b>Duration:</b> 16 Hours | <b>Cognitive Level:</b> Applying<br/>"
        "<b>Prescribed Textbooks:</b> (1) Kenneth H. Rosen (7th Ed), (2) Ralph P. Grimaldi (5th Ed), (3) Thomas Koshy (2nd Ed).<br/>"
        "<b>Exam Alignment:</b> Includes exact solved 1-mark, 3-mark, and 7-mark PYQs from State Board Exams (Nov 2024 & Nov 2025)."
    )
    story.append(make_box(meta_text, "COURSE SYLLABUS & EXAM ALIGNMENT", C_BG_BOX, C_BORDER_BOX, callout_text, "#075985"))
    story.append(Spacer(1, 10))

    # Section 1
    story.append(Paragraph("1. Set Theory & Inclusion-Exclusion Principle (M2.01 - M2.03)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))
    story.append(Paragraph(
        "• <b>Set & Power Set P(A):</b> Unordered collection of distinct elements. $|P(A)| = 2^n$.<br/>"
        "• <b>Set Operations:</b> Union ($A \\cup B$), Intersection ($A \\cap B$), Difference ($A \\setminus B$), Complement ($A'$), Symmetric Diff ($A \\oplus B$).<br/>"
        "• <b>De Morgan's Set Laws:</b> <i>(A \\cup B)' = A' \\cap B'</i> and <i>(A \\cap B)' = A' \\cup B'</i>.<br/>"
        "• <b>Inclusion-Exclusion Principle:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; 2 Sets: <i>|A \\cup B| = |A| + |B| - |A \\cap B|</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; 3 Sets: <i>|A \\cup B \\cup C| = |A| + |B| + |C| - |A \\cap B| - |B \\cap C| - |A \\cap C| + |A \\cap B \\cap C|</i>",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Section 2
    story.append(Paragraph("2. Relations & Equivalence Classes (M2.04 - M2.06)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))
    story.append(Paragraph(
        "• <b>Binary Relation R ⊆ A × B:</b> $|A \\times B| = m \\cdot n$. Represented by Boolean Matrix $M_R$ or Digraph.<br/>"
        "• <b>Properties of Relations on Set A:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; 1. <b>Reflexive:</b> $\\forall x \\in A, (x,x) \\in R$<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; 2. <b>Symmetric:</b> $(x,y) \\in R \\implies (y,x) \\in R$<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp; 3. <b>Transitive:</b> $(x,y) \\in R \\land (y,z) \\in R \\implies (x,z) \\in R$<br/>"
        "• <b>Equivalence Relation:</b> Relation that is Reflexive, Symmetric, and Transitive.<br/>"
        "• <b>Equivalence Class [a]:</b> $[a] = \\{x \\in A \\mid (a,x) \\in R\\}$. Equivalence classes partition set $A$ into disjoint subsets.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Section 3
    story.append(Paragraph("3. Functions & Composition (M2.07)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=5))
    story.append(Paragraph(
        "• <b>Function f: A → B:</b> Rule assigning each element in domain $A$ to a unique element in codomain $B$.<br/>"
        "• <b>Injective (One-to-One):</b> $f(x_1) = f(x_2) \\implies x_1 = x_2$.<br/>"
        "• <b>Surjective (Onto):</b> Range $f(A) = B$ (Codomain).<br/>"
        "• <b>Bijective:</b> Both Injective and Surjective. Inverse $f^{-1}: B → A$ exists iff $f$ is bijective.<br/>"
        "• <b>Composition (g ∘ f)(x):</b> $(g \\circ f)(x) = g(f(x))$.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Section 4: PYQs
    story.append(Paragraph("4. State Board Solved University Exam PYQ Bank (Module 2)", h1_style))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_PRIMARY, spaceBefore=1, spaceAfter=6))

    pyq_module2 = (
        "<b>SOLVED MODULE 2 PYQS FROM STATE BOARD DIPLOMA EXAMS (NOV 2024 & NOV 2025)</b><br/><br/>"
        "<b>Q1 [1-Mark, Nov 2025]:</b> If (x² - 1, y + 3) = (3, 4), find x and y.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> x² - 1 = 3 ⇒ x² = 4 ⇒ <b>x = ±2</b>. y + 3 = 4 ⇒ <b>y = 1</b>.<br/><br/>"
        "<b>Q2 [1-Mark, Nov 2024]:</b> If |A| = m and |B| = n, then n(A × B) = ......?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> n(A × B) = <b>m · n</b>.<br/><br/>"
        "<b>Q3 [3-Mark, Nov 2025]:</b> If f(x) = sin x and g(x) = x², find (g ∘ f)(x).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> (g ∘ f)(x) = g(f(x)) = g(sin x) = <b>sin² x</b>.<br/><br/>"
        "<b>Q4 [3-Mark, Nov 2024]:</b> Prove that f(x) = 3x + 7 is one-one.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> 3x₁ + 7 = 3x₂ + 7 ⇒ 3x₁ = 3x₂ ⇒ x₁ = x₂. Hence one-one.<br/><br/>"
        "<b>Q5 [7-Mark, Nov 2025]:</b> 49 study Physics (P), 37 English (E), 21 Biology (B). 9 study P&E, 5 E&B, 4 P&B, 3 P,E&B. Find total students.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> |P ∪ E ∪ B| = 49 + 37 + 21 - 9 - 5 - 4 + 3 = 107 - 18 = <b>89 students</b>.<br/><br/>"
        "<b>Q6 [7-Mark, Nov 2025]:</b> Find inverse for f(x) = 6x + 3.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Sol:</b> y = 6x + 3 ⇒ x = (y - 3)/6 ⇒ <b>f⁻¹(x) = (x - 3)/6</b>."
    )
    story.append(make_box(pyq_module2, "MODULE 2 SOLVED EXAM QUESTIONS (PYQ BANK)", C_BG_PYQ, C_BORDER_PYQ, pyq_text, "#6B21A8"))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Module 2 Full Notes PDF written to: {pdf_path}")

if __name__ == '__main__':
    create_module2_latex()
    create_module2_pdf()
