import random
import string

wordss = ["hello", "world", "Hello-world", "hello world", "python", "Javascript", "Typescript", "nextjs", "developer"]

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(wordss)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = len(word)

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and You have used these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Wrong guess!")

        elif user_letter in used_letters:
            print("You have already used that character!")
        else:
            print("Invalid Character. Please try again.")
    if lives == 0:
      print("You died, sorry! The word was ",word)
    else:
      print(f"\n🎉 You won! The word was '{word}'")

hangman()
