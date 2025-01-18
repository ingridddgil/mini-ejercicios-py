import random
words = ['python', 'java', 'swift', 'kotlin']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome 2 Hangman. U have to guess what is the word behind the underscores!.\nAre u ready?? Let\'s begin!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Type a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveal letter
    else:
        print(f"That letter doesn\'t appear in the word. U have {attempts - 1} attempts")
        attempts -= 1
else:
    print(f"U ran out of attempts, the word was {chosen_word}:(")


if '_' not in word_display:
    print("you guessed the word!", " ".join(word_display), "You survived! :)", end=" ")

