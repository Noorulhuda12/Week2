# -*- coding: utf-8 -*-
"""game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pqKbR-ylX0HfYdoTw5JLQcCu1cW6CJIR
"""

import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    level = get_positive_integer("Level: ")
    secret_number = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()