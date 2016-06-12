def _extract_func_name(line):
    left = line.index("def ") + 4
    while line[left] == ' ':
        left += 1
    if line.find("(") == -1:
        return None
    else:
        right = line.index("(")
    return line[left:right]

def _extract_class_name(line):
    left = line.index("class") + 6
    right = 0
    if line.find("(") != -1:
        right = line.index("(")
    else:
        right = line.index(":")
    return line[left:right]

def _extract_args(line):
    if line.find("(") != -1 and line.find(")") != -1:
        left = line.index("(") + 1
        while left == " ":
            left += 1
        right = line.index(")")
        line = line[left:right]

    elif line.find("(") != -1:
        left = line.index("(") + 1
        line = line[left:]

    elif line.find(")") != -1:
        right = line.index(")")
        line = line[:right]
        
    args = line.split(",")
    for arg in args:
        arg = arg.replace(" ", "")
    return args
