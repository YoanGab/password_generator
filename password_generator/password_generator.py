import secrets

from password_generator.available_characters import get_possible_characters
from password_generator.password_criteria import respect_criteria


def generate_password(password_length: int, require_digits: bool, require_symbols: bool, require_uppercase: bool) -> str:
    possible_characters: str = get_possible_characters(require_digits, require_symbols, require_uppercase)
    password: str = ''
    while not respect_criteria(password, password_length, require_digits, require_symbols, require_uppercase):
        password: str = ''.join(secrets.choice(possible_characters) for _ in range(password_length))
    return password
