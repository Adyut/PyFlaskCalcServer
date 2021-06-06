from flask import Flask, jsonify, json, request
from flask_cors import CORS, cross_origin
from CalcOps import SimpleOps as so

calc = Flask(__name__)
cors = CORS(calc)
calc.config['CORS_HEADERS'] = 'Content-Type'


@calc.route("/<op_name>", methods=['POST'])
@cross_origin()
def operation(op_name):
    data = json.loads(request.data)
    # op_name = data['op']
    print(f"Received Operation Request for '{op_name}' with arguments num1 : {data['num1']} and num2 : {data['num2']}.")
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
        result = so.mul(data['num2'], -1)

    print(f"Response is {result}.")
    return jsonify(result)


if __name__ == '__main__':
    calc.run(port=5050)
