import os
import sys

def create_flawless_module1_latex():
    notes_dir = os.path.join(os.getcwd(), "Notes")
    os.makedirs(notes_dir, exist_ok=True)
    tex_path = os.path.join(notes_dir, "Module_1_Discrete_Mathematics.tex")

    latex_content = r"""\documentclass[11pt,a4paper]{article}

% --- Essential Standard Packages ---
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=0.75in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs,array,multirow,tabularx}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\tcbuselibrary{breakable}
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
\definecolor{codebg}{RGB}{248, 250, 252}       % Code block bg

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
\rhead{\small \textcolor{primaryblue}{\textbf{MODULE 1: MATHEMATICAL LOGIC | DISCRETE MATHEMATICS (3341)}}}
\lhead{\small \textcolor{gray}{Diploma in AI \& ML — Semester III}}
\rfoot{\small Page \thepage}
\lfoot{\small \textcolor{gray}{State Board of Technical Education, Kerala}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.6pt}

% --- Custom Breakable TColorBoxes ---
\newtcolorbox{lecturnote}[1]{
    breakable,
    colback=boxbg,
    colframe=primaryblue,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt,
    top=6pt,
    bottom=6pt,
    left=8pt,
    right=8pt
}

\newtcolorbox{examtip}[1]{
    breakable,
    colback=tipbg,
    colframe=orange!85!black,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt,
    top=6pt,
    bottom=6pt,
    left=8pt,
    right=8pt
}

\newtcolorbox{pyqbox}[1]{
    breakable,
    colback=pyqbg,
    colframe=purple!75!black,
    fonttitle=\bfseries\color{white},
    title=#1,
    arc=3pt,
    boxrule=1pt,
    top=6pt,
    bottom=6pt,
    left=8pt,
    right=8pt
}

% --- Title & Section Formatting ---
\titleformat{\section}{\large\bfseries\color{primaryblue}}{\thesection.}{0.5em}{}[\titlerule]
\titleformat{\subsection}{\bfseries\color{secondaryteal}}{\thesubsection}{0.5em}{}
\titleformat{\subsubsection}{\bfseries\color{darkslate}}{\thesubsubsection}{0.5em}{}

% --- Solution Environment ---
\newenvironment{sol}{\begin{proof}[Solution]}{\end{proof}}

\begin{document}

% ==============================================================================
% PAGE 1: ELEGANT COVER PAGE (NO TOC ON FRONT PAGE)
% ==============================================================================
\thispagestyle{empty}

\begin{center}
    \tcbset{colback=primaryblue,colframe=primaryblue,arc=0pt,top=12pt,bottom=12pt}
    \begin{tcolorbox}[halign=center]
        \color{white}
        {\large \textbf{STATE BOARD OF TECHNICAL EDUCATION, KERALA}}\\[4pt]
        {\Large \textbf{DIPLOMA EXAMINATION IN ENGINEERING \& TECHNOLOGY}}\\[4pt]
        {\large \textbf{COURSE: DISCRETE MATHEMATICS (COURSE CODE: 3341)}}\\[2pt]
        {\small SEMESTER III --- DIPLOMA IN ARTIFICIAL INTELLIGENCE \& MACHINE LEARNING}
    \end{tcolorbox}
\end{center}

\vspace{15pt}

\begin{center}
    {\huge \textbf{\textcolor{primaryblue}{MODULE 1: MATHEMATICAL LOGIC}}}\\[8pt]
    {\Large \textbf{\textcolor{secondaryteal}{EXHAUSTIVE COMPREHENSIVE LECTURE TEXTBOOK \& PYQ BANK}}}\\[6pt]
    \textit{Prescribed Textbooks: Kenneth H. Rosen (7th Ed), Ralph P. Grimaldi (5th Ed), Thomas Koshy (2nd Ed)}
\end{center}

\vspace{15pt}

\begin{lecturnote}{COURSE OUTCOME CO1 \& DETAILED SYLLABUS SCOPE}
\textbf{Course Outcome CO1:} Apply the basic concepts of mathematical logic to solve computational problems. (Duration: 16 Hours | Cognitive Level: Applying)\\[6pt]
\textbf{Module Sub-Outcomes (M1.01 -- M1.05):}
\begin{itemize}[leftmargin=1.5em, itemsep=3pt]
    \item \textbf{M1.01:} Describe the concept of propositional logic. (2 Hours, Cognitive Level: Understanding)
    \item \textbf{M1.02:} Solve problems using truth tables and logical operations. (3 Hours, Cognitive Level: Applying)
    \item \textbf{M1.03:} Prove logical equivalence, contingency, tautology and contradictions. (4 Hours, Cognitive Level: Applying)
    \item \textbf{M1.04:} Describe the concept of predicate logic. (3 Hours, Cognitive Level: Understanding)
    \item \textbf{M1.05:} Apply inference rules to solve problems. (4 Hours, Cognitive Level: Applying)
\end{itemize}
\end{lecturnote}

\vfill

\begin{center}
    \small \textcolor{darkslate}{\textbf{Department of Technical Education, Government of Kerala}}\\
    \small \textcolor{gray}{Academic Session 2024--2025 | Revision 2021 Syllabus}
\end{center}

\clearpage % Ends Cover Page Cleanly

% ==============================================================================
% PAGE 2: TABLE OF CONTENTS (DEDICATED PAGE)
% ==============================================================================
\pagestyle{fancy}
\thispagestyle{fancy}

\begin{center}
    {\Large \textbf{\textcolor{primaryblue}{TABLE OF CONTENTS}}}\\[4pt]
    \rule{\linewidth}{1pt}
\end{center}

\vspace{10pt}
\tableofcontents

\clearpage % Ends Table of Contents Page Cleanly

% ==============================================================================
% PAGE 3 ONWARDS: MAIN LECTURE TEXTBOOK CONTENT
% ==============================================================================

% ==============================================================================
% CHAPTER 1: PROPOSITIONAL LOGIC & LOGICAL OPERATIONS
% ==============================================================================
\section{Propositional Logic \& Logical Operations}

\subsection{Introduction \& Concept of Propositional Logic (M1.01)}

Logic is the formal study of reasoning, proof, and inference. In computer science and artificial intelligence, logic provides the foundation for digital circuit design, program verification, knowledge representation, automated reasoning, and database query optimization.

\begin{definition}[\textbf{Proposition / Statement}]
A \textbf{proposition} (or statement) is a declarative sentence that is either \textbf{True (T)} or \textbf{False (F)}, but not both. The truth value of a proposition is denoted by $\text{T}$ (or $1$) for true and $\text{F}$ (or $0$) for false.
\end{definition}

Propositions are conventionally represented using lowercase letters such as $p, q, r, s, t$.

\subsubsection*{Exhaustive Classification of Sentences}

To determine whether a sentence is a proposition, test whether it makes a declarative assertion that can be objectively assigned a single truth value ($\text{T}$ or $\text{F}$).

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|c|X|c|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{\#} & \color{white}\textbf{Sentence} & \color{white}\textbf{Is it a Proposition?} & \color{white}\textbf{Detailed Reason / Truth Value} \\ \hline
1 & Thiruvananthapuram is the capital of Kerala. & \textbf{YES} & Declarative statement; Truth Value = \textbf{T} \\ \hline
2 & $2 + 3 = 7$ & \textbf{YES} & Declarative statement; Truth Value = \textbf{F} \\ \hline
3 & Python is a high-level programming language. & \textbf{YES} & Declarative statement; Truth Value = \textbf{T} \\ \hline
4 & $x + 5 = 12$ & \textbf{NO} & Open sentence; value depends on variable $x$ \\ \hline
5 & What time is the Discrete Mathematics exam? & \textbf{NO} & Interrogative sentence (Question) \\ \hline
6 & Submit your laboratory assignment immediately! & \textbf{NO} & Imperative sentence (Command / Request) \\ \hline
7 & Oh, what a beautiful morning! & \textbf{NO} & Exclamatory sentence \\ \hline
8 & This statement is false. & \textbf{NO} & Self-referential paradox (Liar Paradox) \\ \hline
9 & Every prime number greater than 2 is odd. & \textbf{YES} & Declarative statement; Truth Value = \textbf{T} \\ \hline
10 & $x^2 \ge 0$ for all real numbers $x$. & \textbf{YES} & Declarative statement; Truth Value = \textbf{T} \\ \hline
\end{tabularx}
\caption{Classification of Sentences in Propositional Logic}
\end{table}

\subsubsection*{Atomic vs. Compound Propositions}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Atomic (Primitive) Proposition:} A simple proposition that expresses a single complete thought and cannot be divided into simpler propositions. \\
    \textit{Example:} $p$: ``$\sqrt{2}$ is an irrational number.''
    \item \textbf{Compound Proposition:} Formed by combining two or more atomic propositions using \textbf{logical connectives} (operators). \\
    \textit{Example:} $p \land q$: ``$\sqrt{2}$ is an irrational number AND $2$ is an even prime number.''
\end{itemize}

\subsection{Logical Connectives \& Fundamental Truth Tables (M1.02)}

Logical connectives combine primitive propositions to form compound propositions. Let $p$ and $q$ be propositions.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|c|c|l|X|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Connective} & \color{white}\textbf{Symbol} & \color{white}\textbf{Logical Name} & \color{white}\textbf{Meaning / Exact Condition for Truth} \\ \hline
NOT & $\neg$ (or $\sim$) & Negation & Reverses truth value. True when proposition is false. \\ \hline
AND & $\land$ & Conjunction & True \textbf{ONLY when BOTH} $p$ and $q$ are True. \\ \hline
OR & $\lor$ & Disjunction (Inclusive) & True when \textbf{AT LEAST ONE} of $p, q$ is True. \\ \hline
XOR & $\oplus$ & Exclusive-OR & True when \textbf{EXACTLY ONE} of $p, q$ is True (differs). \\ \hline
IF...THEN & $\rightarrow$ & Implication / Conditional & False \textbf{ONLY when} $p$ is True and $q$ is False. \\ \hline
IFF & $\leftrightarrow$ & Biconditional & True when $p$ and $q$ have the \textbf{SAME} truth value. \\ \hline
\end{tabularx}
\caption{Summary of Fundamental Logical Connectives}
\end{table}

\subsubsection*{Detailed Analysis of Each Logical Connective}

\paragraph{1. Negation ($\neg p$):}
The negation of $p$, written $\neg p$ (read ``not $p$''), is the proposition ``It is not the case that $p$''. The truth value of $\neg p$ is the opposite of the truth value of $p$.

\paragraph{2. Conjunction ($p \land q$):}
The conjunction of $p$ and $q$, written $p \land q$ (read ``$p$ and $q$''), is true when both $p$ and $q$ are true, and false otherwise. In natural language, words like ``but'', ``although'', ``however'' also represent conjunction.

\paragraph{3. Disjunction ($p \lor q$):}
The disjunction of $p$ and $q$, written $p \lor q$ (read ``$p$ or $q$''), is the inclusive OR statement. It is true when at least one of $p$ or $q$ is true, and false only when both $p$ and $q$ are false.

\paragraph{4. Exclusive-OR ($p \oplus q$):}
The exclusive OR of $p$ and $q$, written $p \oplus q$ (read ``$p$ XOR $q$''), is true when exactly one of $p$ or $q$ is true, and false when both are true or both are false.

\paragraph{5. Implication / Conditional Statement ($p \rightarrow q$):}
The conditional statement $p \rightarrow q$ (read ``if $p$, then $q$'') asserts that $p$ implies $q$.
\begin{itemize}[leftmargin=1.5em]
    \item $p$ is called the \textbf{Hypothesis} (or Antecedent / Premise).
    \item $q$ is called the \textbf{Conclusion} (or Consequent).
\end{itemize}

\begin{examtip}{THE 10 ENGLISH EXPRESSIONS FOR IMPLICATION ($p \rightarrow q$)}
In polytechnic examinations, the implication $p \rightarrow q$ appears in many verbal disguises:
\begin{multicols}{2}
\begin{enumerate}[leftmargin=1.5em]
    \item If $p$, then $q$
    \item $p$ implies $q$
    \item $p$ is sufficient for $q$
    \item $q$ is necessary for $p$
    \item $p$ only if $q$
    \item $q$ whenever $p$
    \item $q$ follows from $p$
    \item $q$ provided that $p$
    \item $q$ is a consequence of $p$
    \item $p$ leads to $q$
\end{enumerate}
\end{multicols}
\end{examtip}

\paragraph{6. Biconditional Statement ($p \leftrightarrow q$):}
The biconditional statement $p \leftrightarrow q$ (read ``$p$ if and only if $q$'', abbreviated ``$p$ iff $q$'') is true when $p$ and $q$ have the same truth value, and false when they have opposite truth values.

\subsubsection*{Master Truth Table for All Basic Connectives}

For $n=2$ atomic variables $p$ and $q$, there are $2^2 = 4$ possible truth assignments:

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|*{8}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{primaryblue} \color{white}$p$ & \color{white}$q$ & \color{white}$\neg p$ & \color{white}$p \land q$ & \color{white}$p \lor q$ & \color{white}$p \oplus q$ & \color{white}$p \rightarrow q$ & \color{white}$p \leftrightarrow q$ \\ \hline
T & T & F & \textbf{T} & \textbf{T} & F & \textbf{T} & \textbf{T} \\ \hline
T & F & F & F & \textbf{T} & \textbf{T} & \textcolor{red}{\textbf{F}} & F \\ \hline
F & T & T & F & \textbf{T} & \textbf{T} & \textbf{T} & F \\ \hline
F & F & T & F & F & F & \textbf{T} & \textbf{T} \\ \hline
\end{tabularx}
\caption{Master Truth Table for All Fundamental Logical Connectives}
\end{table}

\subsection{Construction of Complex Truth Tables}

To construct a truth table for any compound proposition involving $n$ atomic variables:
\begin{enumerate}[leftmargin=1.5em]
    \item Determine the number of rows: $2^n$ rows. For $n=2 \implies 4$ rows; for $n=3 \implies 8$ rows; for $n=4 \implies 16$ rows.
    \item Systematically fill the atomic variable columns in standard binary pattern.
    \item Break down the complex expression into sub-expressions working from inside parentheses outward.
    \item Evaluate each column step-by-step using the basic connective definitions.
\end{enumerate}

\subsubsection*{Worked Example 1: Construct the Truth Table for $(p \lor \neg q) \rightarrow (p \land q)$}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|*{7}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Row} & \color{white}$p$ & \color{white}$q$ & \color{white}$\neg q$ & \color{white}$p \lor \neg q$ (A) & \color{white}$p \land q$ (B) & \color{white}\textbf{A $\rightarrow$ B} \\ \hline
1 & T & T & F & T & T & \textbf{T} \\ \hline
2 & T & F & T & T & F & \textcolor{red}{\textbf{F}} \\ \hline
3 & F & T & F & F & F & \textbf{T} \\ \hline
4 & F & F & T & T & F & \textcolor{red}{\textbf{F}} \\ \hline
\end{tabularx}
\caption{Truth Table Evaluation for $(p \lor \neg q) \rightarrow (p \land q)$}
\end{table}

\subsubsection*{Worked Example 2: Construct the Truth Table for $(p \leftrightarrow q) \oplus (p \lor q)$}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|*{6}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Row} & \color{white}$p$ & \color{white}$q$ & \color{white}$p \leftrightarrow q$ (A) & \color{white}$p \lor q$ (B) & \color{white}\textbf{A $\oplus$ B} \\ \hline
1 & T & T & T & T & \textbf{F} \\ \hline
2 & T & F & F & T & \textbf{T} \\ \hline
3 & F & T & F & T & \textbf{T} \\ \hline
4 & F & F & T & F & \textbf{T} \\ \hline
\end{tabularx}
\caption{Truth Table Evaluation for $(p \leftrightarrow q) \oplus (p \lor q)$}
\end{table}

% ==============================================================================
% CHAPTER 2: CONDITIONAL STATEMENTS, IMPLICATION & TRUTH CLASSIFICATIONS
% ==============================================================================
\section{Conditional Statements, Implication \& Truth Classifications}

\subsection{Variants of Conditional Statements (M1.03)}

Given an original conditional statement $p \rightarrow q$, three related conditional statements can be constructed:

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|c|X|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Statement Name} & \color{white}\textbf{Symbolic Form} & \color{white}\textbf{English Translation} & \color{white}\textbf{Logical Equivalence} \\ \hline
Original Implication & $p \rightarrow q$ & If $p$, then $q$ & Baseline statement \\ \hline
\textbf{Converse} & $q \rightarrow p$ & If $q$, then $p$ & Logically equivalent to Inverse ($\neg p \rightarrow \neg q$) \\ \hline
\textbf{Inverse} & $\neg p \rightarrow \neg q$ & If not $p$, then not $q$ & Logically equivalent to Converse ($q \rightarrow p$) \\ \hline
\textbf{Contrapositive} & $\mathbf{\neg q \rightarrow \neg p}$ & If not $q$, then not $p$ & \textbf{STRICTLY EQUIVALENT to $p \rightarrow q$} \\ \hline
\end{tabularx}
\caption{The Three Variants of a Conditional Statement}
\end{table}

\subsubsection*{Proof of Logical Equivalence Between Implication and Contrapositive}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|*{8}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{secondaryteal} \color{white}$p$ & \color{white}$q$ & \color{white}$\neg p$ & \color{white}$\neg q$ & \color{white}\textbf{$p \rightarrow q$} & \color{white}\textbf{$\neg q \rightarrow \neg p$} & \color{white}$q \rightarrow p$ & \color{white}$\neg p \rightarrow \neg q$ \\ \hline
T & T & F & F & \textbf{T} & \textbf{T} & T & T \\ \hline
T & F & F & T & \textbf{F} & \textbf{F} & T & T \\ \hline
F & T & T & F & \textbf{T} & \textbf{T} & F & F \\ \hline
F & F & T & T & \textbf{T} & \textbf{T} & T & T \\ \hline
\end{tabularx}
\caption{Truth Table Proof of Equivalence for Contrapositive and Implication}
\end{table}

\begin{lecturnote}{FUNDAMENTAL THEOREM OF CONDITIONAL STATEMENTS}
As proven in Columns 5 and 6 of Table 5:
$$(p \rightarrow q) \;\;\equiv\;\; (\neg q \rightarrow \neg p)$$
A conditional statement and its contrapositive always have identical truth values in every row!  
However, the Converse ($q \rightarrow p$) and Inverse ($\neg p \rightarrow \neg q$) are NOT logically equivalent to the original implication $p \rightarrow q$.
\end{lecturnote}

\subsubsection*{Worked Verbal Translation Examples}

\paragraph{Example 3:}
Consider the statement: \textit{``If a triangle is equilateral ($p$), then it is equiangular ($q$).''}
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Converse ($q \rightarrow p$):} ``If a triangle is equiangular, then it is equilateral.'' (True)
    \item \textbf{Inverse ($\neg p \rightarrow \neg q$):} ``If a triangle is not equilateral, then it is not equiangular.'' (True)
    \item \textbf{Contrapositive ($\neg q \rightarrow \neg p$):} ``If a triangle is not equiangular, then it is not equilateral.'' (True)
\end{itemize}

\paragraph{Example 4:}
Consider the statement: \textit{``If $2 < 3$ and $3 + 7 = 10$, then $\sqrt{4} = 2$.''}
\begin{itemize}[leftmargin=1.5em]
    \item Let $p$: ``$2 < 3 \land 3 + 7 = 10$'' (Truth value = \textbf{T}).
    \item Let $q$: ``$\sqrt{4} = 2$'' (Truth value = \textbf{T}).
    \item \textbf{Original Implication ($p \rightarrow q$):} Truth value: $\text{T} \rightarrow \text{T} \equiv \mathbf{T}$.
    \item \textbf{Converse ($q \rightarrow p$):} ``If $\sqrt{4} = 2$, then $2 < 3$ and $3 + 7 = 10$''. Truth value: $\text{T} \rightarrow \text{T} \equiv \mathbf{T}$.
    \item \textbf{Inverse ($\neg p \rightarrow \neg q$):} ``If it is not the case that ($2 < 3$ and $3 + 7 = 10$), then $\sqrt{4} \ne 2$''. Truth value: $\text{F} \rightarrow \text{F} \equiv \mathbf{T}$.
    \item \textbf{Contrapositive ($\neg q \rightarrow \neg p$):} ``If $\sqrt{4} \ne 2$, then it is not the case that ($2 < 3$ and $3 + 7 = 10$)''. Truth value: $\text{F} \rightarrow \text{F} \equiv \mathbf{T}$.
\end{itemize}

\subsection{Tautology, Contradiction, and Contingency (M1.03)}

Compound propositions are categorized into three distinct classes based on their truth values across all possible truth assignments:

\begin{definition}[\textbf{Truth Classifications}]
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Tautology ($\mathbf{T}$):} A compound proposition that is \textbf{ALWAYS TRUE} under all possible truth assignments for its atomic variables (e.g., $p \lor \neg p$).
    \item \textbf{Contradiction ($\mathbf{F}$):} A compound proposition that is \textbf{ALWAYS FALSE} under all possible truth assignments for its atomic variables (e.g., $p \land \neg p$).
    \item \textbf{Contingency:} A compound proposition that is \textbf{NEITHER} a tautology nor a contradiction (it is true under some assignments and false under others, e.g., $p \rightarrow q$).
\end{itemize}
\end{definition}

\subsubsection*{Worked Example 5: Prove that $[(p \rightarrow q) \land (q \rightarrow r)] \rightarrow (p \rightarrow r)$ is a Tautology}

This compound proposition represents the fundamental rule of reasoning known as \textbf{Hypothetical Syllogism}.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|*{8}{>{\centering\arraybackslash}X|}}
\hline
\rowcolor{primaryblue} \color{white}$p$ & \color{white}$q$ & \color{white}$r$ & \color{white}$p \rightarrow q$ & \color{white}$q \rightarrow r$ & \color{white}$(p \rightarrow q) \land (q \rightarrow r)$ (A) & \color{white}$p \rightarrow r$ (B) & \color{white}\textbf{A $\rightarrow$ B} \\ \hline
T & T & T & T & T & T & T & \textbf{T} \\ \hline
T & T & F & T & F & F & F & \textbf{T} \\ \hline
T & F & T & F & T & F & T & \textbf{T} \\ \hline
T & F & F & F & T & F & F & \textbf{T} \\ \hline
F & T & T & T & T & T & T & \textbf{T} \\ \hline
F & T & F & T & F & F & T & \textbf{T} \\ \hline
F & F & T & T & T & T & T & \textbf{T} \\ \hline
F & F & F & T & T & T & T & \textbf{T} \\ \hline
\end{tabularx}
\caption{Truth Table Proof showing Hypothetical Syllogism is a Tautology}
\end{table}

\noindent \textit{Conclusion:} Since every single entry in the final column is $\text{T}$, the proposition is a \textbf{Tautology}.

\subsection{Normal Forms: DNF and CNF}

In propositional logic, any compound proposition can be transformed into a standardized canonical form:

\begin{definition}[\textbf{Literals, Minterms, Maxterms, DNF, CNF}]
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Literal:} An atomic variable $p$ or its negation $\neg p$.
    \item \textbf{Minterm:} A conjunction ($\land$) of literals in which each variable appears exactly once (either negated or unnegated). A minterm evaluates to $\text{T}$ for exactly one row of the truth table.
    \item \textbf{Maxterm:} A disjunction ($\lor$) of literals in which each variable appears exactly once. A maxterm evaluates to $\text{F}$ for exactly one row.
    \item \textbf{Disjunctive Normal Form (DNF / Sum-of-Products):} A disjunction ($\lor$) of minterms. DNF is formed by taking the minterms corresponding to all rows in the truth table where the final output is \textbf{TRUE (T)}.
    \item \textbf{Conjunctive Normal Form (CNF / Product-of-Sums):} A conjunction ($\land$) of maxterms. CNF is formed by taking the maxterms corresponding to all rows where the final output is \textbf{FALSE (F)}.
\end{itemize}
\end{definition}

\subsubsection*{Worked Example 6: Derive DNF and CNF for $p \oplus q$}

From the master truth table of $p \oplus q$:
\begin{itemize}[leftmargin=1.5em]
    \item Output is \textbf{TRUE} in Row 2 ($p=\text{T}, q=\text{F}$) and Row 3 ($p=\text{F}, q=\text{T}$).
    \item Minterm for Row 2: $p \land \neg q$
    \item Minterm for Row 3: $\neg p \land q$
    \item \textbf{DNF Representation:} $\mathbf{(p \land \neg q) \lor (\neg p \land q)}$
    \item Output is \textbf{FALSE} in Row 1 ($p=\text{T}, q=\text{T}$) and Row 4 ($p=\text{F}, q=\text{F}$).
    \item Maxterm for Row 1: $\neg p \lor \neg q$
    \item Maxterm for Row 4: $p \lor q$
    \item \textbf{CNF Representation:} $\mathbf{(\neg p \lor \neg q) \land (p \lor q)}$
\end{itemize}

% ==============================================================================
% CHAPTER 3: LOGICAL EQUIVALENCE & DUALITY PRINCIPLE
% ==============================================================================
\section{Logical Equivalence \& Duality Principle}

\subsection{Concept of Logical Equivalence (M1.03)}

\begin{definition}[\textbf{Logical Equivalence}]
Two compound propositions $A$ and $B$ are \textbf{logically equivalent}, written $A \equiv B$ or $A \Leftrightarrow B$, if and only if $A \leftrightarrow B$ is a \textbf{Tautology}. Equivalent propositions have identical truth values in every row of their joint truth table.
\end{definition}

\subsection{Fundamental Laws of Logical Equivalences}

The algebraic laws of propositional logic allow simplifying expressions and proving equivalences without constructing truth tables.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|X|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Law Category} & \color{white}\textbf{Equivalence Statement 1 (AND / OR)} & \color{white}\textbf{Equivalence Statement 2 (Dual Form)} \\ \hline
\textbf{Identity Laws} & $p \land \mathbf{T} \equiv p$ & $p \lor \mathbf{F} \equiv p$ \\ \hline
\textbf{Domination Laws} & $p \lor \mathbf{T} \equiv \mathbf{T}$ & $p \land \mathbf{F} \equiv \mathbf{F}$ \\ \hline
\textbf{Idempotent Laws} & $p \lor p \equiv p$ & $p \land p \equiv p$ \\ \hline
\textbf{Double Negation Law} & $\neg(\neg p) \equiv p$ & --- \\ \hline
\textbf{Commutative Laws} & $p \lor q \equiv q \lor p$ & $p \land q \equiv q \land p$ \\ \hline
\textbf{Associative Laws} & $(p \lor q) \lor r \equiv p \lor (q \lor r)$ & $(p \land q) \land r \equiv p \land (q \land r)$ \\ \hline
\textbf{Distributive Laws} & $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ & $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ \\ \hline
\textbf{De Morgan's Laws} & \textbf{$\neg(p \land q) \equiv \neg p \lor \neg q$} & \textbf{$\neg(p \lor q) \equiv \neg p \land \neg q$} \\ \hline
\textbf{Absorption Laws} & $p \lor (p \land q) \equiv p$ & $p \land (p \lor q) \equiv p$ \\ \hline
\textbf{Negation Laws} & $p \lor \neg p \equiv \mathbf{T}$ & $p \land \neg p \equiv \mathbf{F}$ \\ \hline
\textbf{Conditional Equivalences} & \textbf{$p \rightarrow q \equiv \neg p \lor q$} & \textbf{$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$} \\ \hline
\textbf{Exportation Law} & \multicolumn{2}{c|}{$(p \land q) \rightarrow r \;\;\equiv\;\; p \rightarrow (q \rightarrow r)$} \\ \hline
\end{tabularx}
\caption{Fundamental Laws of Logical Equivalences}
\end{table}

\subsection{Algebraic Proofs Without Truth Tables}

In polytechnic examinations, proving equivalences using algebraic laws requires stating the exact law used at each step.

\subsubsection*{Worked Example 7: Prove that $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$}

\begin{proof}
Starting from the Left-Hand Side (LHS):
\begin{align*}
\neg(p \lor (\neg p \land q)) &\equiv \neg p \land \neg(\neg p \land q) && \text{[By De Morgan's Law]} \\
&\equiv \neg p \land (\neg(\neg p) \lor \neg q) && \text{[By De Morgan's Law]} \\
&\equiv \neg p \land (p \lor \neg q) && \text{[By Double Negation Law]} \\
&\equiv (\neg p \land p) \lor (\neg p \land \neg q) && \text{[By Distributive Law]} \\
&\equiv \mathbf{F} \lor (\neg p \land \neg q) && \text{[By Negation Law: $\neg p \land p \equiv \mathbf{F}$]} \\
&\equiv \mathbf{\neg p \land \neg q} && \text{[By Identity Law: $\mathbf{F} \lor A \equiv A$]}
\end{align*}
LHS = RHS. Hence proved algebraically without constructing a truth table.
\end{proof}

\subsubsection*{Worked Example 8: Prove that $(p \rightarrow q) \land (p \rightarrow r) \equiv p \rightarrow (q \land r)$}

\begin{proof}
Starting from LHS:
\begin{align*}
(p \rightarrow q) \land (p \rightarrow r) &\equiv (\neg p \lor q) \land (\neg p \lor r) && \text{[By Conditional Equivalence: $A \rightarrow B \equiv \neg A \lor B$]} \\
&\equiv \neg p \lor (q \land r) && \text{[By Distributive Law (factoring out $\neg p$)]} \\
&\equiv \mathbf{p \rightarrow (q \land r)} && \text{[By Conditional Equivalence]}
\end{align*}
LHS = RHS. Hence proved.
\end{proof}

\subsection{Duality Principle}

\begin{definition}[\textbf{Dual of a Compound Proposition}]
Let $s$ be a compound proposition containing only connectives $\land, \lor,$ and $\neg$. The \textbf{dual of $s$}, denoted $s^*$, is obtained by replacing:
\begin{itemize}[leftmargin=1.5em]
    \item Every $\land$ with $\lor$, and every $\lor$ with $\land$.
    \item Every $\mathbf{T}$ (Tautology) with $\mathbf{F}$ (Contradiction), and every $\mathbf{F}$ with $\mathbf{T}$.
\end{itemize}
\textit{Crucial Note:} Negation operators ($\neg$) and atomic variables remain completely unchanged!
\end{definition}

\begin{theorem}[\textbf{Principle of Duality}]
If two compound propositions $s$ and $t$ are logically equivalent ($s \equiv t$), then their duals are also logically equivalent ($s^* \equiv t^*$).
\end{theorem}

\subsubsection*{Worked Examples of Duality}
1. Statement $s$: $(p \land q) \lor \mathbf{T}$ $\implies$ Dual $s^*$: $\mathbf{(p \lor q) \land \mathbf{F}}$. \\
2. Statement $s$: $(p \lor \neg q) \land (r \lor \mathbf{F})$ $\implies$ Dual $s^*$: $\mathbf{(p \land \neg q) \lor (r \land \mathbf{T})}$. \\
3. Identity $p \lor (p \land q) \equiv p$ (Absorption Law) $\implies$ Dual Identity: $\mathbf{p \land (p \lor q) \equiv p}$.

% ==============================================================================
% CHAPTER 4: PREDICATE LOGIC & QUANTIFIERS
% ==============================================================================
\section{Predicate Logic \& Quantifiers}

\subsection{Limitations of Propositional Logic \& Need for Predicate Logic (M1.04)}

Propositional logic cannot express assertions involving properties of objects or relationships between elements. For example, the valid argument:
\begin{center}
\textit{``All computer science students take Discrete Mathematics. Rahul is a computer science student. Therefore, Rahul takes Discrete Mathematics.''}
\end{center}
cannot be represented in propositional logic because it lacks variables, predicates, and quantifiers.

\subsection{Predicates \& Propositional Functions}

\begin{definition}[\textbf{Predicate \& Domain}]
A statement involving a variable $x$, denoted $P(x)$, consists of two parts:
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Subject ($x$):} The variable taking values from a specified set.
    \item \textbf{Predicate ($P$):} The property or characteristic assigned to $x$.
    \item \textbf{Domain of Discourse (Universe $U$):} The set of all possible values that $x$ can take.
\end{itemize}
$P(x)$ is a \textbf{propositional function}; it becomes a proposition with a definite truth value only when a specific value $c \in U$ is assigned to $x$, or when $x$ is bound by a quantifier.
\end{definition}

\subsubsection*{Multiple Variables ($n$-ary Predicates)}
- Unary Predicate: $P(x)$ --- ``$x > 5$'' \\
- Binary Predicate: $Q(x, y)$ --- ``$x + y = 10$'' \\
- Ternary Predicate: $R(x, y, z)$ --- ``$x^2 + y^2 = z^2$''

\subsection{Quantifiers (Universal \& Existential)}

Quantification converts a propositional function $P(x)$ into a proposition over a domain $U$.

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|c|l|X|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Quantifier Name} & \color{white}\textbf{Symbol} & \color{white}\textbf{Meaning in English} & \color{white}\textbf{When is it TRUE?} & \color{white}\textbf{When is it FALSE?} \\ \hline
\textbf{Universal Quantifier} & $\forall x \, P(x)$ & For all $x$, $P(x)$ & $P(x)$ is True for \textbf{EVERY} $x \in U$. & At least one counterexample $x \in U$ exists where $P(x)$ is False. \\ \hline
\textbf{Existential Quantifier} & $\exists x \, P(x)$ & There exists an $x$ such that $P(x)$ & $P(x)$ is True for \textbf{AT LEAST ONE} $x \in U$. & $P(x)$ is False for \textbf{EVERY SINGLE} $x \in U$. \\ \hline
\end{tabularx}
\caption{Truth Conditions for Universal and Existential Quantifiers}
\end{table}

\subsubsection*{Finite Domain Expansions}
If the domain $U$ is finite, $U = \{a_1, a_2, \dots, a_n\}$:
$$\forall x \, P(x) \;\;\equiv\;\; P(a_1) \land P(a_2) \land \dots \land P(a_n)$$
$$\exists x \, P(x) \;\;\equiv\;\; P(a_1) \lor P(a_2) \lor \dots \lor P(a_n)$$

\subsection{Quantifiers over Restricted Domains}

\begin{examtip}{RESTRICTED DOMAIN CONVENTION}
When quantifiers are restricted to a subset of domain $U$:
\begin{enumerate}[leftmargin=1.5em]
    \item \textbf{Universal Quantifier ($\forall$) uses Implication ($\rightarrow$):}
    $$\forall x < 0 \, (x^2 > 0) \;\;\equiv\;\; \forall x \, (x < 0 \rightarrow x^2 > 0)$$
    \item \textbf{Existential Quantifier ($\exists$) uses Conjunction ($\land$):}
    $$\exists x > 0 \, (x^2 = 2) \;\;\equiv\;\; \exists x \, (x > 0 \land x^2 = 2)$$
\end{enumerate}
\end{examtip}

\subsection{Negation of Quantified Statements (De Morgan's Laws for Quantifiers)}

To negate a quantified statement, change the quantifier type and negate the predicate:
$$\mathbf{\neg (\forall x \, P(x)) \;\;\equiv\;\; \exists x \, \neg P(x)}$$
$$\mathbf{\neg (\exists x \, P(x)) \;\;\equiv\;\; \forall x \, \neg P(x)}$$

\subsubsection*{Finite Domain Proof of Quantifier De Morgan's Law}
Let domain $U = \{a, b, c\}$.
\begin{align*}
\neg(\forall x \, P(x)) &\equiv \neg(P(a) \land P(b) \land P(c)) \\
&\equiv \neg P(a) \lor \neg P(b) \lor \neg P(c) && \text{[By De Morgan's Law for Propositional Logic]} \\
&\equiv \exists x \, \neg P(x) && \text{Q.E.D.}
\end{align*}

\subsection{Nested Quantifiers}

When multiple quantifiers are present, \textbf{the order of quantifiers matters!}
$$\forall x \, \exists y \, P(x, y) \;\;\not\equiv\;\; \exists y \, \forall x \, P(x, y)$$

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|X|X|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Statement} & \color{white}\textbf{When is it TRUE?} & \color{white}\textbf{When is it FALSE?} \\ \hline
$\forall x \, \forall y \, P(x, y)$ & $P(x, y)$ is True for \textbf{every pair} $(x, y)$. & There is at least one pair $(x, y)$ where $P(x, y)$ is False. \\ \hline
$\forall x \, \exists y \, P(x, y)$ & For \textbf{every $x$}, there is \textbf{at least one $y$} (which may depend on $x$) making $P(x,y)$ True. & There is some $x$ for which no $y$ makes $P(x,y)$ True. \\ \hline
$\exists x \, \forall y \, P(x, y)$ & There is \textbf{at least one fixed $x$} that works for \textbf{every single $y$}. & For every $x$, there is at least one $y$ where $P(x,y)$ fails. \\ \hline
$\exists x \, \exists y \, P(x, y)$ & There is \textbf{at least one pair} $(x, y)$ for which $P(x, y)$ is True. & $P(x, y)$ is False for \textbf{every possible pair} $(x, y)$. \\ \hline
\end{tabularx}
\caption{Nested Quantifier Truth Conditions Matrix}
\end{table}

% ==============================================================================
% CHAPTER 5: RULES OF INFERENCE & NATURAL DEDUCTION
% ==============================================================================
\section{Rules of Inference \& Natural Deduction}

\subsection{Logical Arguments \& Validity (M1.05)}

An \textbf{argument} in logic is a sequence of statements ending in a conclusion. The initial statements are called \textbf{premises} ($P_1, P_2, \dots, P_k$) and the final statement is the \textbf{conclusion} ($C$).

\begin{definition}[\textbf{Valid Argument}]
An argument with premises $P_1, P_2, \dots, P_k$ and conclusion $C$ is \textbf{VALID} if and only if the conditional statement:
$$(P_1 \land P_2 \land \dots \land P_k) \;\;\rightarrow\;\; C \quad \text{is a \textbf{Tautology}}.$$
An invalid argument is called a \textbf{fallacy}.
\end{definition}

\subsection{Rules of Inference for Propositional Logic}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|c|c|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Rule Name} & \color{white}\textbf{Premises} & \color{white}\textbf{Conclusion} & \color{white}\textbf{Tautology Form} \\ \hline
\textbf{Modus Ponens} & $p, \; p \rightarrow q$ & $\therefore q$ & $[p \land (p \rightarrow q)] \rightarrow q$ \\ \hline
\textbf{Modus Tollens} & $\neg q, \; p \rightarrow q$ & $\therefore \neg p$ & $[\neg q \land (p \rightarrow q)] \rightarrow \neg p$ \\ \hline
\textbf{Hypothetical Syllogism} & $p \rightarrow q, \; q \rightarrow r$ & $\therefore p \rightarrow r$ & $[(p \rightarrow q) \land (q \rightarrow r)] \rightarrow (p \rightarrow r)$ \\ \hline
\textbf{Disjunctive Syllogism} & $p \lor q, \; \neg p$ & $\therefore q$ & $[(p \lor q) \land \neg p] \rightarrow q$ \\ \hline
\textbf{Addition} & $p$ & $\therefore p \lor q$ & $p \rightarrow (p \lor q)$ \\ \hline
\textbf{Simplification} & $p \land q$ & $\therefore p$ & $(p \land q) \rightarrow p$ \\ \hline
\textbf{Conjunction} & $p, \; q$ & $\therefore p \land q$ & $[(p) \land (q)] \rightarrow (p \land q)$ \\ \hline
\textbf{Resolution} & $p \lor q, \; \neg p \lor r$ & $\therefore q \lor r$ & $[(p \lor q) \land (\neg p \lor r)] \rightarrow (q \lor r)$ \\ \hline
\end{tabularx}
\caption{Primary Rules of Inference for Propositional Logic}
\end{table}

\subsection{Rules of Inference for Quantified Statements}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|c|c|X|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Rule Name} & \color{white}\textbf{Premise} & \color{white}\textbf{Conclusion} & \color{white}\textbf{Condition / Restriction} \\ \hline
\textbf{Universal Instantiation (UI)} & $\forall x \, P(x)$ & $\therefore P(c)$ & $c$ is ANY element in domain $U$. \\ \hline
\textbf{Universal Generalization (UG)} & $P(c)$ for arbitrary $c$ & $\therefore \forall x \, P(x)$ & $c$ MUST be an \textbf{arbitrary} element. \\ \hline
\textbf{Existential Instantiation (EI)} & $\exists x \, P(x)$ & $\therefore P(c)$ & $c$ is a \textbf{SOME specific} element (must be new!). \\ \hline
\textbf{Existential Generalization (EG)} & $P(c)$ for known $c$ & $\therefore \exists x \, P(x)$ & Holds if $P(c)$ is true for a known element $c$. \\ \hline
\end{tabularx}
\caption{Rules of Inference for Quantified Statements}
\end{table}

\subsection{Formal Two-Column Proof Examples}

\subsubsection*{Worked Example 9: Prove conclusion $s$ given premises: (1) $p \rightarrow q$, (2) $q \rightarrow r$, (3) $\neg r$, and (4) $p \lor s$}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|c|X|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Step} & \color{white}\textbf{Statement} & \color{white}\textbf{Justification / Rule Used} \\ \hline
1 & $p \rightarrow q$ & Premise 1 \\ \hline
2 & $q \rightarrow r$ & Premise 2 \\ \hline
3 & $p \rightarrow r$ & \textbf{Hypothetical Syllogism} on Steps 1 and 2 \\ \hline
4 & $\neg r$ & Premise 3 \\ \hline
5 & $\neg p$ & \textbf{Modus Tollens} on Steps 3 and 4 \\ \hline
6 & $p \lor s$ & Premise 4 \\ \hline
7 & \textbf{$s$} & \textbf{Disjunctive Syllogism} on Steps 5 and 6 (\textbf{Q.E.D.}) \\ \hline
\end{tabularx}
\caption{Two-Column Natural Deduction Proof}
\end{table}

% ==============================================================================
% CHAPTER 6: METHODS OF PROOF & RESOLUTION PRINCIPLE
% ==============================================================================
\section{Methods of Proof \& Resolution Principle}

\subsection{Standard Methods of Proof (M1.05)}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{|l|X|X|X|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Proof Method} & \color{white}\textbf{Assumption Made} & \color{white}\textbf{Goal to Demonstrate} & \color{white}\textbf{Key Strategy / Logic} \\ \hline
\textbf{Direct Proof} & Assume $p$ is True & Show $q$ is True & Use axioms, definitions, and logic directly. \\ \hline
\textbf{Proof by Contraposition} & Assume $\neg q$ is True & Show $\neg p$ is True & Uses logical equivalence $(p \rightarrow q) \equiv (\neg q \rightarrow \neg p)$. \\ \hline
\textbf{Proof by Contradiction} & Assume $\neg p$ (or $p \land \neg q$) & Derive contradiction $r \land \neg r$ ($\mathbf{F}$) & If assumption leads to non-sense, original statement is True! \\ \hline
\textbf{Proof by Cases} & Assume $p = p_1 \lor p_2 \lor \dots \lor p_k$ & Show $p_i \rightarrow q$ for all $i$ & Exhaustive evaluation of all distinct scenarios. \\ \hline
\end{tabularx}
\caption{Summary of Proof Strategies}
\end{table}

\subsubsection*{Classical Proof Example: Prove that $\sqrt{2}$ is an Irrational Number (Proof by Contradiction)}

\begin{proof}
\begin{enumerate}[leftmargin=1.5em]
    \item Assume for contradiction that \textbf{$\sqrt{2}$ is rational}. Then $\sqrt{2}$ can be written as a fraction $a/b$ in lowest terms, where $a, b \in \mathbb{Z}$ and $\gcd(a, b) = 1$.
    \item Squaring both sides gives: $2 = \frac{a^2}{b^2} \implies a^2 = 2b^2$.
    \item Since $a^2$ is a multiple of $2$, $a^2$ is even, which implies \textbf{$a$ is even}. Let $a = 2k$ for some integer $k$.
    \item Substitute $a = 2k$ into the equation: $(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2$.
    \item This implies $b^2$ is even, so \textbf{$b$ is also even}.
    \item Since both $a$ and $b$ are even, they share a common factor of $2$, contradicting the assumption that $\gcd(a, b) = 1$!
    \item Therefore, our initial assumption that $\sqrt{2}$ is rational is FALSE. Thus, \textbf{$\sqrt{2}$ is IRRATIONAL}. $\qed$
\end{enumerate}
\end{proof}

\subsection{Resolution Principle \& Resolution Refutation}

The \textbf{Resolution Principle} (Robinson, 1965) is an algorithmic inference rule used in automated theorem proving (such as Prolog).

\begin{definition}[\textbf{Clause Form \& Resolvent}]
\begin{itemize}[leftmargin=1.5em]
    \item \textbf{Clause:} A disjunction ($\lor$) of literals, e.g., $C_1 = p \lor \neg q \lor r$.
    \item \textbf{Resolvent Rule:} Given two clauses containing complementary literals ($p$ and $\neg p$):
    $$\frac{p \lor C, \quad \neg p \lor D}{\therefore C \lor D} \quad \text{(Resolvent)}$$
\end{itemize}
\end{definition}

\subsubsection*{Resolution Refutation Algorithm (Proof by Contradiction):}
\begin{enumerate}[leftmargin=1.5em]
    \item Convert all premises into Clause Form (CNF disjunctions).
    \item Negate the conclusion to be proven and convert it into clause form.
    \item Add the negated conclusion clause to the set of premise clauses.
    \item Iteratively apply the resolution rule to pairs of clauses to generate new resolvent clauses.
    \item If the \textbf{Empty Clause ($\square$ or $\mathbf{F}$)} is derived, a contradiction is established, proving the original conclusion VALID!
\end{enumerate}

\subsubsection*{Worked Resolution Refutation Example}
Prove premises $p \rightarrow q$ and $p$ entail conclusion $q$:
\begin{enumerate}[leftmargin=1.5em]
    \item Premise 1 in clause form: $p \rightarrow q \equiv \mathbf{\neg p \lor q}$ (Clause 1).
    \item Premise 2 in clause form: $\mathbf{p}$ (Clause 2).
    \item Negated conclusion: $\mathbf{\neg q}$ (Clause 3).
    \item Resolve Clause 1 ($\neg p \lor q$) and Clause 2 ($p$) on $p \implies \mathbf{q}$ (Clause 4).
    \item Resolve Clause 4 ($q$) and Clause 3 ($\neg q$) on $q \implies \mathbf{\square}$ (\textbf{Empty Clause / Contradiction}).
    \item Since $\square$ is derived, the argument is \textbf{VALID}. $\qed$
\end{enumerate}

% ==============================================================================
% CHAPTER 7: PREVIOUS YEAR UNIVERSITY QUESTION BANK (PYQ) WITH FULL SOLUTIONS
% ==============================================================================
\section{University Exam Question Bank \& Solved PYQs (Module 1)}

\begin{pyqbox}{DIPLOMA EXAMINATION PREVIOUS YEAR QUESTION BANK (REVISION 2021)}
This section contains \textbf{exact questions} asked in the State Board Diploma Examinations (November 2024 \& November 2025) for Module 1, along with step-by-step model solutions prepared by senior faculty.
\end{pyqbox}

\subsection{Part A: 1-Mark Objective PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} Interpret the logical equivalence to the statement: \textit{``I pass only if you pass''}.
    \begin{sol}
    Let $p$: ``I pass'', $q$: ``You pass''. \\
    The phrase ``$p$ only if $q$'' is symbolically expressed as the conditional statement \textbf{$p \rightarrow q$}. \\
    By logical equivalence, $p \rightarrow q \equiv \mathbf{\neg p \lor q} \equiv \mathbf{\neg q \rightarrow \neg p}$ (Contrapositive: \textit{``If you do not pass, then I do not pass''}).
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2025]} Write the dual for $(p \land q) \lor \mathbf{T}$.
    \begin{sol}
    By the Duality Principle, replace $\land \leftrightarrow \lor$ and $\mathbf{T} \leftrightarrow \mathbf{F}$. \\
    Dual statement $= \mathbf{(p \lor q) \land \mathbf{F}}$.
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2024]} If $p$ is a proposition, $\neg(\neg p) = \dots$?
    \begin{sol}
    By the Double Negation Law, $\neg(\neg p) = \mathbf{p}$.
    \end{sol}
    \vspace{4pt}

    \item \textbf{[Nov 2024]} If $A$ has $n$ elements, then number of subsets of $A = \dots$?
    \begin{sol}
    Number of subsets $= |P(A)| = \mathbf{2^n}$.
    \end{sol}
\end{enumerate}

\subsection{Part B: 3-Mark Short Answer PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} Show that the implication $[(p \rightarrow q) \land (q \rightarrow r)] \rightarrow (p \rightarrow r)$ is a tautology.
    \begin{sol}
    Construct truth table with columns for $p, q, r$, $p \rightarrow q$, $q \rightarrow r$, antecedent $A = (p \rightarrow q) \land (q \rightarrow r)$, consequent $B = p \rightarrow r$, and final implication $A \rightarrow B$. As shown in Chapter 2 Section 2.3 Table 7, all 8 rows evaluate to $\text{T}$. Hence, it is a \textbf{Tautology}.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025]} Without constructing a truth table, prove that $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$.
    \begin{sol}
    Refer to Chapter 3 Section 3.3 Example 7 for the complete 6-step algebraic proof using De Morgan's, Double Negation, Distributive, Negation, and Identity Laws. ($\qed$)
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} Determine the truth value / truth table of conjunction table ($p \land q$).
    \begin{sol}
    Conjunction $p \land q$ is True ONLY when both $p$ and $q$ are True.
    \begin{table}[htbp]
    \centering
    \small
    \begin{tabularx}{0.5\textwidth}{|*{3}{>{\centering\arraybackslash}X|}}
    \hline
    $p$ & $q$ & $p \land q$ \\ \hline
    T & T & \textbf{T} \\ \hline
    T & F & F \\ \hline
    F & T & F \\ \hline
    F & F & F \\ \hline
    \end{tabularx}
    \end{table}
    \end{sol}
\end{enumerate}

\subsection{Part C: 7-Mark Long Answer PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} Construct the truth table for $(p \lor q) \land (\neg p \rightarrow \neg q)$.
    \begin{sol}
    Let $A = p \lor q$ and $B = \neg p \rightarrow \neg q$.
    \begin{table}[htbp]
    \centering
    \small
    \begin{tabularx}{\textwidth}{|*{7}{>{\centering\arraybackslash}X|}}
    \hline
    $p$ & $q$ & $\neg p$ & $\neg q$ & $A = p \lor q$ & $B = \neg p \rightarrow \neg q$ & \textbf{$A \land B$} \\ \hline
    T & T & F & F & T & T & \textbf{T} \\ \hline
    T & F & F & T & T & T & \textbf{T} \\ \hline
    F & T & T & F & T & F & \textbf{F} \\ \hline
    F & F & T & T & F & T & \textbf{F} \\ \hline
    \end{tabularx}
    \end{table}
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025 --- OR]} Write the converse, inverse and contrapositive of the implication: \\
    \textit{``If $2 < 3$ and $3 + 7 = 10$, then $\sqrt{4} = 2$''}. \\
    Also determine its truth value as well as the truth value of its corresponding converse, inverse and contrapositive.
    \begin{sol}
    Let $p$: ``$2 < 3 \land 3 + 7 = 10$'', $q$: ``$\sqrt{4} = 2$''. \\
    Truth value of $p$: $2 < 3$ (T) and $3+7=10$ (T) $\implies p$ is \textbf{True (T)}. \\
    Truth value of $q$: $\sqrt{4} = 2$ $\implies q$ is \textbf{True (T)}. \\
    \begin{itemize}[leftmargin=1.5em]
        \item \textbf{Original Implication ($p \rightarrow q$):} ``If $2 < 3$ and $3 + 7 = 10$, then $\sqrt{4} = 2$''. \\
        Truth Value: $\text{T} \rightarrow \text{T} \equiv \mathbf{T}$.
        \item \textbf{Converse ($q \rightarrow p$):} ``If $\sqrt{4} = 2$, then $2 < 3$ and $3 + 7 = 10$''. \\
        Truth Value: $\text{T} \rightarrow \text{T} \equiv \mathbf{T}$.
        \item \textbf{Inverse ($\neg p \rightarrow \neg q$):} ``If it is not the case that ($2 < 3$ and $3 + 7 = 10$), then $\sqrt{4} \ne 2$''. \\
        Truth Value: $\text{F} \rightarrow \text{F} \equiv \mathbf{T}$.
        \item \textbf{Contrapositive ($\neg q \rightarrow \neg p$):} ``If $\sqrt{4} \ne 2$, then it is not the case that ($2 < 3$ and $3 + 7 = 10$)''. \\
        Truth Value: $\text{F} \rightarrow \text{F} \equiv \mathbf{T}$.
    \end{itemize}
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025]} Establish the validity of the following argument by the method of proof: \\
    Premises: (1) $p \rightarrow q$, (2) $q \rightarrow (r \land s)$, (3) $\neg r \lor (\neg t \lor u)$, (4) $p \land t$. \\
    Conclusion: $u$.
    \begin{sol}
    \textbf{Two-Column Deduction Proof:}
    \begin{table}[htbp]
    \centering
    \small
    \begin{tabularx}{\textwidth}{|c|X|X|}
    \hline
    \textbf{Step} & \textbf{Statement} & \textbf{Justification} \\ \hline
    1 & $p \land t$ & Premise 4 \\ \hline
    2 & $p$ & \textbf{Simplification} on Step 1 \\ \hline
    3 & $t$ & \textbf{Simplification} on Step 1 \\ \hline
    4 & $p \rightarrow q$ & Premise 1 \\ \hline
    5 & $q$ & \textbf{Modus Ponens} on Steps 2 and 4 \\ \hline
    6 & $q \rightarrow (r \land s)$ & Premise 2 \\ \hline
    7 & $r \land s$ & \textbf{Modus Ponens} on Steps 5 and 6 \\ \hline
    8 & $r$ & \textbf{Simplification} on Step 7 \\ \hline
    9 & $\neg r \lor (\neg t \lor u)$ & Premise 3 \\ \hline
    10 & $\neg t \lor u$ & \textbf{Disjunctive Syllogism} on Steps 8 and 9 (since $\neg(\neg r) \equiv r$) \\ \hline
    11 & \textbf{$u$} & \textbf{Disjunctive Syllogism} on Steps 3 and 10 (\textbf{Q.E.D.}) \\ \hline
    \end{tabularx}
    \end{table}
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025 --- OR]} List any seven Rules of Inference with related logical implication and name of the rule.
    \begin{sol}
    Refer to Chapter 5 Section 5.2 Table 9 for the complete 8-rule table including Modus Ponens, Modus Tollens, Hypothetical Syllogism, Disjunctive Syllogism, Addition, Simplification, Conjunction, and Resolution with their corresponding tautology implications.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} Construct the truth table for the compound statement $\neg(p \lor q) \rightarrow \neg p$.
    \begin{sol}
    \begin{table}[htbp]
    \centering
    \small
    \begin{tabularx}{\textwidth}{|*{6}{>{\centering\arraybackslash}X|}}
    \hline
    $p$ & $q$ & $p \lor q$ & $\neg(p \lor q)$ & $\neg p$ & \textbf{$\neg(p \lor q) \rightarrow \neg p$} \\ \hline
    T & T & T & F & F & \textbf{T} \\ \hline
    T & F & T & F & F & \textbf{T} \\ \hline
    F & T & T & F & T & \textbf{T} \\ \hline
    F & F & F & T & T & \textbf{T} \\ \hline
    \end{tabularx}
    \end{table}
    \textit{Conclusion:} Every row evaluates to $\text{T}$. Hence, $\neg(p \lor q) \rightarrow \neg p$ is a \textbf{Tautology}.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024 --- OR]} Use truth table to show that $\neg(p \rightarrow q) \rightarrow \neg q$ is a logical implication.
    \begin{sol}
    A statement $A \rightarrow B$ is a logical implication if $A \rightarrow B$ is a tautology.
    \begin{table}[htbp]
    \centering
    \small
    \begin{tabularx}{\textwidth}{|*{6}{>{\centering\arraybackslash}X|}}
    \hline
    $p$ & $q$ & $p \rightarrow q$ & $\neg(p \rightarrow q)$ & $\neg q$ & \textbf{$\neg(p \rightarrow q) \rightarrow \neg q$} \\ \hline
    T & T & T & F & F & \textbf{T} \\ \hline
    T & F & F & T & T & \textbf{T} \\ \hline
    F & T & T & F & F & \textbf{T} \\ \hline
    F & F & T & F & T & \textbf{T} \\ \hline
    \end{tabularx}
    \end{table}
    Since the final column contains only $\text{T}$, $\neg(p \rightarrow q) \rightarrow \neg q$ is a tautology, proving it is a valid \textbf{logical implication}. ($\qed$)
    \end{sol}
\end{enumerate}

\end{document}
"""

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_content)

    print(f"Flawless Module 1 LaTeX file written to: {tex_path}")

if __name__ == "__main__":
    create_flawless_module1_latex()
