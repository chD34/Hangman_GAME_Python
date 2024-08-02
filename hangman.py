# Problem Set 2, hangman.py
# Name: Chernetska Dayana
# Collaborators: None
# Time spent: +- 6 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    The function returns True if letter
    in letters_guessed is in secret_word.
    In other case the function returns False.

    * letters_guessed is a list which contains
    letter which user have already entered.
    * secret_word is a word which user must guess.

    """
    set_of_letters = set()
    result = True
    for letter in secret_word:
        if letter not in letters_guessed:
            result = False
    return result



def get_guessed_word(secret_word, letters_guessed):
    """
    The function returns secret_word which consists of
    guessed letters and not guessed letters replaced with "_".
    """

    result = secret_word
    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word = secret_word.replace(letter, "_")
        else:
            continue
    return secret_word


def get_available_letters(letters_guessed):
    """
       The function returns all latin letters
       which weren`t mentioned by user.
    """
    string = ""
    for i in range(ord("a"), ord("z") + 1):
        string = string + chr(i)
    for letter in string:
        if letter in letters_guessed:
            string = string.replace(letter, "")
    print(string)

    
    

def hangman(secret_word = "bezique"):
    """
    It is a function of the game Hangman without hints
    """
    while True:
        guesses = 6
        letters_guessed = []
        number_of_letters = len(secret_word)
        rest_of_guesses = guesses - len(letters_guessed)
        print("Welcome to the game Hangman!\n"
              'I am thinking of a word that is {} letters long.'.format(number_of_letters))

        while guesses != 0:
            print("Avaliable letters: ")
            try:
                get_available_letters(letters_guessed)
            except ValueError:
                print("Error!")
            print("You have {} guesses left".format(guesses))

            while True:
                try:
                    letter = str(input("Enter a letter: "))
                    if len(letter) != 1:
                        raise ValueError("Enter one  letter!")
                    break
                except ValueError as ve:
                    print(ve)
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Good guess!")
            else:
                guesses -= 1
                print("Oops! That letter is not in my word! ")
            print("---------------------------")
            print("My word: ")
            try:
                res = get_guessed_word(secret_word, letters_guessed)
                print(res)
            except ValueError:
                print("Error!")
            try:
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print("Congratulations! You won !")
                    break
            except ValueError:
                print("Error")
        if guesses == 0:
            print("Sorry, you ran out of guesses.The word was : " + str(secret_word))
        print("\n""Start the game again?(print yes or not)")
    # перезапуск програми за бажанням
        while True:
            start = input()
            if start == "yes" or start == "not":
                break
            else:
                print("Error! Print yes or not")
        if start == "not":
            break



def match_with_gaps(my_word, other_word):
    """
    This function should return True if the
    guessed letters from my_word match
    the corresponding letters from other_word.
    It should return False if two words are
    different  lengths or the guessed letters
    from my_word do not match the letters
    from other_word.

    * my_word is a word which consists of
    guessed letters and not guessed letters replaced with "_"
    *
    """

    result = False
    index = 0
    for letter in my_word:
        try:
            if letter != "_" and letter == other_word[index] and len(my_word) == len(other_word):
                index = index + 1
                result = True
            elif letter == "_":
                index = index + 1
                result = True
                continue
            else:
                result = False
                break
        except IndexError:
            result = False
            break
    return result


def show_possible_matches(my_word):
    """
        This function should output all words from
        the wordlist that match my_word. It should
        display "No matches found" if there are no matches.
    """
    result = "No matches found"
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            result = ""
            print(other_word)
    print(result)


def hangman_with_hints(secret_word):
    """
       It is a function of the game Hangman with hints
    """
    while True:
        guesses = 6
        letters_guessed = []
        number_of_letters = len(secret_word)
        rest_of_guesses = guesses - len(letters_guessed)
        print("Welcome to the game Hangman!\n"
              "Print letters in lower case if you want the computer understand them "
              'I am thinking of a word that is {} letters long.'.format(number_of_letters))
        while guesses != 0:
            print("Avaliable letters: ")
            try:
                get_available_letters(letters_guessed)
            except ValueError:
                print("Error!")
            print("You have {} guesses left".format(guesses))

            while True:
                try:
                    letter = str(input("Enter a letter: "))
                    if len(letter) != 1:
                        raise ValueError("Enter one  letter!")
                    elif letter == "*":
                        try:
                            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                        except ValueError:
                            print("Error")
                    break
                except ValueError as ve:
                    print(ve)
            letters_guessed.append(letter)
            if letter == "*":
                print()
            elif letter in secret_word:
                print("Good guess!")
            else:
                guesses -= 1
                print("Oops! That letter is not in my word! ")
            print("---------------------------")
            print("My word: ")
            try:
                res = get_guessed_word(secret_word, letters_guessed)
                print(res)
            except ValueError:
                print("Error!")
            try:
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print("Congratulations! You won !")
                    break
            except ValueError:
                print("Error")
        if guesses == 0:
            print("Sorry, you ran out of guesses.The word was : " + str(secret_word))
        print("\n""Start the game again?(print yes or not)")
    # перезапуск програми за бажанням
        while True:
            start = input()
            if start == "yes" or start == "not":
                break
            else:
                print("Error! Print yes or not")
        if start == "not":
            break




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
