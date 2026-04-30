# Scenario Examples

## 9.1 Scientific Scenarios

### 9.1.1 Mathematical Typesetting

**User:** "Write a paper with complex mathematical equations including matrices and integrals"

**LaTeX Expert:**
> **Mathematical Writing:**
> 
> ```latex
> The solution to the differential equation is given by
> \begin{equation}
> \label{eq:solution}
> y(x) = e^{\lambda x}\left(C_1 + C_2 x\right),
> \end{equation}
> where $C_1$ and $C_2$ are constants determined by initial conditions.
> 
> The matrix representation is
> \begin{equation}
> \mathbf{A} = 
> \begin{bmatrix}
> a_{11} & a_{12} & \cdots & a_{1n} \\
> a_{21} & a_{22} & \cdots & a_{2n} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n1} & a_{n2} & \cdots & a_{nn}
> \end{bmatrix}.
> \end{equation}
> 
> The volume integral becomes
> \begin{equation}
> \label{eq:volume}
> \iiint_V f(x,y,z)\,dV = \int_0^1\int_0^1\int_0^1 
> f(x,y,z)\,dx\,dy\,dz.
> \end{equation}
> ```

### 9.1.2 Thesis Writing

**User:** "Write a chemistry thesis with multiple figures, tables, and chemical structures"

**LaTeX Expert:**
> **Chemistry Thesis:**
> 
> ```latex
> \chapter{Results and Discussion}
> \label{chap:results}
> 
> \section{Spectroscopic Analysis}
> \label{sec:spectra}
> 
> The UV-Vis spectra (Figure~\ref{fig:uvvis}) show characteristic 
> absorption bands...
> 
> \begin{figure}[htbp]
> \centering
> \includegraphics[width=0.8\textwidth]{figures/uvvis_spectra.pdf}
> \caption{UV-Vis spectra of compounds 1--5 in methanol.}
> \label{fig:uvvis}
> \end{figure}
> 
> \section{Compound Characterization}
> Table~\ref{tab:compounds} lists the synthesized compounds...
> 
> \begin{table}[htbp]
> \caption{Synthesized compounds and their yields.}
> \label{tab:compounds}
> \begin{tabular}{@{}lccc@{}}
> \toprule
> Compound & Molecular Formula & MW (g/mol) & Yield (\%) \\
> \midrule
> 1 & C\textsubscript{12}H\textsubscript{18}O\textsubscript{4} & 226.27 & 78 \\
> 2 & C\textsubscript{14}H\textsubscript{20}O\textsubscript{5} & 268.31 & 65 \\
> \bottomrule
> \end{tabular}
> \end{table}
> ```

## 9.2 Data Analysis Workflows

### Multi-panel Figure
```latex
\begin{figure}[htbp]
\centering
\begin{minipage}{0.45\textwidth}
\centering
\subfloat[Control group]{
\label{fig:ctrl}
\includegraphics[width=\textwidth]{figures/ctrl.pdf}
}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\subfloat[Treatment group]{
\label{fig:treat}
\includegraphics[width=\textwidth]{figures/treat.pdf}
}
\end{minipage}
\caption{Effect of treatment on cell viability.}
\label{fig:comparison}
\end{figure}
```

### Statistical Results Table
```latex
\begin{table}[htbp]
\caption{Statistical analysis of experimental results.}
\label{tab:stats}
\begin{tabular}{@{}lSSSS@{}}
\toprule
Measure & \multicolumn{2}{c}{Control} & \multicolumn{2}{c}{Treatment} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
 & {Mean} & {SD} & {Mean} & {SD} \\
\midrule
Parameter A & 12.34 & 2.15 & 15.67 & 1.89 \\
Parameter B & 8.91 & 1.23 & 11.45 & 2.01 \\
\bottomrule
\end{tabular}
\end{table}
```

## 9.3 Publication Workflows

### ACM Digital Library Submission
```latex
\documentclass[sigconf]{acmart}

\title{Your Paper Title}

\begin{document}

\begin{abstract}
...
\end{abstract}

\keywords{keyword1, keyword2, keyword3, keyword4}

\maketitle

\section{Introduction}

\section{Background}

\section{Proposed Method}

\section{Experimental Evaluation}

\section{Related Work}

\section{Conclusion}

\acks{Acknowledgments text.}

\bibliographystyle{ACM-Reference-Format}
\bibliography{references}

\end{document}
```

### Nature Journal Submission
```latex
\documentclass{nature}

\title{Your Paper Title}

\begin{document}

\maketitle

\begin{abstract}
Abstract text (max 150 words)...
\end.Abstract}

\keywords{keyword1, keyword2, keyword3}

\section{Intro}

\section{Results}

\section{Methods}

\section{References}

\section{Online Only}
(Supplementary information)

\end{document}
```

### Using siunitx for Units
```latex
\usepackage{siunitx}

The sample was heated to \SI{150}{\celsius} for \SI{30}{\minute}.
Concentration: \SI{5.0e-6}{\mol\per\liter}
Distance: \SI{10.5 \pm 0.2}{\cm}
Mass: \SI{2.5}{\g\cancel{s}\second}

\SIlist{1; 2; 4}{\tesla}  % list formatting
\SIrange{0}{100}{\celsius}  % ranges
```
