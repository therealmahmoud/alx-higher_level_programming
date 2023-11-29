#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if (n // 5) * 5 == n and (n //3) * 3 == n:
            print("fizzbuzz", end=" ")
        elif (n // 3) * 3 == n:
            print("fizz", end=" ")
        elif (n // 5) *5 == n:
            print("buzz", end=" ")
        else:
            print(n, end=" ")
