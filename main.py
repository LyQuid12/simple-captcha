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

print_slow(f"{colors.CYAN}Simple Captcha Authentication\n")
print_slow(f"Made With Python BY LyQuid{colors.END}")
print("")

# Generate Random 2FA
key_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 7
))

# 2FA
print(f"\n{colors.BLUE}Captcha : {colors.END}")
print(f"{colors.CYAN}========={colors.END}")
print_slow(f"{colors.WARNING} {key_code}{colors.END}\n")
print(f"{colors.CYAN}========={colors.END}\n")

print_slow(f"{colors.ORANGE}Captcha Code: {colors.END}")
t = dt.datetime.now()
key_answer = input("")

time_taken = dt.datetime.now ()-t

# 2FA Results

if(key_answer == key_code):
  print_slow(f"{colors.GREEN}\nNice, Captcha code matches{colors.END}\n")
  print(f"{colors.WARNING}Time Taken :{colors.END} {colors.CYAN}{time_taken}{colors.END}")
  print("")

else:
  print_slow(f"{colors.FAIL}\nBruh, Captcha code does not match{colors.END}\n")
  print(f"{colors.WARNING}Time Taken :{colors.END} {colors.CYAN}{time_taken}{colors.END}")
