import matplotlib as mpl
import matplotlib.cm as cm
from tabulate import tabulate

def latex_command(value, num, mapping):
    """
    Helper function to generate a color name and definition for a given value.
    Num is used to identify different colors. Mapping is the mapping generated in
    generate_table
    """
    r,g,b,a = mapping.to_rgba(value)
    colorname = 'color' + str(num)
    definition = "\definecolor{{{colorname}}}{{rgb}}{{{r},{g},{b}}}".format(colorname = colorname,
                                                                            r = r,
                                                                            g = g,
                                                                            b = b)
    return colorname, definition

def latex_command_dict(values, mapping):
    """
    Helper function to generate commands for all values.
    """
    value_to_colors = dict()
    definitions = set()
    for num, value in enumerate(values):
        if not value in value_to_colors:
            colorname, definition = latex_command(value, num, mapping)
            value_to_colors[value] = colorname
            definitions.add(definition)
    return definitions, value_to_colors

def modify_cell_content(content, value_to_colors):
    """
    Function to include colors in the cells containing values.
    """
    if type(1) == int or content.isdigit():
        color = value_to_colors[content]
        return ' '.join(['\cellcolor{{{}}}'.format(color), str(content)])
    else:
        return content

def generate_table(data, headers, fmt='latex_booktabs', cmap=cm.Blues):
    "Generate a LaTeX table with colored cells."
    try:
        assert fmt in {'latex','latex_booktabs'}
    except KeyError:
        raise KeyError('Use latex or latex_booktabs!')
    
    values = [int(i) for row in data for i in row if type(i) == int or i.isdigit()]
    norm = mpl.colors.Normalize(vmin=min(values)-1, vmax=max(values)+1)
    mapping = cm.ScalarMappable(norm=norm, cmap=cmap)
    definitions, value_to_colors = latex_command_dict(values, mapping)
    print('PUT THIS IN THE PREAMBLE:')
    if fmt == 'latex_booktabs':
        print('\\usepackage[table]{booktabs}')
    print('\\usepackage{xcolor}')
    print('\\usepackage{colortbl}')
    print('\n'.join(definitions),'\n')
    data = [[modify_cell_content(value, value_to_colors) for value in row]
            for row in data]
    print('THE TABLE:')
    if headers:
        table = tabulate(data, headers, tablefmt=fmt)
    else:
        table = tabulate(data, tablefmt=fmt)
    table = table.replace('\\textbackslash{}','\\')
    table = table.replace('\\{','{')
    table = table.replace('\\}','}')
    print(table)
    
