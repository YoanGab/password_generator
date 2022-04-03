from flask import Flask, render_template, request

from password_generator import generate_password

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    password_length: int = int(request.form['passwordLength'])
    require_digits: bool = request.form.get('requireNumbers') is not None
    require_symbols: bool = request.form.get('requireSymbols') is not None
    require_uppercase: bool = request.form.get('requireUpperCase') is not None
    password: str = generate_password(
        password_length=password_length,
        require_digits=require_digits,
        require_symbols=require_symbols,
        require_uppercase=require_uppercase
    )

    return render_template('index.html', password=password)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
