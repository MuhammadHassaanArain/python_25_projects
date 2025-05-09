import time
import sys
def countdown(t):
  while t:
    mins,secs = divmod(t,60)
    # timer = '{:02d}:{:02d}'.format(mins,secs)
    # timer = f"{mins:02d}:{secs:02d}"
    # print(timer, end="\r")

    sys.stdout.write(f"\r{mins:02d}:{secs:02d}")
    sys.stdout.flush()
    time.sleep(1)
    t -= 1
  print("\n Go for a run now!")

user_input = input("Enter the time in second: ")
countdown(int(user_input))