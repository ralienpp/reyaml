import yaml


def load(raw):
    '''Parses a YAML string, tolerating comments and inline comments, as well as
    warning you about mixed tabs and spaces'''
    lines = []
    spaces = False
    tabs = False

    for line in raw.splitlines():
        if line.lstrip().startswith('#'):
            continue # a line that is a comment (doesn't begin with whitespace)
        if 0 == len( line.strip() ):
            continue # this is an empty line, skip it
        if line.startswith('\t'):
            tabs = True
            line = line.replace('\t', '    ')
        elif line.startswith('  '):
            spaces = True
        if spaces and tabs:
            error = 'You mixed tabs and spaces. Use one or the other, but not both. Problematic line:\n'
            error += line
            raise SyntaxError(error)

        #find lines that contain an unquoted URL with an anchor
        if '#' in line:
            for part in line.split():
                if '://' in part and not part[0] in ['\'', '\"']:
                    error = 'You have a line with a URL and a comment, the comment could be a URL anchor.\n'
                    error += 'To avoid ambiguities, quote such URLs. Problematic line:\n'
                    error += line
                    raise SyntaxError(error)
        lines.append(line)

    return yaml.load('\n'.join(lines), Loader=yaml.SafeLoader)


def load_from_file(path):
    '''Load a YAML file and return its contents as a dictionary'''
    with open(path, 'r') as f:
        raw = f.read()
        return load(raw)
