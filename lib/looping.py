#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1

    print("Happy New Year!")
    pass

def square_integers(int_list):
    squared_ints = []
    for num in int_list: 
        squared_ints.append(num * num)

    return squared_ints

    pass

def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else :
            print(num)
    pass
