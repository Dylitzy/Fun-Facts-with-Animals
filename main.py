import requests
from bs4 import BeautifulSoup

"""
Project: Fun Facts with Animals
File: main.py

This program takes in input for any animal, and searches through several databases to find 5 interesting facts
about the specified animal. It takes a multistep approach, from finding the data, to scraping the data, searching
through the data for the most interesting facts, and finally, condensing it to a few short bullet points.

Author: Dylan Sturr
"""


def get_info(inpt):
    """
    Determines if the input is an animal or not. If so, scrapes the necessary info from various sources.
    Utilizes BeautifulSoup.
    :param inpt: (possible) animal input
    :return: whether the input is an animal or not
    """
    # url = f"https://www.itis.gov/ITISWebService/jsonservice/searchByCommonName?srchKey={inpt}"
    url = "https://www.itis.gov/servlet/SingleRpt/SingleRpt"
    response = requests.get(url)
    return False


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
    if get_info(input):
        print(animal_name)
    else:
        print(f"Invalid input: {animal_name} is not a recognized animal name!")


if __name__ == '__main__':
    main()
