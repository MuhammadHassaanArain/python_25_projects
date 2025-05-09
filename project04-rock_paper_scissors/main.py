import random
def main():
  choices = ["rock","paper","scissor"]
  comp_selected = random.choice(choices)
  print("Select one of the following.")
  print("1 Rock")
  print("2 Paper")
  print("3 Scissor")
  try:
    user_selected = int(input("Type Your choice here: ").strip())
    if user_selected not in [1, 2, 3]:
      print("❌ Please select 1, 2, or 3.")
      return
  except ValueError:
      print("❌ Invalid Input. Please enter a number (1, 2, or 3).")
      return

  user_choice = choices[user_selected -1]
  print(f"🧑‍💻 You selected: {user_choice}")
  print(f"🖥️ Computer selected: {comp_selected}")
  if user_choice == comp_selected:
    print("It's a tie! 🤝")
  else:
    winning_cases = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper"
        }
    if winning_cases[user_choice] == comp_selected:
      print("You win 🎉")
    else:
      print("You lose 😢")


if __name__ == '__main__':
  main()