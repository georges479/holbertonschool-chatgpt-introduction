#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Check if arguments are passed
    if len(sys.argv) < 2:
        print("No arguments provided. Usage: ./script.py <arg1> <arg2> ...")
    else:
        # Print all arguments, including the script name
        for i in range(len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
