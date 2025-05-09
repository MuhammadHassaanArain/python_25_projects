def main():
  try:
    print("Welcome to Mad Libs: A Day at the Zoo! 🦁🐵")
    adjective = input("Enter an Adjective: ")
    animal = input("Enter an Aminal Name: ")
    verb = input("Enter a verb: ")
    story = f"The {adjective} {animal} loves to {verb}!"
    print(f"Here's your mad libs story: {story} \n")
  except ValueError:
    print("❌ Invalid Input!")
if __name__ == '__main__':
  main()