a = 1
b = 2

try:
    result = a / b
except ZeroDivisionError as zero_error:
    print(zero_error)
    print("Error! ZeroDivisionError!")
except TypeError as type_error:
    print(type_error)
else:
    print("No errors!")
    print(f'Result: {result}')


nominator = 100.21
denominator = 'a string'

try:
    result = nominator / denominator
    print(result)
except TypeError as type_error:
    print(type_error)
    print("Whoops")