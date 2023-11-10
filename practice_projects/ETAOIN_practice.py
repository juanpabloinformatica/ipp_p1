"""
get number of  each letter in a pretty format
"""
import pprint


def letter_count(text: str) -> dict:
    """
    dict that has the letter encounters in the text
    with the ocurrences of the same
    """
    ALPHABET = "abcdefghijklmnopqrstwxyz"
    letter_count_dict = {}
    for letter in text:
        if letter in ALPHABET:
            if letter not in letter_count_dict:
                letter_count_dict[letter] = [letter]
            else:
                update_value = [*letter_count_dict[letter], letter]
                letter_count_dict.update({letter: update_value})
    # print(letter_count)
    return letter_count_dict


def main() -> None:
    """
    Entry point
    """
    text = "Like the castle in its corner in a\
            medieval game, I foresee terrible \
trouble and I stay here just the same."
    letter_count_dict = letter_count(text)
    printer = pprint.PrettyPrinter(indent=10, width=80, depth=6)
    printer.pprint(letter_count_dict)

if __name__ == "__main__":
    main()
