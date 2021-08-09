import random
import sys
import string
import time
import datetime as dt

# Slow print code
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

# All colors code
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    ORANGE = '\033[33m'
    PURPLE = '\033[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NEGATIVE1 = '\033[3m'
    NEGATIVE2 = '\033[5m'


# Main Menu

print_slow(f"{colors.CYAN}Simple 2FA In Python\n")
print_slow(f"Made With Python BY LyQuid{colors.END}")
print("")

# Generate Random 2FA
fa_generator = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 7
))

# 2FA
print(f"\n{colors.BLUE}2FA : {colors.END}")
print(f"{colors.CYAN}========={colors.END}")
print_slow(f"{colors.WARNING} {fa_generator}{colors.END}\n")
print(f"{colors.CYAN}========={colors.END}\n")

print_slow(f"{colors.ORANGE}2FA Answer: {colors.END}")
t = dt.datetime.now()
fa_answer = input("")

time_taken = dt.datetime.now ()-t

# 2fa Results

if(fa_answer == fa_generator):
  print_slow(f"{colors.GREEN}\nNice, 2FA Matches{colors.END}\n")
  print(f"{colors.WARNING}Time Taken :{colors.END} {colors.CYAN}{time_taken}{colors.END}")

else:
  print(f"{colors.FAIL}\nBruh, 2FA does not match{colors.END}")
  print(f"{colors.WARNING}Time Taken :{colors.END} {colors.CYAN}{time_taken}{colors.END}")
