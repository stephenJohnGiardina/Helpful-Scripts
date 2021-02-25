"""
This is a script that you can use to browse the file architecture.
"""

import inquirer
import os

def obtain_directory(question):
    """
    This is a function that helps the user locate directories.
    """

    correct_input = False
    current_directory = None

    while not correct_input:
        directories = []

        for file in os.listdir(current_directory):
            if current_directory == None:
                if os.path.isdir(file):
                    directories.append("DIRECTORY: " + file)  
            else:
                if os.path.isdir(current_directory + file):
                    directories.append(file)

        questions = [
            inquirer.List(
                "IN",
                message=question,
                choices=directories
            )
        ]

        answers = inquirer.prompt(questions)

        if current_directory == None:
            current_directory = ""

        current_directory += answers["IN"] + "/"
        correct_directory_questions = [
            inquirer.List(
                "Correct input",
                message=(
                    "Is this the directory you want to use?" + current_directory
                ),
                choices=[
                    "Yes",
                    "No. The directory I want is in this directory.",
                    "No. I did not mean to choose this directory. Let me choose again."
                ]
            )
        ]
        correct_directory_answers = inquirer.prompt(correct_directory_questions)
        correct_directory_answer = correct_directory_answers["Correct input"]
        if correct_directory_answer == "Yes":
            return current_directory
        elif "I want" in correct_directory_answer:
            continue
        elif "I did" in correct_directory_answer:
            current_directory = current_directory[:current_directory.rfind('/')]
            if current_directory == "":
                current_directory = None

def obtain_file(question):
    """
    This is a function that helps the user locate files.
    """
    # TODO: allow for files to be chosen

    correct_input = False
    current_directory = None

    while not correct_input:
        directories = []

        for file in os.listdir(current_directory):
            if current_directory == None:
                if os.path.isdir(file):
                    directories.append("DIRECTORY: " + file)
                else:
                    directories.append(file)
            else:
                if os.path.isdir(current_directory + file):
                    directories.append("DIRECTORY: " + file)
                else:
                    directories.append(file)

        questions = [
            inquirer.List(
                "IN",
                message=question,
                choices=directories
            )
        ]

        answers = inquirer.prompt(questions)

        if current_directory == None:
            current_directory = ""

        current_directory += answers["IN"] + "/"
        correct_directory_questions = [
            inquirer.List(
                "Correct input",
                message=(
                    "Is this the directory you want to use?" + current_directory
                ),
                choices=[
                    "Yes",
                    "No. The directory I want is in this directory.",
                    "No. I did not mean to choose this directory. Let me choose again."
                ]
            )
        ]
        correct_directory_answers = inquirer.prompt(correct_directory_questions)
        correct_directory_answer = correct_directory_answers["Correct input"]
        if correct_directory_answer == "Yes":
            return current_directory
        elif "I want" in correct_directory_answer:
            continue
        elif "I did" in correct_directory_answer:
            current_directory = current_directory[:current_directory.rfind('/')]
            if current_directory == "":
                current_directory = None


# TODO: Add the ability to go up directories passed the starting directory.

print("This is the directory you chose:\n\n" + obtain_directory("Pick a folder"))
print("This is the file you chose:\n\n" + obtain_file("Pick a file"))
