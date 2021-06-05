from flask import Flask, jsonify, json, request
from flask_cors import CORS
from CalcOps import SimpleOps as so

calc = Flask(__name__)
CORS(calc)


@calc.route("/<op_name>", methods=['POST'])
def operation(op_name):
    data = json.loads(request.data)
    result = 'Error'
    if 'add' == op_name:
        result = so.add(data['num1'], data['num2'])
    elif 'mul' == op_name:
        result = so.mul(data['num1'], data['num2'])
    elif 'div' == op_name:
        result = so.div(data['num1'], data['num2'])
    elif 'sub' == op_name:
        result = so.sub(data['num1'], data['num2'])
    elif 'neg' == op_name:
        result = so.mul(data['num1'], -1)

    return jsonify(result)


if __name__ == '__main__':
    calc.run(port=5050)
