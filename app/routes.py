from flask import render_template
from app import app, db
import math

from app.util import request_log


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/pow/b=<base>/e=<exponent>/m=<modulus>', methods=['GET'])
@app.route('/pow/b=<base>/e=<exponent>', methods=['GET'])
def power(base, exponent, modulus='missing'):
    if modulus == 'missing':
        result = 'pow({}, {}) = {}'.format(base, exponent, pow(int(base), int(exponent)))
        request_log('pow', str([base, exponent]), result)
        return '<a href="http://127.0.0.1:5000">Back</a><br><br>' + result

    result = 'pow({}, {}, {}) = {}'.format(base, exponent, modulus, pow(int(base), int(exponent), int(modulus)))
    request_log('pow', str([base, exponent, modulus]), result)
    return '<a href="http://127.0.0.1:5000">Back</a><br><br>' + result + ''


@app.route('/fib/n=<value>', methods=['GET'])
def fib(value):
    n = int(value)
    lst = []

    def fib(n):
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return
            yield a
            a, b = b, a + b
            counter += 1

    for x in fib(n - 1):
        lst.append(x)
    result = 'Element {} in Fibbonaci sequence is: {}'.format(n, lst[-1])
    request_log('fact', n, result)
    return '<a href="http://127.0.0.1:5000">Back</a><br><br>' + result + ''


@app.route('/fact/n=<value>', methods=['GET'])
def fact(value):
    n = int(value)
    result = 'factorial({}) = {}'.format(n, str(math.factorial(n)))
    request_log('fact', n, result)
    return '<a href="http://127.0.0.1:5000">Back</a><br><br>' + result + ''
