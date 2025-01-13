#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        # Vérifier si un argument est fourni
        if len(sys.argv) != 2:
            print("Usage: ./factorial.py <non-negative integer>")
            sys.exit(1)
        
        # Convertir l'argument en entier
        number = int(sys.argv[1])

        # Calculer la factorielle
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except RecursionError:
        print("Error: The input number is too large to compute its factorial.")

