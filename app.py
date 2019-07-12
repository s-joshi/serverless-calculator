# app.py file

from flask import Flask, request

app = Flask(__name__)

@app.route('/calc')
def calc():
    operand_1 = request.args.get('operand_1')
    print('operand_1', operand_1)
    operand_2 = request.args.get('operand_2')
    print('operand_2', operand_2)
    operator = request.args.get('operator')
    print('operator', operator)

    if operator == 'add':
        operator = '+'
    elif operator == 'minus':
        operator = '-'
    elif operator == 'div':
        operator = '/'
    elif operator == 'mult':
        operator = '*'
    elif operator == 'mod':
        operator = '%'
    else:
        return {'operand_1': operand_1, 'operand_2': operand_2,
        'operator': operator, 'error': 'invalid parameters',
        'status_code': 400}

    return {'operand_1': operand_1, 'operand_2': operand_2,
    'operator': operator, 'result': eval(str(operand_1) + operator + str(operand_2)),
    'status_code': 200}
