# Standards & Reference

## 7.1 Official Documentation

- [LaTeX Project](https://www.latex-project.org/)
- [LaTeX Documentation](https://latexref.xyz/)
- [CTAN - Comprehensive TeX Archive](https://www.ctan.org/)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [TeX Stack Exchange](https://tex.stackexchange.com/)
- [ memoir class manual](https://ctan.org/pkg/memoir)

## 7.2 Reference Tables

### Essential Packages

| Package | Purpose | Load Order |
|---------|---------|------------|
| `amsmath` | Math equations | After font packages |
| `amssymb` | Math symbols | After amsmath |
| `bm` | Bold math symbols | After amsmath |
| `geometry` | Page margins | Any |
| `graphicx` | Include images | Any |
| `hyperref` | Hyperlinks | Last (most cases) |
| `biblatex` | Bibliography | Any |
| `booktabs` | Professional tables | Any |
| `siunitx` | Units and numbers | Any |
| `microtype` | Typography tweaks | After font packages |

### Mathematical Environments

| Environment | Use Case | Code |
|-------------|----------|------|
| `equation` | Single equation, numbered | `\[ ... \]` |
| `align` | Multiple aligned equations | `&` for alignment |
| `gather` | Centered equations, no align | `\\` for breaks |
| `multline` | Long single equation | First line left, last right |
| `split` | Sub-equation alignment | Inside equation |
| `cases` | Piecewise functions | |

### Document Classes

| Class | Use Case | Key Options |
|-------|----------|-------------|
| `article` | Short papers, reports | `11pt`, `a4paper`, `oneside` |
| `report` | Theses, longer documents | `chapter` option |
| `book` | Books, dissertations | `twoside`, `openright` |
| `memoir` | Flexible thesis/book | Built-in many features |
| `IEEEtran` | IEEE publications | `conference`, `journal` |
| `lncs` | Springer conferences | |

## 7.3 Common Patterns

### Document Structure
```latex
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{margin=1in}

\title{Your Title Here}
\author{Author Name\thanks{Institution}}
\date{\today}

\begin{document}
\maketitle
\begin{abstract}
Your abstract here.
\end{abstract}

\section{Introduction}
\label{sec:intro}

\section{Methods}
\label{sec:methods}

\section{Results}
\label{sec:results}

\section{Conclusion}
\label{sec:conclusion}

\bibliographystyle{plain}
\bibliography{references}
\end{document}
```

### Table of Contents
```latex
\newpage
\tableofcontents
\newpage
\listoffigures
\listoftables
\newpage
```

### Cross-references
```latex
\section{Background}
\label{sec:background}

As shown in Section~\ref{sec:background}...

Figure~\ref{fig:example} shows...

Table~\ref{tab:results} summarizes...

Equation~\ref{eq:main} defines...
```

## 7.4 Version Compatibility

| LaTeX Distribution | Release Year | Key Features |
|--------------------|--------------|--------------|
| TeX Live 2020 | 2020 | expl3 stable |
| TeX Live 2022 | 2022 | L3 kernel default |
| TeX Live 2023 | 2023 | UTF-8 default |
| TeX Live 2024 | 2024 | Current stable |

| Package | Min Version | Notes |
|---------|-------------|-------|
| `biblatex` | 3.18 | Biber backend default |
| `siunitx` | 3.0 | Redesigned syntax |
| `hyperref` | 7.00 | PDF/A support |
| `fontspec` | 2.7 | Unicode math |
| `graphicx` | 2020 | SVG support |
