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
    num = 0
    for value in values:
        if not value in value_to_colors:
            colorname, definition = latex_command(value, num, mapping)
            value_to_colors[value] = colorname
            definitions.add(definition)
            num += 1
    return definitions, value_to_colors

def latex_column_command_dict(data, mapping):
    """
    Helper function to generate commands for all values.
    """
    value_to_colors = dict()
    definitions = set()
    num = 0
    for row in data:
        for pair in row:
            index, value = pair
            if not pair in value_to_colors:
                colorname, definition = latex_command(value, num, mapping[index])
                value_to_colors[pair] = colorname
                definitions.add(definition)
                num += 1
    return definitions, value_to_colors

def modify_cell_content(content, value_to_colors):
    """
    Function to include colors in the cells containing values.
    """
    if type(content) == int or type(value) == float:
        color = value_to_colors[content]
        return ' '.join(['\cellcolor{{{}}}'.format(color), str(content)])
    else:
        return content

def modify_column_cell_content(content, value_to_colors):
    """
    Function to include colors in the cells containing values.
    Also removes the index that was used for bookkeeping.
    """
    idx, value = content
    if type(value) == int or type(value) == float:
        color = value_to_colors[content]
        return ' '.join(['\cellcolor{{{}}}'.format(color), str(value)])
    else:
        return value

def generate_table(data,
                   headers=None,
                   columns=False,
                   fmt='latex_booktabs',
                   cmap=cm.Blues):
    "Generate a LaTeX table with colored cells."
    try:
        assert fmt in {'latex','latex_booktabs'}
    except KeyError:
        raise KeyError('Use latex or latex_booktabs!')
    if columns:
        # Transpose the data so that we have columns instead of rows.
        data_cols = list(zip(*data))
        # Generate norms for each column. (Assumption: no text in the col.)
        norms = [mpl.colors.Normalize(vmin=min(col)-1, vmax=max(col)+1)
                 for col in data_cols]
        # Create dictionary from column index to color mapping.
        mappings = {i: cm.ScalarMappable(norm=norm, cmap=cmap)
                    for i,norm in enumerate(norms)}
        # Prepare the data.
        data = [list(enumerate(row)) for row in data]
        # Create a mapping from cell to color.
        definitions, value_to_colors = latex_column_command_dict(data, mappings)
        # And color the table.
        data = [[modify_column_cell_content(value, value_to_colors) for value in row]
                for row in data]
    else:
        # Get all values.
        values = [int(i) for row in data for i in row if type(i) in {int, float}]
        # Normalize them.
        norm = mpl.colors.Normalize(vmin=min(values)-1, vmax=max(values)+1)
        # Create color mapping.
        mapping = cm.ScalarMappable(norm=norm, cmap=cmap)
        # Get color definitions and cell-to-color mapping.
        definitions, value_to_colors = latex_command_dict(values, mapping)
        # Color the table.
        data = [[modify_cell_content(value, value_to_colors) for value in row]
                for row in data]
    print('% PUT THIS IN THE PREAMBLE:')
    if fmt == 'latex_booktabs':
        print('\\usepackage{booktabs}')
    print('\\usepackage{xcolor}')
    print('\\usepackage{colortbl}')
    print('\n'.join(definitions),'\n')
    print('% THE TABLE:')
    if headers:
        table = tabulate(data, headers, tablefmt=fmt)
    else:
        table = tabulate(data, tablefmt=fmt)
    table = table.replace('\\textbackslash{}','\\')
    table = table.replace('\\{','{')
    table = table.replace('\\}','}')
    print(table)
    
