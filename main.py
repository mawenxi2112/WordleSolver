# need a list of possible 5 letter words DONE

# while loop
# 1. take input from user (word that they tried, the result BBBBG etc)
# 2. check result, and process word
# 3. print out words that can fall into to the result

import time

words = []
current_words = []

letter_options = {
    "0": "⬜️",
    "1": "🟩",
    "2": "🟨"
}

class Letter():

    def __init__(self, character, condition):
        self.character = character
        self.condition = condition


def convert_to_letter_list(word, conditions):
    letter_list = []

    for x in range(len(word)):
        letter_list.append(Letter(word[x], conditions[x]))

    return letter_list


def check_weighted_letter_from_list(letter, letter_list):
    current_letter = None

    for x in letter_list:
        if letter == x.character:
            if x.condition != '0':
                return True

    return False



with open('answer-list.txt') as f:
    lines = f.readlines()

    for line in lines:
        words.append(line.strip().lower())

    print("loaded possible words: " + str(len(words)) + "!\n")
    current_words = words


def possible_words(word_list, input_word, conditions):
    start_time = time.time()

    possible_word_list = []

    for word in word_list:
        invalid_letter_count = 0
        letter_list = convert_to_letter_list(input_word, conditions)

        for i, condition in enumerate(conditions):

            if condition == '0':
                invalid_letter_count = invalid_letter_count + 1

                if input_word[i] in word:
                    if not check_weighted_letter_from_list(input_word[i], letter_list):
                        break

                # check whether there is more than one substring of letter in word

                # if yes, we need to check the condition of that letter in conditions 
                # if condition is 1 or 2, we have to ignore.


            elif condition == '1':
                if word[i] != input_word[i]:
                    break

            elif condition == '2':
                if input_word[i] == word[i] or input_word[i] not in word:
                    break

            if invalid_letter_count == 5:
                break

            if i == len(conditions) - 1:
                possible_word_list.append(word)

    return possible_word_list, time.time() - start_time


while True:
    print("Example: adieu")
    print("")
    attempted_word = input("Enter word attempted: ").lower()
    print("")

    for item in letter_options:
        print(letter_options[item] + " = " + item)
    print("Example: 01220")
    print("")

    result_word = input("Enter word result:  ")
    print("")

    print(attempted_word)

    for result in result_word:
        print(letter_options[result], end=" ")

    print("\n")

    current_words, result_time = possible_words(current_words, attempted_word, result_word)

    print(str(len(current_words)) + " possible results out of " + str(len(words)))
    print("results took: " + str(result_time) + "s to return")

    for word in current_words:
        print(word)

    print("-------------------------------------------------")
