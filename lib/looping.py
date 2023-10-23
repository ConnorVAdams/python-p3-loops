#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i-= 1
    print('Happy New Year!')

happy_new_year()

def square_integers(int_list):
    return [num * num for num in int_list]

ints = square_integers([1, 2, 3, 4, 5])
print(ints)

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i += 1

fizzbuzz()