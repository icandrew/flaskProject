from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Micaela"):
    if name:
        return f"Hello {name}"
    else:
        return "Hello"


@app.route('/<celsius_str>')
def celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = (celsius * 9 / 5) + 32
        return f"<h1>{fahrenheit:.2f} Fahrenheit</h1>"
    except ValueError:
        return "Invalid input. Please enter a valid Celsius value."


if __name__ == '__main__':
    app.run()
