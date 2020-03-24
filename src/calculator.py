import operator
import re
import sys

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
OPERATION_PRIORITY = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '**': 3}


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

        
        elif token == '(':
          stack_operators.append(token)            
    
        elif token == ')':
            while stack_operators[-1] != '(':
                stack_nums.append(stack_operators.pop())
                operand_right = stack_nums.pop(-2)
                operand_left = stack_nums.pop(-2)
                func = OPERATORS[stack_nums.pop()]                
                result_num = func(operand_left, operand_right)                
                stack_nums.append(result_num)
            stack_operators.pop()


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
    if len(sys.argv) == 1:
        print('Please enter arguments')
    elif len(sys.argv) >= 2:
        expr = (sys.argv[1])
        print(calculate(expr))
    
    
    


        
 #       elif token == '(':
   #       stack_operators.append(token)            
    
    #    elif token == ')':
     #       while stack_operators[-1] != '(':
      #          stack_nums.append(stack_operators.pop())
       #         operand_right = stack_nums.pop()
        #        operand_left = stack_nums.pop()
         #       func = OPERATORS[stack_nums.pop()]                
          #      result_num = func(operand_left, operand_right)                
           #     stack_nums.append(result_num)
#
 #           stack_operators.pop()