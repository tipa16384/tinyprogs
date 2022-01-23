def cnv_win_to_cyg_path(path):
    """
    Converts a windows path to a cygwin path.
    """
    path = path.replace('\\', '/')
    if path[1] == ':':
        path = '/cygdrive/' + path[0].lower() + path[2:]
    return path

if __name__ == "__main__":
    assert '/cygdrive/c/Users/joe/Documents/' == cnv_win_to_cyg_path('C:/Users/joe/Documents/')
