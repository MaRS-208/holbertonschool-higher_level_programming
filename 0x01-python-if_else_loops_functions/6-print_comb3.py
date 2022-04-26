#!/usr/bin/python3
num = 0
for i in range(0, 9):
    num = num + 1
    for j in range(num, 10):
        if i != j and i < 8:
            print(f'{i}{j}, ', end='')
        else:
            print(f'{i}{j}')
