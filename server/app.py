#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5550, debug=True)

@app.route('/')
def index():
    return '<h1>"Python Operations with Flask Routing and Views".</h1>'

# Additional code for String Print function
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'

# Additional code for Count function
@app.route('/count/<int:parameter>')
def count(parameter):
    return '<br>'.join(str(i) for i in range(1, parameter+1))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Dictionary of operations
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "div": lambda a, b: a / b,
        "%": lambda a, b: a % b
    }

    # Check if the operation is valid
    if operation not in operations:
        return 'Invalid operation. Use one of +, -, *, div, % .', 400

    # Perform the operation and return the result
    result = operations[operation](num1, num2)
    return str(result)