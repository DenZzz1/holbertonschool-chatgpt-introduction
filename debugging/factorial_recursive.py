#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return None  # Factorielle non définie pour les négatifs
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    f = factorial(n)
    if f is None:
        print("Error: Factorial is not defined for negative numbers")
        sys.exit(1)
    print(f)
except ValueError:
    print("Error: Please provide a valid integer")
    sys.exit(1)
