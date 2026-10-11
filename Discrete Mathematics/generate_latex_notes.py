import os

def create_latex_file():
    notes_dir = os.path.join(os.getcwd(), "Notes")
    os.makedirs(notes_dir, exist_ok=True)
    tex_path = os.path.join(notes_dir, "Module_1_Discrete_Mathematics.tex")

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
    {\huge \textbf{\textcolor{primaryblue}{MODULE 1: MATHEMATICAL LOGIC}}}\\[6pt]
    {\large \textbf{\textcolor{secondaryteal}{Complete Lecture Notes \& Previous Year Question (PYQ) Bank}}}\\[4pt]
    \textit{Strictly Prescribed Textbooks: Kenneth H. Rosen (7th Ed), Ralph P. Grimaldi (5th Ed), Thomas Koshy (2nd Ed)}
\end{center}

\vspace{10pt}

\begin{lecturnote}{MODULE OUTCOMES \& SYLLABUS SCOPE (Course Outcome CO1)}
\textbf{Course Outcome CO1:} Apply the basic concepts of mathematical logic to solve computational problems. (Duration: 16 Hours | Cognitive Level: Applying)\\[4pt]
\textbf{Module Sub-Outcomes:}
\begin{itemize}[leftmargin=1.5em, itemsep=1pt]
    \item \textbf{M1.01:} Describe the concept of propositional logic. (2 Hours, Understanding)
    \item \textbf{M1.02:} Solve problems using truth tables and logical operations. (3 Hours, Applying)
    \item \textbf{M1.03:} Prove logical equivalence, contingency, tautology and contradictions. (4 Hours, Applying)
    \item \textbf{M1.04:} Describe the concept of predicate logic. (3 Hours, Understanding)
    \item \textbf{M1.05:} Apply inference rules to solve problems. (4 Hours, Applying)
\end{itemize}
\end{lecturnote}

\vspace{10pt}
\tableofcontents
\newpage

% ==============================================================================
% SECTION 1: PROPOSITIONAL LOGIC & LOGICAL OPERATIONS
% ==============================================================================
\section{Propositional Logic \& Logical Operations}

\subsection{Concept of Propositional Logic (M1.01)}

\begin{definition}[\textbf{Proposition / Statement}]
A \textbf{proposition} (or statement) is a declarative sentence that is either \textbf{True (T)} or \textbf{False (F)}, but not both. The truth value of a proposition is denoted by $\text{T}$ (or $1$) for true and $\text{F}$ (or $0$) for false.
\end{definition}

\noindent Propositions are conventionally represented using lowercase letters such as $p, q, r, s$.

\subsubsection*{Examples of Propositions vs. Non-Propositions}
\begin{table}[h!]
\centering
\begin{tabular}{|l|c|l|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Sentence} & \color{white}\textbf{Is it a Proposition?} & \color{white}\textbf{Reason / Truth Value} \\ \hline
Kerala is a state in India. & \textbf{YES} & Declarative sentence; Truth Value = \textbf{T} \\ \hline
$2 + 3 = 7$ & \textbf{YES} & Declarative sentence; Truth Value = \textbf{F} \\ \hline
What time is it? & \textbf{NO} & Interrogative sentence (Question) \\ \hline
Solve this equation immediately! & \textbf{NO} & Imperative sentence (Command) \\ \hline
$x + 5 = 12$ & \textbf{NO} & Open sentence; truth value depends on variable $x$ \\ \hline
\end{tabular}
\caption{Classification of Sentences in Logic}
\end{table}

\subsubsection*{Atomic vs. Compound Propositions}
\begin{itemize}
    \item \textbf{Atomic (Primitive) Proposition:} A simple proposition that cannot be broken down into simpler propositions (e.g., $p$: ``It is raining'').
    \item \textbf{Compound Proposition:} Formed by combining two or more atomic propositions using \textbf{logical connectives} (e.g., $p \land q$: ``It is raining AND it is cold'').
\end{itemize}

\subsection{Logical Connectives \& Fundamental Truth Tables (M1.02)}

Logical connectives are operators used to form compound propositions. Let $p$ and $q$ be propositions.

