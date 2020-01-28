def reverse(line):
    amp = line.find('&')
    col1 = line[0: amp]
    amp2 = line.find('&', amp+1)
    # col2 = line[amp + 1 : amp2]
    dub_backslash = line.find('\\')
    # for a 3 column table uncomment above and below, comment out col2 below
    # col3 = line[amp2 + 1 : dub_backslash]
    col2 = line[amp2 + 1 : dub_backslash]
    return col2 + ' & ' + col1 + ' \\'

def reverse_cols(table):
    splitable = table.split('\\')
    new_table = []
    for row in splitable:
        new_row = reverse(remove_special(row))
        new_table.append(new_row)
    for row in new_table:
        print(row)

def remove_special(string):
    if '\n' in string:
        string = string.replace('\n', '')
    if '\t' in string:
        string = string.replace('\t', '')
    return string
    
    
    
