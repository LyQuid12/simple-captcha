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


# Main Menu

print_slow("Simple Captcha Authentication\n")
print_slow("Made With Python BY LyQuid")
print("")

# Generate Random 2FA
key_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 7
))

# 2FA
print("\nCaptcha :")
print("=========")
print_slow(f"{key_code}\n")
print("=========\n")

print_slow("Captcha Code: ")
t = dt.datetime.now()
key_answer = input("")

time_taken = dt.datetime.now ()-t

# 2FA Results

if(key_answer == key_code):
  print_slow("\nNice, Captcha code matches\n")
  print(f"Time Taken : {time_taken}")
  print("")

else:
  print_slow("\nBruh, Captcha code does not match\n")
  print(f"Time Taken : {time_taken}")
