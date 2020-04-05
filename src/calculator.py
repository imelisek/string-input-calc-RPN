import math
import operator
import re
import sys


OPERATORS = {
    '+': operator.add, 
    '-': operator.sub, 
    '*': operator.mul, 
    '/': operator.truediv, 
    '**': operator.pow
    }

UNARY_OPERTRS = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sh': math.sinh,
    'ch': math.cosh,
    'th': math.tanh
    }

OPERATION_PRIORITY = {
    '(': 0, ')': 0, 
    '+': 1, '-': 1, 
    '*': 2, '/': 2, 
    '**': 3, 
    'sin': 4, 'cos': 4,
    'tan': 4, 'sh': 4,
    'ch': 4, 'th': 4
    }


def is_action(val):
    if val in OPERATORS.keys():
        return True
    return False
    
def is_number(val):
    if re.search(r'-?\d+(?:\.\d+)?', val):
        return True
    return False
    
def is_unary(val):
    if val in UNARY_OPERTRS.keys():
        return True
    return False


def process_stacks(numbers, actions):
    if is_action(actions[-1]):
        operand_right = numbers.pop()
        operand_left = numbers.pop()
        func = OPERATORS[actions.pop()]                
        result_num = func(operand_left, operand_right)                
        numbers.append(result_num)

    elif is_unary(actions[-1]):
        operand = numbers.pop()
        prefix_operation = UNARY_OPERTRS[actions.pop()]   
        result_num = prefix_operation(math.radians(operand))
        numbers.append(result_num)


def calculate(expr):
    stack_nums = []
    stack_operators = []

    for token in expr.split():
        if is_action(token):
            while len(stack_operators) != 0 and OPERATION_PRIORITY[stack_operators[-1]] >= OPERATION_PRIORITY[token]:
                process_stacks(stack_nums, stack_operators)
            stack_operators.append(token)

        elif is_unary(token):
            while len(stack_operators) != 0 and OPERATION_PRIORITY[stack_operators[-1]] >= OPERATION_PRIORITY[token]:
                process_stacks(stack_nums, stack_operators)
            stack_operators.append(token)
                               
        elif is_number(token):
            stack_nums.append(float(token)) 
                
        elif token == '(':                  
          stack_operators.append(token)            
    
        elif token == ')':
            while stack_operators[-1] != '(' and OPERATION_PRIORITY[stack_operators[-1]] >= OPERATION_PRIORITY[token]:
                process_stacks(stack_nums, stack_operators)
            stack_operators.pop()

        elif token == '!':
            operand_left = stack_nums.pop()                
            result_num = math.factorial(operand_left)                
            stack_nums.append(result_num)
                      
        else: 
            raise ValueError
                        
    while len(stack_operators) != 0:
        process_stacks(stack_nums, stack_operators)

    return stack_nums[-1]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Please enter arguments')
    elif len(sys.argv) >= 2:
        expr = (sys.argv[1])
        print(calculate(expr))
    