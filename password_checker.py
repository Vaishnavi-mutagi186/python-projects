import re

password = input("Enter password: ")

strength = 0

if len(password) >= 8:
    strength += 1
    print("✔ Length is sufficient")
else:
    print("✘ Password too short")

if re.search("[A-Z]", password):
    strength += 1
    print("✔ Contains uppercase letter")
else:
    print("✘ Missing uppercase letter")

if re.search("[a-z]", password):
    strength += 1
    print("✔ Contains lowercase letter")
else:
    print("✘ Missing lowercase letter")

if re.search("[0-9]", password):
    strength += 1
    print("✔ Contains number")
else:
    print("✘ Missing number")

if re.search("[@#$%^&*()!]", password):
    strength += 1
    print("✔ Contains special character")
else:
    print("✘ Missing special character")

print("\nPassword Strength:")

if strength <= 2:
    print("WEAK ❌")
elif strength == 3 or strength == 4:
    print("MEDIUM ⚠️")
else:
    print("STRONG ✅")
