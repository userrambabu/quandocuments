import random
import colorama

# Initialize colorama to work with Windows, Linux, and macOS terminals
colorama.init()

# Example usage
print(colorama.Fore.RED + "This text is in red color.")
print(colorama.Fore.GREEN + "This text is in green color.")
print(colorama.Fore.BLUE + "This text is in blue color.")

# Reset the color to the default (usually white) for the rest of the output
print(colorama.Style.RESET_ALL + "This text is back to the default color.")

lives = 3

words = ['pizza', 'fairy', 'teeth', 'shirt', 'water', 'band']
secret_word = random.choice(words)

clue = list('?????')
heart_symbol = u'\u2764'

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1

if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