\begin{table}[h!]
\centering
\begin{tabular}{|c|c|l|p{7cm}|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Connective} & \color{white}\textbf{Symbol} & \color{white}\textbf{Logical Name} & \color{white}\textbf{Meaning / Condition for Truth} \\ \hline
NOT & $\neg$ (or $\sim$) & Negation & Reverses truth value. True when proposition is false. \\ \hline
AND & $\land$ & Conjunction & True \textbf{ONLY when BOTH} $p$ and $q$ are True. \\ \hline
OR & $\lor$ & Disjunction (Inclusive) & True when \textbf{AT LEAST ONE} of $p, q$ is True. \\ \hline
XOR & $\oplus$ & Exclusive-OR & True when \textbf{EXACTLY ONE} of $p, q$ is True (differs). \\ \hline
IF...THEN & $\rightarrow$ & Implication / Conditional & False \textbf{ONLY when} $p$ is True and $q$ is False. \\ \hline
IFF & $\leftrightarrow$ & Biconditional & True when $p$ and $q$ have the \textbf{SAME} truth value. \\ \hline
\end{tabular}
\caption{Summary of Logical Connectives}
\end{table}

\subsubsection*{Master Truth Table for All Basic Connectives}
For $n=2$ atomic variables $p$ and $q$, there are $2^2 = 4$ possible truth assignments:

\begin{table}[h!]
\centering
\begin{tabular}{|c|c||c|c|c|c|c|c|}
\hline
\rowcolor{primaryblue} \color{white}$p$ & \color{white}$q$ & \color{white}$\neg p$ & \color{white}$p \land q$ & \color{white}$p \lor q$ & \color{white}$p \oplus q$ & \color{white}$p \rightarrow q$ & \color{white}$p \leftrightarrow q$ \\ \hline
T & T & F & \textbf{T} & \textbf{T} & F & \textbf{T} & \textbf{T} \\ \hline
T & F & F & F & \textbf{T} & \textbf{T} & \textcolor{red}{\textbf{F}} & F \\ \hline
F & T & T & F & \textbf{T} & \textbf{T} & \textbf{T} & F \\ \hline
F & F & T & F & F & F & \textbf{T} & \textbf{T} \\ \hline
\end{tabular}
\caption{Master Truth Table for Propositional Operators}
\end{table}

\begin{examtip}{LECTURER'S DEEP DIVE ON IMPLICATION ($p \rightarrow q$)}
In the implication statement $p \rightarrow q$:
\begin{itemize}
    \item $p$ is called the \textbf{Hypothesis (Antecedent / Premise)}.
    \item $q$ is called the \textbf{Conclusion (Consequent)}.
\end{itemize}
\textbf{Crucial Rule:} $p \rightarrow q$ is False \textbf{ONLY} when a True hypothesis leads to a False conclusion (Row 2). When the hypothesis $p$ is False (Rows 3 \& 4), the implication $p \rightarrow q$ is automatically \textbf{TRUE} regardless of $q$. This is known as a \textbf{vacuous truth}.
\end{examtip}

\subsection{Step-by-Step Truth Table Construction}

To construct a truth table for a complex compound proposition:
\begin{enumerate}
    \item Identify the number of distinct proposition variables $n$. The table will have $2^n$ rows.
    \item List the truth values for the atomic propositions in a systematic binary order.
    \item Create columns for sub-expressions from inside out (working through negations, parentheses, conjunctions/disjunctions, and finally implications).
\end{enumerate}

\subsubsection*{Example 1: Construct the Truth Table for $(p \lor \neg q) \rightarrow (p \land q)$}

\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Row} & \color{white}$p$ & \color{white}$q$ & \color{white}$\neg q$ & \color{white}$p \lor \neg q$ (A) & \color{white}$p \land q$ (B) & \color{white}\textbf{A $\rightarrow$ B} \\ \hline
1 & T & T & F & T & T & \textbf{T} \\ \hline
2 & T & F & T & T & F & \textcolor{red}{\textbf{F}} \\ \hline
3 & F & T & F & F & F & \textbf{T} \\ \hline
4 & F & F & T & T & F & \textcolor{red}{\textbf{F}} \\ \hline
\end{tabular}
\caption{Truth Table for $(p \lor \neg q) \rightarrow (p \land q)$}
\end{table}

\newpage

% ==============================================================================
% SECTION 2: CONDITIONAL STATEMENTS & TRUTH CLASSIFICATIONS
% ==============================================================================
\section{Conditional Statements, Implication \& Truth Classifications}

\subsection{Variants of Conditional Statements (M1.03)}

