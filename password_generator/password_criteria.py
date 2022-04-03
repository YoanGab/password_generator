from password_generator.available_characters import alphabet_lowercase, alphabet_uppercase, digits, symbols


def has_uppercase_and_lowercase(password: str) -> bool:
    return any(letter in password for letter in alphabet_lowercase) and any(
        letter in password for letter in alphabet_uppercase)


def has_digits(password: str) -> bool:
    return any(digit in password for digit in digits)


def has_symbols(password: str) -> bool:
    return any(symbol in password for symbol in symbols)


def respect_criteria(password: str, password_length, require_digits: bool,
                     require_symbols: bool, require_uppercase: bool) -> bool:
    return (
            len(password) == password_length and
            (not require_digits or has_digits(password)) and
            (not require_symbols or has_symbols(password)) and
            (not require_uppercase or has_uppercase_and_lowercase(password))
    )
