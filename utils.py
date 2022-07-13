import string


def make_safe(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)


def list_to_string(raw):
    out = ''
    for i in range(0, len(raw)-1):
        out += f'{raw[i]}\n'
    out += f'{raw[-1]}'
    return out