Given an original implication statement $p \rightarrow q$, three related conditional statements can be constructed:

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|l|p{5.5cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Statement Name} & \color{white}\textbf{Symbolic Form} & \color{white}\textbf{English Translation} & \color{white}\textbf{Logical Equivalence} \\ \hline
Original Implication & $p \rightarrow q$ & If $p$, then $q$ & Baseline statement \\ \hline
\textbf{Converse} & $q \rightarrow p$ & If $q$, then $p$ & Logically equivalent to Inverse ($\neg p \rightarrow \neg q$) \\ \hline
\textbf{Inverse} & $\neg p \rightarrow \neg q$ & If not $p$, then not $q$ & Logically equivalent to Converse ($q \rightarrow p$) \\ \hline
\textbf{Contrapositive} & $\mathbf{\neg q \rightarrow \neg p}$ & If not $q$, then not $p$ & \textbf{STRICTLY EQUIVALENT to $p \rightarrow q$} \\ \hline
\end{tabular}
\caption{Variants of Conditional Statements}
\end{table}

\subsubsection*{Proof of Equivalence Between Implication and Contrapositive}

\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c|c||c|c||c|c|}
\hline
\rowcolor{secondaryteal} \color{white}$p$ & \color{white}$q$ & \color{white}$\neg p$ & \color{white}$\neg q$ & \color{white}\textbf{$p \rightarrow q$} & \color{white}\textbf{$\neg q \rightarrow \neg p$} & \color{white}$q \rightarrow p$ & \color{white}$\neg p \rightarrow \neg q$ \\ \hline
T & T & F & F & \textbf{T} & \textbf{T} & T & T \\ \hline
T & F & F & T & \textbf{F} & \textbf{F} & T & T \\ \hline
F & T & T & F & \textbf{T} & \textbf{T} & F & F \\ \hline
F & F & T & T & \textbf{T} & \textbf{T} & T & T \\ \hline
\end{tabular}
\caption{Truth Table Proof of Contrapositive Equivalence}
\end{table}

\begin{lecturnote}{KEY EXAMINATION FACT}
As shown in columns 5 and 6, $p \rightarrow q$ and its contrapositive $\neg q \rightarrow \neg p$ have identical truth values in every row! Hence:
$$(p \rightarrow q) \;\equiv\; (\neg q \rightarrow \neg p)$$
However, the Converse ($q \rightarrow p$) and Inverse ($\neg p \rightarrow \neg q$) are NOT logically equivalent to the original implication!
\end{lecturnote}

\subsection{Tautology, Contradiction, and Contingency (M1.03)}

Compound propositions are categorized based on their truth values across all possible interpretations:

\begin{definition}[\textbf{Truth Classifications}]
\begin{itemize}
    \item \textbf{Tautology ($\mathbf{T}$):} A compound proposition that is \textbf{ALWAYS TRUE} under all possible truth assignments (e.g., $p \lor \neg p$).
    \item \textbf{Contradiction ($\mathbf{F}$):} A compound proposition that is \textbf{ALWAYS FALSE} under all possible truth assignments (e.g., $p \land \neg p$).
    \item \textbf{Contingency:} A compound proposition that is \textbf{NEITHER} a tautology nor a contradiction (e.g., $p \rightarrow q$).
\end{itemize}
\end{definition}

\subsubsection*{Example 2: Prove that $[(p \rightarrow q) \land (q \rightarrow r)] \rightarrow (p \rightarrow r)$ is a Tautology}

\begin{table}[h!]
\centering
\begin{tabular}{|c|c|c||c|c|c|c||c|}
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
\end{tabular}
\caption{Truth Table Proof for Hypothetical Syllogism Tautology}
\end{table}

\noindent \textit{Conclusion:} Since every entry in the final column is $\text{T}$, the statement is a \textbf{Tautology}.

\subsection{Normal Forms: DNF and CNF}

\begin{itemize}
    \item \textbf{Literal:} An atomic variable $p$ or its negation $\neg p$.
    \item \textbf{Disjunctive Normal Form (DNF / Sum-of-Products):} A disjunction ($\lor$) of minterms, where each minterm is a conjunction ($\land$) of literals. Constructed from rows in a truth table where the final output is \textbf{TRUE (T)}.
    \item \textbf{Conjunctive Normal Form (CNF / Product-of-Sums):} A conjunction ($\land$) of maxterms, where each maxterm is a disjunction ($\lor$) of literals. Constructed from rows where the final output is \textbf{FALSE (F)}.
