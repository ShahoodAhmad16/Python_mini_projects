def main():
    while True:
        number1 = float(input(f'Enter the 1st number: '))
        number2 = float(input(f'Enter the 2nd number: '))
        keep_going = calculator(number1, number2)
        if keep_going is False:
            break


def add(x, y):
    return f'{x+y}'


def subtract(x, y):
    return f'{x-y}'


def multiply(x, y):
    return f'{x*y}'


def divide(x, y):
    if y == 0:
        return 'Cannot divide by zero'
    return f'{x/y:.2f}'


def calculator(num1, num2):
    while True:
        choice = int(input(
            '\nSelect mathematical operation you want to perform\n1:Addition\n2:Subtract\n3:Multiply\n4:Divide\n5:Try another numbers\n6:Exit'))
        if 0 < choice <= 6:
            if choice == 1:
                print(f'Addition: {add(num1, num2)}')
            elif choice == 2:
                print(f'Subtraction: {subtract(num1, num2)}')
            elif choice == 3:
                print(f'Multiplication: {multiply(num1, num2)}')
            elif choice == 4:
                print(f'Divide: {divide(num1, num2)}')
            elif choice == 5:
                return True
            elif choice == 6:
                print('Exiting')
                return False
        else:
            print('Choice must be in between 1 and 6')


main()
