# Common Pitfalls & Anti-Patterns

## 10.1 Common LaTeX Mistakes

| # | Anti-Pattern | Severity | Impact | Quick Fix |
|---|--------------|----------|--------|-----------|
| 1 | **Missing braces** | 🔴 High | Wrong kerning | Use `{...}` for all macros |
| 2 | **Overfull/underfull boxes** | 🔴 High | Bad line breaking | Adjust `emergencystretch` |
| 3 | **Non-breaking spaces misused** | 🟡 Medium | Bad line breaks | `~` vs space |
| 4 | **Equation numbering** | 🟡 Medium | Wrong numbers | `\label{}` before `\ref{}` |
| 5 | **Floating specifier order** | 🟡 Medium | Placement issues | `[htbp]` order matters |
| 6 | **File encoding** | 🟡 Medium | Special characters | Use UTF-8 consistently |

### Examples

```latex
% WRONG: Missing braces
\alpha \mu s  % Will render as αμs instead of αμs
\C   % May cause issues

% CORRECT: Proper braces
\textalpha\ \textmu s
\C{}  % or just \c{C}

% WRONG: Bad line breaks
Figure 1 shows that the parameter (see equation 10)
increases with temperature.

% CORRECT: Non-breaking space
Figure~1 shows that the parameter (see equation~\ref{eq:10})
increases with temperature.

% WRONG: Overfull hbox
This is some text that is too long to fit on one line and 
will cause an overfull hbox warning.

% CORRECT: Adjust settings
\emergencystretch=3em
\tolerance=200
```

## 10.2 Math Typesetting Errors

| # | Anti-Pattern | Severity | Correct Usage |
|---|--------------|----------|---------------|
| 1 | **Double dollars** | 🔴 High | `\[ ... \]` or `equation` |
| 2 | **Text in math mode** | 🟡 Medium | `\text{...}` or `\mathrm{...}` |
| 3 | **Multiscript spacing** | 🟡 Medium | `x_i+1` vs `x_{i+1}` |
| 4 | **Differential d** | 🟡 Medium | `\,d` for spacing |
| 5 | **Bold math** | 🟡 Medium | `\mathbf{}` vs `\bm{}` |

### Examples

```latex
% WRONG: Double dollars
$$f(x) = x^2 + 1$$  % Deprecated

% CORRECT: Display equation
\begin{equation}
\label{eq:quadratic}
f(x) = x^2 + 1
\end{equation}

% WRONG: Text without proper command
$x = 5 where x is the variable$  % Wrong

% CORRECT: Text in math
$x = 5$, where $x$ is the variable
% Or: $x = 5\ \text{where}\ x\ \text{is the variable}$

% WRONG: No spacing in differential
\int x dx  % No space

% CORRECT: Thin space before d
\int x \, dx
\int_0^1 x^2 \, dx

% WRONG: Using textbf for bold math
\textbf{A}  % Wrong for vectors

% CORRECT: Use bm or bmatrix
\mathbf{A}  % Upright bold
\boldsymbol{\alpha}  % Italic bold symbols
bmatrix{A}  % For matrices
```

## 10.3 Table Formatting Issues

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Vertical lines** | 🟡 Medium | Use booktabs, avoid vertical |
| 2 | **No alignment** | 🟡 Medium | Use `S` column from siunitx |
| 3 | **Horizontal crowding** | 🟡 Medium | Add `@{\ extracollskip }` |
| 4 | **Caption placement** | 🟡 Medium | Caption above, notes below |

### Examples

```latex
% WRONG: Vertical lines, poor formatting
\begin{tabular}{|l|l|l|}
\hline
Column 1 & Column 2 & Column 3 \\
\hline
Data 1 & Data 2 & Data 3 \\
\hline
\end{tabular}

% CORRECT: Professional table
\begin{table}[htbp]
\caption{Experimental results.}
\label{tab:results}
\begin{tabular}{@{}lSSS@{}}
\toprule
Condition & \multicolumn{1}{c}{Trial 1} & \multicolumn{1}{c}{Trial 2} & \multicolumn{1}{c}{Trial 3} \\
\midrule
Control & 10.23 & 9.87 & 10.45 \\
Treatment & 15.67 & 14.89 & 16.12 \\
\bottomrule
\end{tabular}
\end{table}

% For numbers with units:
\usepackage{siunitx}
\begin{tabular}{@{}lS[table-format=2.2]S[table-format=2.2]@{}}
% Numbers will align on decimal point
```

## 10.4 Bibliography Anti-Patterns

```
❌ Mixing BibTeX styles (plain, alpha, unsrt)
✅ Choose one style, use consistently

❌ Duplicate entries in .bib file
✅ Use JabRef or BibTeX managing tools

❌ Missing fields required by style
✅ Check required/optional fields for each entry type

❌ Non-standard citation commands
✅ \cite{}, \citep{}, \citet{} (from natbib)

❌ Special characters in .bib without escaping
✅ Use \{}, \&, etc. or use biber with unicode
```

### Correct BibTeX Entry
```bibtex
@article{smith2023example,
  author  = {Smith, John and Doe, Jane},
  title   = {A Study on Example Citations},
  journal = {Journal of Examples},
  year    = {2023},
  volume  = {15},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1234/jex.2023.001},
}
```

## 10.5 Build System Issues

```bash
# WRONG: Single pdflatex run with bibliography
pdflatex main.tex
# (Missing references, citations)

# CORRECT: Complete build sequence
pdflatex main.tex      # First pass
biber main.bcf        # Process bibliography (or bibtex)
pdflatex main.tex      # Second pass
pdflatex main.tex      # Third pass (cross-refs stable)

# Using latexmk (automated)
latexmk -pdf main.tex

# Using VS Code LaTeX Workshop
# Already configured for multiple passes
```
