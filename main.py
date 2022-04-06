import random
import sys
import string
import time
import datetime as dt

# Slow print code
def slow_print(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


# Main Menu

slow_print("Simple Captcha Authentication\n")
slow_print("Made With Python BY LyQuid")
print("")

# Generate Random Captcha
key_code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 7
))

# Captcha
print("\nCaptcha :")
print("=========")
slow_print(f"{key_code}\n")
print("=========\n")

slow_print("Captcha Code: ")
t = dt.datetime.now()
key_answer = input("")

time_taken = dt.datetime.now ()-t

# Captcha Results

if key_answer == key_code:
	slow_print("\nNice, Captcha code matches\n")
	print(f"Time Taken : {time_taken}")
	print("")

else:
	slow_print("\nBruh, Captcha code does not match\n")
	print(f"Time Taken : {time_taken}")
