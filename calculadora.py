#!/usr/bin/python3

import sys
import operator

NUM_ARGS = 4

operations = {'suma': operator.add,
              'resta': operator.sub,
              'multiplicar': operator.mul,
              'dividir': operator.truediv
              }

if __name__ == "__main__":

    if len(sys.argv) != NUM_ARGS:
        sys.exit('Usage error: <operation> <num1> <num2>')

    try:
        op = operations[sys.argv[1]]
        print(op(int(sys.argv[2]), int(sys.argv[3])))
    except (KeyError, ValueError):
        sys.exit('Invalid operation')
    except ZeroDivisionError:
        sys.exit('Can not be divided by zero')
