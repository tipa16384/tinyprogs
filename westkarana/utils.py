filename = 'westkarana.md'


def consume(l):
    state = 0
    stuff = None

    for c in l:
        if state == 0:
            if c.isdigit():
                state = 1
                stuff = int(c)
            elif c == "'":
                state = 2
                stuff = ''
        elif state == 1:
            if c.isdigit():
                stuff = stuff * 10 + int(c)
            elif stuff is not None:
                yield stuff
                stuff = None
                state = 0
        elif state == 2:
            if c == '\\':
                state = 3
            elif c == "'":
                yield stuff
                stuff = None
                state = 0
            else:
                stuff += c
        elif state == 3:
            if c == "'":
                stuff += "'"
            else:
                stuff += "\\" + c
            state = 2

    if stuff:
        yield stuff


def mangle(l):
    l = l.replace('tipa@westkarana.com', 'brendahol@gmail.com')
    l = l.replace('http://westkarana.com', 'https://chasingdings.com')
    return l.replace('\\r', '').replace('\\n\\n\\n\\n', '\n\n').replace('\\n', '\n')
