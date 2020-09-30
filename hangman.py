#!/usr/bin/env python3
# hangman.py

def hangman(word):
    stages = [ ""
              ,"-----------         "
              ,"|         |         "
              ,"|         |         "
              ,"|         O         "
              ,"|        /|\        "
              ,"|        / \        "
              ,"|                   "
]

    wrong = 0
    board = ["_"] * len(word)

    print("Welcome to Hangman")
    while wrong < len(stages):
        print("===================================")
        char = input("Guess a letter: ")

        char_pos = word.find(char)
        if char_pos >= 0:
            board[char_pos] = char
        else:
            wrong += 1
            print("\n".join(stages[:wrong]))

        print(" ".join(board))

        if "_" not in board:
            print("You win!")
            break
    else:
        print("You lose! It was {}.".format(word))

hangman("cat")
