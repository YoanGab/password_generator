import string

alphabet_lowercase: str = string.ascii_lowercase
alphabet_uppercase: str = string.ascii_uppercase
digits: str = string.digits
symbols: str = string.punctuation


def get_possible_characters(require_digits: bool, require_symbols: bool, require_uppercase: bool) -> str:
    possible_characters: str = alphabet_lowercase
    if require_uppercase:
        possible_characters += alphabet_uppercase
    if require_digits:
        possible_characters += digits
    if require_symbols:
        possible_characters += symbols
    return possible_characters
