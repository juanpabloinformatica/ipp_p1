"""
Random Name Generator

This script generates random first names and last names, combines them to create full names, and allows the user to choose whether to continue generating names or stop the process. It uses the 'names' library to generate random names.

Functions:
- generate_firstnames(list_length: int) -> list[str]: Generates a list of random first names.
- generate_lastnames(list_length: int) -> list[str]: Generates a list of random last names.
- generate_name(first_name: str, last_name: str) -> str: Combines a first name and a last name to create a full name.

Main Function:
- main() -> None: The main function of the script that generates and prints random names based on user input.

Constants:
- MIN_VALUE: Final[int] = 0: The minimum value for generating a random dimension.
- MAX_VALUE: Final[int] = 10: The maximum value for generating a random dimension.
- DIMENSION: Final[int]: A random dimension between MIN_VALUE and MAX_VALUE.
- firstnames: list[str]: A list of generated random first names.
- lastnames: list[str]: A list of generated random last names.

Usage:
Run this script to generate and print random names. The user can choose to continue generating names or stop the process by entering 1 or 2 when prompted.
"""
from typing import Final
import random
import names


def main() -> None:
    """
    The main function of the script.

    It generates random first names and last names, combines them to create full names, and allows the user to choose whether to continue generating names or stop the process.
    """
    MIN_VALUE: Final[int] = 0
    MAX_VALUE: Final[int] = 10
    DIMENSION: Final[int] = random.randint(MIN_VALUE, MAX_VALUE)
    firstnames: list[str] = generate_firstnames(DIMENSION)
    lastnames: list[str] = generate_lastnames(DIMENSION)
    print(firstnames)
    print(lastnames)
    switch: int = int(input("Enter:\n1 -> Continue\n2 -> Stop\n"))
    while switch == 1:
        firstname: str = firstnames[random.randint(MIN_VALUE, DIMENSION - 1)]
        lastname: str = lastnames[random.randint(MIN_VALUE, DIMENSION - 1)]
        new_name: str = generate_name(firstname, lastname)
        print("Generated Name:")
        print(new_name)
        switch = int(input("Do you want to continue:\n1 -> Continue\n2 -> Stop\n"))


def generate_lastnames(list_length: int) -> list[str]:
    """
    Generate a list of random last names.

    Args:
        list_length (int): The number of last names to generate.

    Returns:
        list[str]: A list of random last names.
    """
    return [names.get_last_name() for _ in range(list_length)]


def generate_firstnames(list_length: int) -> list[str]:
    """
    Generate a list of random first names.

    Args:
        list_length (int): The number of first names to generate.

    Returns:
        list[str]: A list of random first names.
    """
    return [names.get_first_name() for _ in range(list_length)]


def generate_name(first_name: str, last_name: str) -> str:
    """
    Combine a first name and a last name to create a full name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        str: The full name.
    """
    return f"{first_name} {last_name}"


if __name__ == "__main__":
    main()
