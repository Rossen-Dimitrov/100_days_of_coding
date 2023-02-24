from replit import clear
import random
from hangman_word_list import word_list
import hangman_arts


print(hangman_arts.logo)

word = random.choice(word_list)

display_word = ["_"] * len(word)
print(*display_word)

lives = 6
used_letters = []
while True:
    user_letter = input("Enter a letter: ").lower()
    clear()
    if user_letter in used_letters:
        print(f'You already guessed letter {user_letter}')
        continue
    used_letters += user_letter
    if user_letter in word:
        for i in range(len(word)):
            if user_letter == word[i]:
                display_word[i] = user_letter
        print(*display_word)
    else:
        print(hangman_arts.stages[lives])
        lives -= 1

    if "_" not in display_word:
        print("You Won")
        break
    elif lives == 0:
        print("You Loose")
        print(hangman_arts.stages[0])
        break
