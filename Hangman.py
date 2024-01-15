import random
from Hangman_words import word_list
from Hangman_art import logo
from Hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)
# print(chosen_word)

display = []

for char in range(word_length):
    display.append("_")
end_of_game = False
while not end_of_game:
    guess = input("Guess a number:").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    # print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
