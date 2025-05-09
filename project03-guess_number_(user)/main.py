import random
def main(num):
    low = 1
    high = num
    feedback = ""
    while feedback != "c":
      if low != high:
        guess_num = random.randint(low,high)
      else:
        guess_num = low
      feedback = input(f"Is {guess_num} too high (h),too low (l) or correct (c)??").lower().strip()
      if feedback not in ["c","l","h"]:
        print("❌Invalid Input Please Enter (c,l,h):")
        continue
      if feedback == "h":
        high = guess_num -1
      elif feedback == "l":
        low = guess_num +1
    print(f"The Computer guess the number 🎉 : {guess_num}")



if __name__ == '__main__':
  main(100)