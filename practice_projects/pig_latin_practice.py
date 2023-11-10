"""
practice projects
    - exercice 1
"""


def word2piglatin(word: str) -> str:
    """
    take a word and depending is starts with consonant
    or with vowel it returns it's pig_latin version
    """
    if word[0] not in ["a", "e", "i", "o", "u"]:
        print(word[1:])
        new_word = word[1:] + word[0] + "ay"
    else:
        new_word = word + "way"
    return new_word


def main() -> None:
    """
    Entry point
    """
    word = input("Write a word:\t").strip()
    pig_latin = word2piglatin(word)
    print(pig_latin)


if __name__ == "__main__":
    main()
