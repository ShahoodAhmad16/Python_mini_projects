import random


def main():
    random_number = random.randint(0, 10)
    check_random_number(random_number)


def check_random_number(computer_generated_number):
    count = 1
    while count <= 3:
        number = int(input('Guess a number in between 0 and 10'))
        if number == computer_generated_number:
            print('Congrates you guess the number')
            return
        else:
            print('Wrong Try again')
            count += 1
    print('\nSorry\nYou are out of chances')


main()
