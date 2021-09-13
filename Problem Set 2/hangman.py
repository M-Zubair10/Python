# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    verify = ""
    for i in secret_word:
        for m in letters_guessed:
            if i == m:
                verify += i
                break
    if verify == secret_word:
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    underscore = ""
    for i in secret_word:
        checker = False
        letters_storage = ""
        for m in letters_guessed:
            if i == m:
                if i == letters_storage:
                    break
                underscore += i + " "
                checker = True
                letters_storage += i
        if not checker:
            underscore += "_ "
    return underscore





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_storage = " "
    is_letters_in = False
    if letters_guessed in string.ascii_uppercase:
       letters_guessed = str.lower(letters_guessed)
    letters_available = string.ascii_lowercase
    for i in letters_guessed:
        if i == letters_storage[-1]:
            is_letters_in = True
        elif i in letters_available:
            is_letters_in = True
            letters_available = letters_available.replace(i, "")
            letters_storage += i
        else:
            is_letters_in = False
    print("Available letters: ", letters_available, "\n")
    if is_letters_in:
        return True
    else:
        return False




def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print(" " * 60 + "Welcome to the game hangman!")
    print("I am thinking of a word which is ", len(secret_word), " letters long")
    print("______________")
    print(secret_word)

    remaining_guesses = 6
    letters_guessed = ""
    number_of_warnings = 3
    is_it_guessed = False
    get_available_letters(letters_guessed)
    print("=> Number of guesses: ", remaining_guesses)
    print("=> Number of warnings: ", number_of_warnings, "\n")
    score = 0
    while is_it_guessed == False and remaining_guesses > 0 and number_of_warnings > 0:
        check = False
        guess = input("Please guess a letter: ")
        if guess in letters_guessed:
            number_of_warnings -= 1
            print("You already guessed that letter.You have", number_of_warnings, "warnings left\n")
        else:
            if guess in string.ascii_uppercase:
                guess = str.lower(guess)
            for char in secret_word:
                if guess == char:
                    letters_guessed += guess
                    check = True
                    score += 1
            ui = get_guessed_word(secret_word, letters_guessed)
            if check:
                print("\nGood guess: ", ui)
            elif len(guess) > 1:
                number_of_warnings -= 1
                print("\n Please enter only one alphabet at a time! ")
                print("=> Number of Warnings Left: ", number_of_warnings, "\n")
            else:
                letters_guessed += guess
                remaining_guesses -= 1
                if guess == "a" or guess == "e" or guess == "i" or guess == "o":
                    remaining_guesses -= 1
                print("\nOops! That letter is not in my word: ", ui)
            is_it_guessed = is_word_guessed(secret_word, letters_guessed)
            total_letters = get_available_letters(letters_guessed)
            if not total_letters:
                if guess in "!@#$%^&*()_+~}{|><?:;/][":
                    remaining_guesses += 1
                    print("* Symbols are not allowed!\n  Kindly write alphabets only\n")
                    number_of_warnings -=1
                    print("=> Number of Warnings Left: ", number_of_warnings)
                elif len(guess) == 1:
                    try:
                        remaining_guesses += 1
                        int(guess)
                        print("* Numbers are not allowed\n  Kindly write alphabets only\n")
                        number_of_warnings -= 1
                        print("=> Number of Warnings Left: ", number_of_warnings)
                    except:
                        pass
            print("=> Number of Guesses Left: ", remaining_guesses, "\n")
            print("______________")

    # Win or Lose:
    if is_it_guessed:
        print("Congratulation, you won!")
        #if remaining_guesses == 5:
         #   print("Your Guess is too Good \n Thanks for Playing")
    elif number_of_warnings == 0:
        print("You are banned for inappropriate behaviour")
    else:
        print("Sorry, you ran out of guesses! \nBetter Luck Next Time!\nThe secret word was", "'",secret_word,"'")
    total_score = remaining_guesses * score
    print("Your total score for this game is:", total_score)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own)
# secret_word while you're doing your own testing)


# -----------------------------------


def removing_spaces(word):
    '''
    word: strings of letters of which spaces would be removed
    return: new string with all space would be removed
    '''
    for i in word:
        if i == " ":
            word = word.replace(i, "")
    return word


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    iteration = ""
    possible_words = ''
    my_word = removing_spaces(my_word)
    # for words in other_word:
    #     if len(my_word) == len(words):
    for i in range(len(my_word)):
        if my_word[i] == '_':
            pass
        else:
            a = i
            print(a)

            # print(possible_words)
    return possible_words





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    return match_with_gaps(get_guessed_word(secret_word, my_word), load_words())



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(" " * 60 + "Welcome to the game hangman!")
    print("I am thinking of a word which is ", len(secret_word), " letters long")
    print("______________")
    print(secret_word)

    remaining_guesses = 6
    letters_guessed = ""
    number_of_warnings = 3
    is_it_guessed = False
    get_available_letters(letters_guessed)
    print("=> Number of guesses: ", remaining_guesses)
    print("=> Number of warnings: ", number_of_warnings, "\n")
    score = 0
    while is_it_guessed == False and remaining_guesses > 0 and number_of_warnings > 0:
        check = False
        guess = input("Please guess a letter: ")
        if guess == "*":
           a = show_possible_matches(letters_guessed)
           print(a)
        elif guess in letters_guessed:
            number_of_warnings -= 1
            print("You already guessed that letter.You have", number_of_warnings, "warnings left\n")
        else:
            if guess in string.ascii_uppercase:
                guess = str.lower(guess)
            for char in secret_word:
                if guess == char:
                    letters_guessed += guess
                    check = True
                    score += 1
            ui = get_guessed_word(secret_word, letters_guessed)
            if check:
                print("\nGood guess: ", ui)
            elif len(guess) > 1:
                number_of_warnings -= 1
                print("\n Please enter only one alphabet at a time! ")
                print("=> Number of Warnings Left: ", number_of_warnings, "\n")
            else:
                letters_guessed += guess
                remaining_guesses -= 1
                if guess == "a" or guess == "e" or guess == "i" or guess == "o":
                    remaining_guesses -= 1
                print("\nOops! That letter is not in my word: ", ui)
            is_it_guessed = is_word_guessed(secret_word, letters_guessed)
            total_letters = get_available_letters(letters_guessed)
            if not total_letters:
                if guess in "!@#$%^&()_+~}{|><?:;/][":
                    remaining_guesses += 1
                    print("* Symbols are not allowed!\n  Kindly write alphabets only\n")
                    number_of_warnings -=1
                    print("=> Number of Warnings Left: ", number_of_warnings)
                elif len(guess) == 1:
                    try:
                        remaining_guesses += 1
                        int(guess)
                        print("* Numbers are not allowed\n  Kindly write alphabets only\n")
                        number_of_warnings -= 1
                        print("=> Number of Warnings Left: ", number_of_warnings)
                    except:
                        pass
            print("=> Number of Guesses Left: ", remaining_guesses, "\n")
            print("______________")

    # Win or Lose:
    if is_it_guessed:
        print("Congratulation, you won!")
        #if remaining_guesses == 5:
         #   print("Your Guess is too Good \n Thanks for Playing")
    elif number_of_warnings == 0:
        print("You are banned for inappropriate behaviour")
    else:
        print("Sorry, you ran out of guesses! \nBetter Luck Next Time!\nThe secret word was", "'",secret_word,"'")
    total_score = remaining_guesses * score
    print("Your total score for this game is:", total_score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    match_with_gaps("t__t", load_words())
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

     #secret_word = choose_word(wordlist)
    # hangman(secret_word)
###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
