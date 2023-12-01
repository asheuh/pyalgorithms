def read_data(filename: str, parser=str, sep='\n') -> list:
    sections = open(filename).read().rstrip().split(sep)
    return [parser(section) for section in sections]

