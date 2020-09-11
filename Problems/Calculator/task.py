a = float(input())
b = float(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '/':
    if b == 0.0:
        print('Division by 0!')
    else:
        print(a / b)
elif op == '*':
    print(a * b)
if op == 'mod':
    if b == 0.0:
        print('Division by 0!')
    else:
        print(a % b)
if op == 'pow':
    print(a ** b)
if op == 'div':
    if b == 0.0:
        print('Division by 0!')
    else:
        print(a // b)
