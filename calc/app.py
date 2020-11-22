# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route('/add')
def run_add():
    '''add a and b'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def run_sub():
    '''subtract a from b'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def run_mult():
    '''multiple a and b'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)


@app.route('/div')
def run_div():
    '''subtract a from b'''
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<opr>")
def run_math(opr):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[opr](a, b)

    return str(result)