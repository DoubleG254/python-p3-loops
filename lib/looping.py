#!/usr/bin/env python3

def happy_new_year():
    t=10
    while t>=1:
        print(t)
        t-=1
    print("Happy New Year!")

    # code goes here!
    pass

def square_integers(int_list):
    square_list=[num*num for num in int_list]
    return square_list
    # code goes here!
    pass

def fizzbuzz():
    n = 1
    while n < 101:
        if n % 3 ==0 and n % 5 ==0:
            print("FizzBuzz")
        elif n % 3 ==0:
            print("Fizz")
        elif n % 5 ==0:
            print("Buzz")
        else:
            print(n)
        n+=1
    # code goes here!
    pass
