import operator
import re
import sys

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
OPERATION_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}


def is_action(val):
    if val in OPERATORS.keys():
        return True
    return False
    
def is_number(val):
    if re.search(r'-?\d+(?:\.\d+)?', val):
        return True
    return False
    

def calculate(expr):
    stack_nums = []
    stack_operators = []

    for token in expr.split():
        if is_action(token):
            while len(stack_operators) != 0 and OPERATION_PRIORITY[stack_operators[-1]] >= OPERATION_PRIORITY[token]:
                operand_right = stack_nums.pop()
                operand_left = stack_nums.pop()
                func = OPERATORS[stack_operators.pop()]                
                result_num = func(operand_left, operand_right)                
                stack_nums.append(result_num)
            stack_operators.append(token)


        elif is_number(token):
            stack_nums.append(float(token)) #process as a number

        else: 
            raise ValueError

    while len(stack_operators) != 0:
        operand_right = stack_nums.pop()
        operand_left = stack_nums.pop()
        func = OPERATORS[stack_operators.pop()]        
        result_num = func(operand_left, operand_right)
        stack_nums.append(result_num)
    
    return stack_nums[-1]


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        expr = (sys.argv[1])
    print(calculate(expr))
    
    
    
