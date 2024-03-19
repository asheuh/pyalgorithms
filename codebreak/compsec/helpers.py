from string import punctuation, ascii_lowercase

def to_ignore(text):
    return text.replace(' ', '').translate(str.maketrans('', '', punctuation))

def alpha_map():
    return {c: i for i, c in enumerate(ascii_lowercase)}

def numeric_map():
    return {i: c for i, c in enumerate(ascii_lowercase)}

