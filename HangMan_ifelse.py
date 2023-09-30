import random  
import re       

with open("words.txt") as f:
    word_list = f.read().splitlines()

random_num = random.randint(0, len(word_list)-1)
word_chosen = word_list[random_num]

encoded_word = re.sub('[0-9a-zA-Z]', '-', word_chosen)

def guess(letter, word, encoded):
    # Checking if letter exist within the word
    found = False
    if letter in word:
        found = True
        # Replace the dashes with the letter
        for i in range(0, len(word)):
            if word[i] == letter:
                encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
    return (found, encoded)


# Initiate the game and prompt the user for their first selection
print("\nTime to guess a letter! You have %d lives remaining." % number_of_lives)
print(encoded_word)

while(number_of_lives > 0):
    guessed_letter = input("Your guess: ")[:1]

    letter_found, encoded_word = guess(guessed_letter, word_chosen, encoded_word)

    if not letter_found:
        number_of_lives -= 1
        if number_of_lives == 0:
            print("\nGame over, you lost! :( The word or phrase was '%s'" % word_chosen)
            break
        else:
            print("\nWhoops! That letter was not found. You now have %d lives remaining." % number_of_lives)
            print(encoded_word)
    else:
        if "-" not in encoded_word:
            print("\nYou won with %d lives remaining. The word or phrase was '%s'" % (number_of_lives, word_chosen))
            break
        else:
            print("\nGood job! That letter was found. You still have %d lives remaining." % number_of_lives)
            print(encoded_word)