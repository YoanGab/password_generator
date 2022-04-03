import secrets
import string

from flask import Flask, render_template, request

app = Flask(__name__)

alphabet_lowercase: str = string.ascii_lowercase
alphabet_uppercase: str = string.ascii_uppercase
digits: str = string.digits
symbols: str = string.punctuation


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


def get_possible_characters(require_digits: bool, require_symbols: bool, require_uppercase: bool) -> str:
    possible_characters: str = alphabet_lowercase
    if require_uppercase:
        possible_characters += alphabet_uppercase
    if require_digits:
        possible_characters += digits
    if require_symbols:
        possible_characters += symbols
    return possible_characters


def get_password(password_length: int, require_digits: bool, require_symbols: bool, require_uppercase: bool) -> str:
    possible_characters: str = get_possible_characters(require_digits, require_symbols, require_uppercase)
    password: str = ''
    while not respect_criteria(password, password_length, require_digits, require_symbols, require_uppercase):
        password: str = ''.join(secrets.choice(possible_characters) for _ in range(password_length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    password_length: int = int(request.form['passwordLength'])
    require_digits: bool = request.form.get('requireNumbers') is not None
    require_symbols: bool = request.form.get('requireSymbols') is not None
    require_uppercase: bool = request.form.get('requireUpperCase') is not None
    password: str = get_password(password_length, require_digits, require_symbols, require_uppercase)

    return render_template('index.html', password=password)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
