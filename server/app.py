#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    parameter = int(parameter)
    numbers = range(parameter)
    output = ''
    for num in numbers:
        output += f'{num}\n'
    return output


@app.route("/math/<int:num1>/<operations>/<int:num2>")
def math(num1, operations, num2):
    if operations == '+':
        return str(num1 + num2)
    elif operations == '-':
        return str(num1 - num2)
    elif operations == '*':
        return str(num1 * num2)
    elif operations == 'div':
        return str(num1 / num2)
    elif operations == '%':
        return str(num1 % num2)
 



