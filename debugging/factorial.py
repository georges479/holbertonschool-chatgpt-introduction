#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to prevent infinite loop
    return result

if __name__ == "__main__":
    # Check if a command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)
    
    try:
        # Convert the input to an integer
        num = int(sys.argv[1])
        # Calculate the factorial
        fact = factorial(num)
        print(f"The factorial of {num} is: {fact}")
    except ValueError as e:
        # Handle invalid inputs or negative numbers
        print(f"Error: {e}")
        sys.exit(1)
