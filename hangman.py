import random

words = ['apple', 'banana', 'cherry', 'orange']
word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6

while tries > 0 and '_' in guessed:
    print(' '.join(guessed))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if '_' not in guessed:
    print("You win! The word was", word)
else:
    print("You lose! The word was", word)
