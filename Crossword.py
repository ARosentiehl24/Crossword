import numpy as game


def main():
    words = game.array(["dog", "cat", "lion", "bear"])
    crossword = game.array([["B", "F", "D", "O", "G"],
                            ["C", "E", "O", "L", "L"],
                            ["A", "F", "A", "I", "I"],
                            ["T", "R", "G", "R", "O"],
                            ["Z", "W", "R", "H", "N"]])

    words_found = []
    keep_playing = 1

    while keep_playing == 1 and len(words_found) != len(words):
        word = ""

        print("\nWords to found:", words)

        print("\n", crossword, "\n")

        initial_x = int(input("Set initial x: "))
        initial_y = int(input("Set initial y: "))
        final_x = int(input("Set final x: "))
        final_y = int(input("Set final y: "))

        print()

        if initial_x == final_x:
            for i in range(initial_y, final_y + 1, 1):
                word += crossword[initial_x][i]
        elif initial_y == final_y:
            for i in range(initial_x, final_x + 1, 1):
                word += crossword[i][initial_y]
        elif (initial_x - final_x) == (initial_y - final_y):
            for i in range(initial_x, final_x + 1, 1):
                word += crossword[i][i]

        if (word.lower() in words) and (word.lower() not in words_found):
            words_found.append(word)

            if initial_x == final_x and initial_y != final_y:
                for i in range(initial_y, final_y + 1, 1):
                    crossword[initial_x][i] = str(crossword[initial_x][i]).lower()
            elif initial_y == final_y and initial_x != final_x:
                for i in range(initial_x, final_x + 1, 1):
                    crossword[i][initial_y] = str(crossword[i][initial_y]).lower()
            elif (initial_x - final_x) == (initial_y - final_y):
                for i in range(initial_x, final_x + 1, 1):
                    crossword[i][i] = str(crossword[i][i]).lower()

            print("Word selected", word)
            print("You found", word, "words found", len(words_found))
        else:
            print("You don't found words")

        print()

        if len(words_found) != len(words):
            keep_playing = int(input("Do you want keep playing? (1 = yes : 0 = no): "))

            while keep_playing != 0 and keep_playing != 1:
                keep_playing = int(input("Invalid input, do you want keep playing? (1 = yes : 0 = no): "))
        else:
            print("¡You win!")

        print("-----------------------------------------------")

    return 0


main()
