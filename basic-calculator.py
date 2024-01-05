strNum1 = ''
strNum2 = ''
operator = ''

while strNum1 == '' or strNum1.isnumeric() is False:
    strNum1 = input('Enter N1: ')
while strNum2 == '' or strNum2.isnumeric() is False:
    strNum2 = input('Enter N2: ')

num1 = int(strNum1)
num2 = int(strNum2)

while operator == '':
    operator = input('Enter the operator : ')

if operator == '+':
    print(num1+num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    if num2 > 0:
        print(num1/num2)
    else:
        print('Division by zero is not allowed')
elif operator == '-':
    print(num1-num2)
elif operator == '**':
    print(num1**num2)
else:
    print('Invalid operator')