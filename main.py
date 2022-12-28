# Hangman:

import random

def play():
    game_title()
    secret_word = select_secret_word()
    correct_letters = start_correct_letters(secret_word)
    used_letters = []
    lost = False
    won = False
    errors = 0
    attempts = 10
    draw_hangman(errors)
    print(*correct_letters)
    print(f"\nThere are {str(correct_letters.count('_'))} missing letters ")
    print(f"You have {attempts} attempts left!")

    while not won and not lost: # loop ends if the player wins or looses

        guess = input_guess()
        if guess == secret_word:
            won = True
            break
        if guess in secret_word:  # checks if the word has the guess
            add_correct_guess(guess, correct_letters, secret_word)
        if guess in correct_letters or guess in used_letters:
            print("You already guessed this!")
        else:
            if guess not in used_letters:
                errors += 1
                attempts = 10 - errors
                used_letters.append(guess)
        lost = errors == 10
        if "_" not in correct_letters:
            won = True
        draw_hangman(errors)
        print(*correct_letters)
        if used_letters:
            print("\nWrong attempts: ")
            print(*used_letters)
            print("")
        else:
            print("")
        print(f"There are {str(correct_letters.count('_'))} missing letters ")
        print(f"You have {attempts} attemps left!")
    if won:
        when_win(secret_word)
    elif lost:
        when_loose(secret_word)
    print("\nGAME OVER!")


def add_correct_guess(guess, correct_letters, secret_word):
    position = 0
    for letter in secret_word:
        if guess.upper() == letter.upper():
            correct_letters[position] = guess
        position += 1


def game_title():
    print('*****************************************')
    print('********** Welcome to Hangman ***********')
    print('*****************************************')


def select_secret_word():
    words = []
    with open("words.txt", "r") as file:
        for word in file:
            word = word.strip()
            words.append(word)
    choose_word = random.randrange(0, len(words))
    secret_word = words[choose_word].upper()
    return secret_word


def start_correct_letters(word):
    return ["_" for letter in word]


def input_guess():
    guess = input("\nChoose a letter: ").upper()
    guess = guess.strip()  # "strip()" removes spaces if inputed
    return guess


def draw_hangman(errors):
    print("\n  _______     ")
    print(" |/      |    ")

    if errors == 0:
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    if errors == 8:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |     _/ \   ")

    if errors == 9:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |     _/ \_  ")

    if errors == 10:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |     _/|\_  ")

    print(" |            ")
    print("_|___         ")
    print()


def when_win(answer):
    print(f"\nYay, you win!\nAnswer: {answer}")
    print("      ___________      ")
    print("     '._==_==_=_.'     ")
    print("     .-\\:      /-.    ")
    print("    | (|:.     |) |    ")
    print("     '-|:.     |-'     ")
    print("       \\::.    /      ")
    print("        '::. .'        ")
    print("          ) (          ")
    print("        _.' '._        ")
    print("       '-------'       ")


def when_loose(answer):
    print(f"\nDamn, you lost!\nAnswer: {answer}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    play()
