"""
Project: Fun Facts with Animals
File: main.py

This program takes in input for any animal, and searches through several databases to find 5 interesting facts
about the specified animal. It takes a multistep approach, from finding the data, to scraping the data, searching
through the data for the most interesting facts, and finally, condensing it to a few short bullet points.

Author: Dylan Sturr
"""


def main():
    """
    Gathers animal input and calls helper methods to ultimately achieve this project's goal
    :return:
    """
    animal_name = input("Name any animal: ")
    print(animal_name)


if __name__ == '__main__':
    main()
