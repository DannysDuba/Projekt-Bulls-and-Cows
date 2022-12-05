"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Daniel Duba
email: duba.danny@gmail.com
discord: DannysDuba#3102
"""
import random
import time

separate = 50 * "-"


def greeting():
    print(f'''
Hi there! 
{separate}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
(If you want to know how to play, check "Readme".)
{separate}''', sep="\n")


def no_duplicate(num):
    """Funkce vyhodnotí, aby se neopakovaly stejné čísla."""
    if len(num) != len(set(num)):
        return True


def four_digit(num):
    """Funkce vyhodnotí, aby zadný vstup obsahoval 4 čísla."""
    if len(num) != 4:
        return True


def no_zero(num):
    """Funkce vyhodnotí, aby zadaný vstup nezačínal nulou."""
    if str(num).startswith("0"):
        return True


def only_numbers(num):
    """Funkce vyhodnotí, aby zadaný vstup obsahoval pouze čísla."""
    if not num.isnumeric():
        return True


def secret_number():
    """Funkce vytvoří tajné, unikátní číslo."""
    while True:
        num = str(random.randint(1000, 9999))
        if len(num) == len(set(num)):
            return num


def singular_plural(bulls, cows):
    """Funkce, která rozliší jednotné a množné číslo."""
    if cows == 1:
        cows_name = "cow"
    else:
        cows_name = "cows"
    if bulls == 1:
        bulls_name = "bull"
    else:
        bulls_name = "bulls"

    print(bulls, bulls_name, ",", cows, cows_name)


def bulls_and_cows(enter, num):
    """Funkce, která přiřadí k zadanému vstupu bulls & cows"""

    cows = 0
    bulls = 0
    for i, x in enumerate(enter):
        for location, value in enumerate(num):
            if i == location and x == value:  # Pokud hráč uhodne hodnotu i umístění, přiřadíme bulls.
                bulls += 1
            elif i != location and x == value:  # Pokud hráč uhodne hodnotu, ale ne umístění, přiřadíme cows.
                cows += 1

    return bulls, cows


def input_check(enter):
    """Funkce, která definuje, aby byly splněny všechny podmínky."""

    print(separate)

    if only_numbers(enter):
        print("Enter a digit! ")

    elif four_digit(enter):
        print("Enter 4 digit number! ")

    elif no_duplicate(enter):
        print("No duplicities!")

    elif no_zero(enter):
        print("Don't start with zero!")

    else:
        print(">>>", enter)
        return True


def stats_one_game(attempts):
    """Funkce, která vyhodnotí pokusy hráče."""

    if attempts < 4:
        return "That's amazing"

    elif attempts < 10:
        return "That's average.."

    else:
        return "That's not so good.."


def game_continue():
    """Funkce, která umožní opakování hry, pokud bude hráč chtít."""
    while (new_game := input("Do you want to play again? Y/N: ")) != "N":
        print("Great let's play again.", separate, sep="\n")

        game()


def guess(attempts):
    """Funkce, která rozliší jednotné a množné číslo slova Guess."""

    if attempts == 1:
        return "Guess"
    else:
        return "Guesess"


def results(elapsed_time, attempts):
    """Funkce vypíše výsledky"""

    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    print(f"Correct, you've guessed the right number.", separate, sep="\n")
    print(f"""STATISTICS:
|GAME TIME: {round(minutes)} minutes and {round(seconds)} seconds.
|{attempts} {guess(attempts)}: {stats_one_game(attempts)}""")
    print(separate)


def game():
    """Průběh hry"""
    greeting()
    num = secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        enter = input("Enter a number: ")
        attempts += 1

        if not input_check(enter):
            print("Don't waste your attempts.")
            print(separate)

            continue

        bulls, cows = bulls_and_cows(num, enter)
        singular_plural(bulls, cows)

        print(separate)

        if bulls == 4:
            end_time = time.time()
            timing = end_time - start_time
            results(timing, attempts)

            break

    game_continue()
    print(separate)
    print("Good game, bye bye")

    exit()


if __name__ == "__main__":
    game()
