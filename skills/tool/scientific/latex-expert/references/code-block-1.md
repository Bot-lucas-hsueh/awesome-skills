# latex Example

```
% main.tex
\documentclass[11pt, a4paper, twoside]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{siunitx}
\usepackage{microtype}

% Bibliography
\usepackage[backend=biber, style=apa, maxnames=5]{biblatex}
\addbibresource{refs.bib}

% Custom commands
\newcommand{\R}{\mathbb{R}}
\DeclareMathOperator*{\argmax}{arg\,max}

% Title
\title{Your Paper Title Here}
\author{Author Name\inst{1} \and Co-Author\inst{2}}
\institute{\inst{1} University A \and \inst{2} University B}

\begin{document}
\maketitle

\begin{abstract}
Your abstract here. Keep it between 150-250 words.
\end{abstract}

\keywords{keyword1, keyword2, keyword3}

\section{Introduction}
\label{sec:intro}

\section{Related Work}
\label{sec:related}

\section{Methodology}
\label{sec:method}

\section{Results}
\label{sec:results}

\section{Conclusion}
\label{sec:conclusion}

\printbibliography

\appendix
\section{Additional Material}
\label{app:extra}
\end{document}
```
