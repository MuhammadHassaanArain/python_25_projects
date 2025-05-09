import random
def main():
  print("Guess My Number! ")
  print("I am thinking of a number between 0 and 99...")
  secret_num = random.randint(0,99)
  user_guess = int(input("Enter a guess: "))
  while user_guess != secret_num:
    if user_guess > secret_num:
      print("Your guess is too high")
    elif user_guess < secret_num:
      print("Your guess is too low")
    user_guess = int(input("Enter a new number: "))
  print(f"Congrats! The number was: {secret_num}")


if __name__ == '__main__':
  main()