import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # overwrite the line
        time.sleep(1)
        seconds -= 1
    print("00:00")
    print("Time's up!")

# Example: countdown for 10 seconds
countdown_timer(10)



# Creating a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# Creating a set
my_set = {100, 200, 300, 400, 500}
print("Set:", my_set)

# Demonstrating operations
# Lists are mutable
my_list.append(6)
print("Updated List:", my_list)

# Tuples are immutable (cannot be changed)
# my_tuple[0] = 99  # This would cause an error

# Sets automatically remove duplicates
my_set.add(300)  # Adding duplicate
print("Updated Set:", my_set)



# Exercise: Number Guessing Game

import random

def number_guessing_game():
    secret_number = random.randint(1, 20)  # Random number between 1 and 20
    attempts = 0
    guess = None

    print("I'm thinking of a number between 1 and 20.")

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.")

# Run the game
number_guessing_game()



# Project: Simple To-Do List App

def todo_app():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"Task '{task}' added!")
        elif choice == "2":
            if not tasks:
                print("No tasks yet!")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove!")
            else:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' removed!")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

# Run the app
todo_app()
