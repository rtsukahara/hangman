import random


def hangman():
    word_list = ["Python", "Java", "PHP", "Ruby","C++"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guess = 0
    stages = ["",
              "______      ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /|\    ",
              "|     |     ",
              "|    / \    ",
              "|           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong_guess < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong_guess += 1
        print(" ".join(board))
        e = wrong_guess + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win! The word was:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:worng_guess + 1]))
        print("You lose! The words was {}.".format(word))


hangman()