\end{itemize}

\newpage

% ==============================================================================
% SECTION 3: LOGICAL EQUIVALENCE & DUALITY PRINCIPLE
% ==============================================================================
\section{Logical Equivalence \& Duality Principle}

\subsection{Fundamental Laws of Logical Equivalences (M1.03)}

Two compound propositions $A$ and $B$ are \textbf{logically equivalent ($A \equiv B$ or $A \Leftrightarrow B$)} if $A \leftrightarrow B$ is a tautology.

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|c|}
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
\end{tabular}
\caption{Fundamental Laws of Propositional Logic}
\end{table}

\subsection{Algebraic Proofs Without Truth Tables}

\subsubsection*{Example 3: Prove that $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$ using Laws of Logic}

\begin{proof}
Working from LHS to RHS:
\begin{align*}
\neg(p \lor (\neg p \land q)) &\equiv \neg p \land \neg(\neg p \land q) && \text{[By De Morgan's Law]} \\
&\equiv \neg p \land (\neg(\neg p) \lor \neg q) && \text{[By De Morgan's Law]} \\
&\equiv \neg p \land (p \lor \neg q) && \text{[By Double Negation Law]} \\
&\equiv (\neg p \land p) \lor (\neg p \land \neg q) && \text{[By Distributive Law]} \\
&\equiv \mathbf{F} \lor (\neg p \land \neg q) && \text{[By Negation Law: $\neg p \land p \equiv \mathbf{F}$]} \\
&\equiv \mathbf{\neg p \land \neg q} && \text{[By Identity Law: $\mathbf{F} \lor A \equiv A$]}
\end{align*}
Hence proved algebraically without constructing a truth table.
\end{proof}

\subsection{Duality Principle}

\begin{definition}[\textbf{Dual of a Proposition}]
Let $s$ be a compound proposition containing only connectives $\land, \lor,$ and $\neg$. The \textbf{dual of $s$}, denoted by $s^*$, is obtained by replacing:
\begin{itemize}
    \item Every $\land$ with $\lor$, and every $\lor$ with $\land$.
    \item Every $\mathbf{T}$ (Tautology) with $\mathbf{F}$ (Contradiction), and every $\mathbf{F}$ with $\mathbf{T}$.
\end{itemize}
\textit{Note:} Negation operators ($\neg$) remain completely unchanged!
\end{definition}

\begin{theorem}[\textbf{Principle of Duality}]
If two compound propositions $s$ and $t$ are logically equivalent ($s \equiv t$), then their duals are also logically equivalent ($s^* \equiv t^*$).
\end{theorem}

\newpage

% ==============================================================================
% SECTION 4: PREDICATE LOGIC & QUANTIFIERS
% ==============================================================================
\section{Predicate Logic \& Quantifiers}

\subsection{Predicates \& Propositional Functions (M1.04)}

Propositional logic cannot analyze statements such as \textit{``All prime numbers are odd except 2''}. Predicate logic extends propositional logic by introducing variables and predicates.

\begin{definition}[\textbf{Predicate}]
A statement of the form $P(x)$ where $x$ is the subject variable and $P$ is the predicate property assigned to $x$. The set of all valid values for $x$ is called the \textbf{Domain of Discourse (Universe $U$)}.
\end{definition}

\subsection{Quantifiers (Universal \& Existential)}

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|l|p{4cm}|p{4.5cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Quantifier Name} & \color{white}\textbf{Symbol} & \color{white}\textbf{Meaning in English} & \color{white}\textbf{When is it TRUE?} & \color{white}\textbf{When is it FALSE?} \\ \hline
\textbf{Universal Quantifier} & $\forall x \, P(x)$ & For all $x$, $P(x)$ & $P(x)$ is True for \textbf{EVERY} $x \in U$. & At least one counterexample $x \in U$ exists where $P(x)$ is False. \\ \hline
\textbf{Existential Quantifier} & $\exists x \, P(x)$ & There exists an $x$ such that $P(x)$ & $P(x)$ is True for \textbf{AT LEAST ONE} $x \in U$. & $P(x)$ is False for \textbf{EVERY SINGLE} $x \in U$. \\ \hline
\end{tabular}
\caption{Truth Conditions for Quantifiers}
\end{table}

\subsection{Negation of Quantified Statements (De Morgan's Laws)}

To negate a quantified statement, swap the quantifier type and negate the inner predicate:
$$\mathbf{\neg (\forall x \, P(x)) \;\equiv\; \exists x \, \neg P(x)}$$
$$\mathbf{\neg (\exists x \, P(x)) \;\equiv\; \forall x \, \neg P(x)}$$

\begin{examtip}{QUANTIFIER TRANSLATION ALGORITHM}
To negate a statement in English:
\begin{enumerate}
    \item Define predicate symbols $P(x), Q(x)$ and specify domain $U$.
    \item Express the original English statement in symbolic predicate logic.
    \item Apply De Morgan's Law for quantifiers to push negation inside.
    \item Translate the simplified symbolic formula back to natural English.
\end{enumerate}
\end{examtip}

\subsection{Nested Quantifiers}

When multiple quantifiers are present, \textbf{the order of quantifiers matters!}
$$\forall x \, \exists y \, P(x, y) \;\;\not\equiv\;\; \exists y \, \forall x \, P(x, y)$$

\begin{table}[h!]
\centering
\begin{tabular}{|l|p{6cm}|p{6cm}|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Statement} & \color{white}\textbf{When is it TRUE?} & \color{white}\textbf{When is it FALSE?} \\ \hline
$\forall x \, \forall y \, P(x, y)$ & $P(x, y)$ is True for \textbf{every pair} $(x, y)$. & There is at least one pair $(x, y)$ where $P(x, y)$ is False. \\ \hline
$\forall x \, \exists y \, P(x, y)$ & For \textbf{every $x$}, there is \textbf{at least one $y$} (which may depend on $x$) making $P(x,y)$ True. & There is some $x$ for which no $y$ makes $P(x,y)$ True. \\ \hline
$\exists x \, \forall y \, P(x, y)$ & There is \textbf{at least one fixed $x$} that works for \textbf{every single $y$}. & For every $x$, there is at least one $y$ where $P(x,y)$ fails. \\ \hline
$\exists x \, \exists y \, P(x, y)$ & There is \textbf{at least one pair} $(x, y)$ for which $P(x, y)$ is True. & $P(x, y)$ is False for \textbf{every possible pair} $(x, y)$. \\ \hline
\end{tabular}
\caption{Nested Quantifier Truth Conditions}
\end{table}

\newpage

% ==============================================================================
% SECTION 5: RULES OF INFERENCE & NATURAL DEDUCTION
% ==============================================================================
\section{Rules of Inference \& Natural Deduction}

\subsection{Logical Arguments \& Validity (M1.05)}

An \textbf{argument} consists of a sequence of premises $P_1, P_2, \dots, P_k$ and a conclusion $C$. An argument is \textbf{VALID} if and only if:
$$(P_1 \land P_2 \land \dots \land P_k) \;\rightarrow\; C \quad \text{is a \textbf{Tautology}}.$$

\subsection{Rules of Inference for Propositional Logic}

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|c|l|}
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
\end{tabular}
\caption{Primary Rules of Inference for Propositional Logic}
\end{table}

\subsection{Rules of Inference for Quantified Statements}

\begin{table}[h!]
\centering
\begin{tabular}{|l|c|c|p{6cm}|}
\hline
\rowcolor{secondaryteal} \color{white}\textbf{Rule Name} & \color{white}\textbf{Premise} & \color{white}\textbf{Conclusion} & \color{white}\textbf{Condition / Restriction} \\ \hline
\textbf{Universal Instantiation (UI)} & $\forall x \, P(x)$ & $\therefore P(c)$ & $c$ is ANY element in domain $U$. \\ \hline
\textbf{Universal Generalization (UG)} & $P(c)$ for arbitrary $c$ & $\therefore \forall x \, P(x)$ & $c$ MUST be an \textbf{arbitrary} element. \\ \hline
\textbf{Existential Instantiation (EI)} & $\exists x \, P(x)$ & $\therefore P(c)$ & $c$ is a \textbf{SOME specific} element (must be new!). \\ \hline
\textbf{Existential Generalization (EG)} & $P(c)$ for known $c$ & $\therefore \exists x \, P(x)$ & Holds if $P(c)$ is true for a known element $c$. \\ \hline
\end{tabular}
\caption{Rules of Inference for Quantified Statements}
\end{table}

\subsection{Formal Two-Column Proof Example}

\subsubsection*{Example 4: Prove conclusion $s$ given premises: (1) $p \rightarrow q$, (2) $q \rightarrow r$, (3) $\neg r$, and (4) $p \lor s$}

\begin{table}[h!]
\centering
\begin{tabular}{|c|l|l|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Step} & \color{white}\textbf{Statement} & \color{white}\textbf{Justification / Rule Used} \\ \hline
1 & $p \rightarrow q$ & Premise 1 \\ \hline
2 & $q \rightarrow r$ & Premise 2 \\ \hline
3 & $p \rightarrow r$ & \textbf{Hypothetical Syllogism} on Steps 1 and 2 \\ \hline
4 & $\neg r$ & Premise 3 \\ \hline
5 & $\neg p$ & \textbf{Modus Tollens} on Steps 3 and 4 \\ \hline
6 & $p \lor s$ & Premise 4 \\ \hline
7 & \textbf{$s$} & \textbf{Disjunctive Syllogism} on Steps 5 and 6 (\textbf{Q.E.D.}) \\ \hline
\end{tabular}
\caption{Two-Column Natural Deduction Proof}
\end{table}

\newpage

% ==============================================================================
% SECTION 6: METHODS OF PROOF & RESOLUTION PRINCIPLE
% ==============================================================================
\section{Methods of Proof \& Resolution Principle}

\subsection{Standard Methods of Proof (M1.05)}

\begin{table}[h!]
\centering
\begin{tabular}{|l|l|l|p{5.5cm}|}
\hline
\rowcolor{primaryblue} \color{white}\textbf{Proof Method} & \color{white}\textbf{Assumption Made} & \color{white}\textbf{Goal to Demonstrate} & \color{white}\textbf{Key Strategy / Logic} \\ \hline
\textbf{Direct Proof} & Assume $p$ is True & Show $q$ is True & Use axioms, definitions, and logic directly. \\ \hline
\textbf{Proof by Contraposition} & Assume $\neg q$ is True & Show $\neg p$ is True & Uses logical equivalence $(p \rightarrow q) \equiv (\neg q \rightarrow \neg p)$. \\ \hline
\textbf{Proof by Contradiction} & Assume $\neg p$ (or $p \land \neg q$) & Derive contradiction $r \land \neg r$ ($\mathbf{F}$) & If assumption leads to non-sense, original statement is True! \\ \hline
\textbf{Proof by Cases} & Assume $p = p_1 \lor p_2 \lor \dots \lor p_k$ & Show $p_i \rightarrow q$ for all $i$ & Exhaustive evaluation of all distinct scenarios. \\ \hline
\end{tabular}
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
\begin{itemize}
    \item \textbf{Clause:} A disjunction ($\lor$) of literals, e.g., $C_1 = p \lor \neg q \lor r$.
    \item \textbf{Resolvent Rule:} Given two clauses containing complementary literals ($p$ and $\neg p$):
    $$\frac{p \lor C, \quad \neg p \lor D}{\therefore C \lor D} \quad \text{(Resolvent)}$$
\end{itemize}
\end{definition}

\subsubsection*{Resolution Refutation Algorithm (Proof by Contradiction):}
\begin{enumerate}
    \item Convert all premises into Clause Form (CNF disjunctions).
    \item Negate the conclusion to be proven and convert it into clause form.
    \item Add the negated conclusion clause to the set of premise clauses.
    \item Iteratively apply the resolution rule to pairs of clauses to generate new resolvent clauses.
    \item If the \textbf{Empty Clause ($\square$ or $\mathbf{F}$)} is derived, a contradiction is established, proving the original conclusion VALID!
\end{enumerate}

\newpage

% ==============================================================================
% SECTION 7: UNIVERSITY EXAM QUESTION BANK & SOLVED PYQS
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
    Construct truth table with columns for $p, q, r$, $p \rightarrow q$, $q \rightarrow r$, antecedent $A = (p \rightarrow q) \land (q \rightarrow r)$, consequent $B = p \rightarrow r$, and final implication $A \rightarrow B$. As shown in Section 2.2 Table 7, all 8 rows evaluate to $\text{T}$. Hence, it is a \textbf{Tautology}.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025]} Without constructing a truth table, prove that $\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q$.
    \begin{sol}
    Refer to Section 3.2 Example 3 for the complete 6-step algebraic proof using De Morgan's, Double Negation, Distributive, Negation, and Identity Laws. ($\qed$)
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} Determine the truth value / truth table of conjunction table ($p \land q$).
    \begin{sol}
    Conjunction $p \land q$ is True ONLY when both $p$ and $q$ are True.
    \begin{table}[h!]
    \centering
    \begin{tabular}{|c|c|c|}
    \hline
    $p$ & $q$ & $p \land q$ \\ \hline
    T & T & \textbf{T} \\ \hline
    T & F & F \\ \hline
    F & T & F \\ \hline
    F & F & F \\ \hline
    \end{tabular}
    \end{table}
    \end{sol}
\end{enumerate}

\subsection{Part C: 7-Mark Long Answer PYQs (With Solutions)}

\begin{enumerate}[leftmargin=1.5em, label=\textbf{Q\arabic*:}]
    \item \textbf{[Nov 2025]} Construct the truth table for $(p \lor q) \land (\neg p \rightarrow \neg q)$.
    \begin{sol}
    Let $A = p \lor q$ and $B = \neg p \rightarrow \neg q$.
    \begin{table}[h!]
    \centering
    \begin{tabular}{|c|c|c|c|c|c|c|}
    \hline
    $p$ & $q$ & $\neg p$ & $\neg q$ & $A = p \lor q$ & $B = \neg p \rightarrow \neg q$ & \textbf{$A \land B$} \\ \hline
    T & T & F & F & T & T & \textbf{T} \\ \hline
    T & F & F & T & T & T & \textbf{T} \\ \hline
    F & T & T & F & T & F & \textbf{F} \\ \hline
    F & F & T & T & F & T & \textbf{F} \\ \hline
    \end{tabular}
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
    \begin{itemize}
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
    \begin{table}[h!]
    \centering
    \begin{tabular}{|c|l|l|}
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
    \end{tabular}
    \end{table}
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2025 --- OR]} List any seven Rules of Inference with related logical implication and name of the rule.
    \begin{sol}
    Refer to Section 5.2 Table 9 for the complete 8-rule table including Modus Ponens, Modus Tollens, Hypothetical Syllogism, Disjunctive Syllogism, Addition, Simplification, Conjunction, and Resolution with their corresponding tautology implications.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024]} Construct the truth table for the compound statement $\neg(p \lor q) \rightarrow \neg p$.
    \begin{sol}
    \begin{table}[h!]
    \centering
    \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $p$ & $q$ & $p \lor q$ & $\neg(p \lor q)$ & $\neg p$ & \textbf{$\neg(p \lor q) \rightarrow \neg p$} \\ \hline
    T & T & T & F & F & \textbf{T} \\ \hline
    T & F & T & F & F & \textbf{T} \\ \hline
    F & T & T & F & T & \textbf{T} \\ \hline
    F & F & F & T & T & \textbf{T} \\ \hline
    \end{tabular}
    \end{table}
    \textit{Conclusion:} Every row evaluates to $\text{T}$. Hence, $\neg(p \lor q) \rightarrow \neg p$ is a \textbf{Tautology}.
    \end{sol}
    \vspace{6pt}

    \item \textbf{[Nov 2024 --- OR]} Use truth table to show that $\neg(p \rightarrow q) \rightarrow \neg q$ is a logical implication.
    \begin{sol}
    A statement $A \rightarrow B$ is a logical implication if $A \rightarrow B$ is a tautology.
    \begin{table}[h!]
    \centering
    \begin{tabular}{|c|c|c|c|c|c|}
    \hline
    $p$ & $q$ & $p \rightarrow q$ & $\neg(p \rightarrow q)$ & $\neg q$ & \textbf{$\neg(p \rightarrow q) \rightarrow \neg q$} \\ \hline
    T & T & T & F & F & \textbf{T} \\ \hline
    T & F & F & T & T & \textbf{T} \\ \hline
    F & T & T & F & F & \textbf{T} \\ \hline
    F & F & T & F & T & \textbf{T} \\ \hline
    \end{tabular}
    \end{table}
    Since the final column contains only $\text{T}$, $\neg(p \rightarrow q) \rightarrow \neg q$ is a tautology, proving it is a valid \textbf{logical implication}. ($\qed$)
    \end{sol}
\end{enumerate}

\end{document}
"""

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex_content)

    print(f"Complete LaTeX file successfully written to: {tex_path}")

if __name__ == "__main__":
    create_latex_file()
