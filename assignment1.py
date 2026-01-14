#!/usr/bin/env python3
"""
Assignment 1 - Basic Python Program
A simple program that demonstrates basic Python concepts.
"""


def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the assignment."""
    print("Welcome to Assignment 1!")
    print(greet("World"))
    
    # Demonstrate basic input/output
    name = input("What's your name? ")
    print(greet(name))


if __name__ == "__main__":
    main()
