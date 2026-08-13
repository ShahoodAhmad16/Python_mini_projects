def main():
    while True:
        table_number = int(input('Table number: '))
        another_turn = table_generator(table_number)
        if another_turn is False:
            break


def table_generator(x):
    i = 1
    while i <= 10:
        print(f'{x}*{i}={x*i}')
        i += 1
    another_number = int(
        input('Do you want another number\n1:Yes\n2:No\n> '))
    if another_number == 1:
        return True
    else:
        print('Exiting')
        return False


main()
