# Colored table cells
### Color LaTeX table cells by their value

This module is useful to visually inspect large arrays of numbers. It's probably best to see this as a proof-of-concept. Ideally this functionality should be ported as a sub-module to the `tabulate` package. That would also get rid of the hacks to put the `\cellcolor` command in each cell --tabulate's normal behavior is to escape all LaTeX commands.

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
% PUT THIS IN THE PREAMBLE:
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{colortbl}
\definecolor{color1}{rgb}{0.7309496507925146,0.8394771337509155,0.9213225729325238}
\definecolor{color0}{rgb}{0.8584083129377926,0.9134486787459429,0.9645674761603861}
\definecolor{color5}{rgb}{0.04405997947734945,0.33388697645243476,0.6244521561790916}
\definecolor{color2}{rgb}{0.5356862896797704,0.7460822911823497,0.8642522187793956}
\definecolor{color3}{rgb}{0.32628989885835086,0.6186236290370717,0.8027989352450651}

% THE TABLE:
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

`generate_table` has two optional arguments: `cmap` and `fmt`. The former can be any palette from `matplotlib.cm`[1], and the latter has to be either `latex` or `latex_booktabs`.

[1] Possible values are: spring, ocean, gist_rainbow_r, hsv_r, RdBu_r, Pastel1_r, Greys_r, Blues_r, Accent, YlGn, Spectral, PRGn, gray_r, Greens, autumn_r, PuOr_r, PuOr, YlGnBu, Paired_r, Greys, rainbow, prism, YlOrBr, seismic_r, Wistia_r, brg, spectral, RdYlBu, YlOrBr_r, gist_stern, RdYlGn_r, YlGnBu_r, BuPu, PiYG, Greens_r, spring_r, bwr_r, cool, GnBu, bone_r, pink_r, hsv, YlOrRd, flag_r, Reds, Purples_r, PuBuGn_r, gist_ncar, gnuplot, winter, spectral_r, BrBG, nipy_spectral, BrBG_r, cool_r, RdYlGn, afmhot, bone, ocean_r, Pastel2_r, gist_gray_r, OrRd, RdGy, cubehelix_r, RdPu_r, binary, summer_r, CMRmap_r, PuBu, hot_r, afmhot_r, hot, winter_r, BuGn_r, autumn, PRGn_r, Oranges_r, terrain_r, gist_earth, pink, PuRd_r, bwr, binary_r, summer, RdPu, gist_heat_r, CMRmap, Dark2, Spectral_r, flag, coolwarm, RdGy_r, gist_rainbow, Reds_r, Blues, Oranges, gnuplot2, OrRd_r, Wistia, seismic, BuPu_r, gist_stern_r, Purples, PuBu_r, YlGn_r, Set2_r, RdYlBu_r, PiYG_r, Set3_r, gist_yarg, gnuplot_r, copper, Set1, Accent_r, rainbow_r, jet_r, nipy_spectral_r, Set2, RdBu, coolwarm_r, Set3, gist_gray, GnBu_r, gist_heat, Set1_r, brg_r, jet, gray, Dark2_r, PuRd, cubehelix, Paired, gist_earth_r, terrain, copper_r, YlOrRd_r, BuGn, PuBuGn, gist_ncar_r, prism_r, gnuplot2_r, Pastel1, Pastel2, gist_yarg_r
