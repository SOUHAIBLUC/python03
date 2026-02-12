#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Main function that processes command-line arguments.
    This function demonstrates:
    1. How to access the program name
    2. How to count arguments
    3. How to display each argument
    """

    print("=== Command Quest ===")

    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:

        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {num_arguments}")

        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
