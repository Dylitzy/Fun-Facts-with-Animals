import requests
import json
from bs4 import BeautifulSoup

"""
Project: Fun Facts with Animals
File: main.py

This program takes in input for any animal, and searches through several databases to find 5 interesting facts
about the specified animal. It takes a multistep approach, from finding the data, to scraping the data, searching
through the data for the most interesting facts, and finally, condensing it to a few short bullet points.

Author: Dylan Sturr
"""


def query(inpt):
    """
    Determines if the input is an animal or not. If so, returns a list of results based on the animal list.
    :param inpt: (possible) animal input
    :return:
    """
    results = []
    with open("animals.txt") as animals:
        for animal in animals:
            stripped = animal.strip()  # don't think about this too much
            if inpt.title() in stripped:
                results.append(stripped)
    return results


def get_info(animal):
    """
    Given the picked animal, finds the top 5 best sources of information about that animal and returns
    them in a list
    :param animal: animal input
    :return: the list of sources
    """
    sources = []
    return sources


def get_facts(source):
    """
    Given the source material, compiles a list of 5 interesting facts about that animal.
    :param source: source to compile facts from
    :return: the list of facts
    """
    facts = []
    return facts


def main():
    """
    Gathers animal input and calls helper methods to ultimately achieve this project's goal
    :return:
    """
    animal_name = input("Name any animal: ")
    results = query(animal_name)
    if len(results) != 0:
        print("Found", len(results), "matches:")
        for i in range(len(results)):
            print(f"{i + 1}. {results[i]}")
        animal_name = input("\nSelect an animal from the list above: ")
        if animal_name in results:
            print("Valid! Have a good day! (WIP)")
        else:
            print(f"Invalid input: {animal_name} was not found among the filtered results. Please check your spelling.")
    else:
        print(f"Invalid input: {animal_name} is not a recognized animal name! Please check your spelling.")


if __name__ == '__main__':
    main()
