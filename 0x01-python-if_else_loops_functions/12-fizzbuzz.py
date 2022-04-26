#!/usr/bin/python3
def fizzbuzz():
    for fb in range(1, 101):
        if fb % 3 == 0 and fb % 5 == 0:
            print(f'FizzBuzz ', end='')
            continue
        elif fb % 3 == 0 and fb % 5 != 0:
            print(f'Fizz ', end='')
            continue
        elif fb % 5 == 0 and fb % 3 != 0:
            print(f'Buzz ', end='')
            continue
        print(f'{fb} ', end='')
