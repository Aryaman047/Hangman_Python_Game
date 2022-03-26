
import os
import random
import time
from words import final_list


def get_word():
    word = random.choice(final_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    time.sleep(2)
    print("WELCOME TO THE GAMBLE OF A LIFE")
    time.sleep(3)
    print("7 TRIES TO DECIDE THE FATE OF A MAN")
    time.sleep(3)
    print("Let's begin my friend")
    time.sleep(2)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            os.system("cls")

            if guess in guessed_letters:
                time.sleep(0.1)
                print("You already guessed the letter", guess)
            elif guess not in word:
                time.sleep(0.1)
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                os.system("cls")
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            os.system("cls")
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        time.sleep(2)
        print("Congrats,YOU HAVE SAVED A LIFE !!")
    else:
        time.sleep(3)
        print("SOMEONE'S AT GUILT FOR A DEATH")
        time.sleep(3)
        print("The word was " + word + ".")
        time.sleep(3)
        print("Better Luck next time")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    os.system("cls")
    play(word)
    while input("Wanna Gamble again? (Y/N) ").upper() == "Y":
        os.system("cls")
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()


##We import a words list from a trusted source and convert it into a list in wors.py
# A random choice word is stored in "word" and 
# while loop runs until tries and guesses are > 0    