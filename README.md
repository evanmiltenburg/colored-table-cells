# Colored table cells
### Color LaTeX table cells by their value

## Requirements
* Matplotlib
* Tabulate

## How to use this script
```python
from colored_table_cells import generate_table
generate_table([[1,2],[3,4],[2,6]],['a','b'])
```

Output:

```latex
PUT THIS IN THE PREAMBLE:
\usepackage[table]{booktabs}
\usepackage{xcolor}
\usepackage{colortbl}
\definecolor{color1}{rgb}{0.7309496507925146,0.8394771337509155,0.9213225729325238}
\definecolor{color0}{rgb}{0.8584083129377926,0.9134486787459429,0.9645674761603861}
\definecolor{color5}{rgb}{0.04405997947734945,0.33388697645243476,0.6244521561790916}
\definecolor{color2}{rgb}{0.5356862896797704,0.7460822911823497,0.8642522187793956}
\definecolor{color3}{rgb}{0.32628989885835086,0.6186236290370717,0.8027989352450651}

THE TABLE:
\begin{tabular}{ll}
\toprule
 a                    & b                    \\
\midrule
 \cellcolor{color0} 1 & \cellcolor{color1} 2 \\
 \cellcolor{color2} 3 & \cellcolor{color3} 4 \\
 \cellcolor{color1} 2 & \cellcolor{color5} 6 \\
\bottomrule
\end{tabular}
```
