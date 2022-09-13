import string

password = input("Enter a password: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('10-million-password-list-top-1000000.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common password list. Score: 0")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 16:
    score += 1
print(f"Password length is {str(length)}, adding {str(score)} point(s).")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) -1)} points.")

if score < 3:
    print(f"This password is very weak. Score: {str(score)} / 6")
elif score == 3:
    print(f"This password is average. Score: {str(score)} / 6")
elif score > 3 and score < 5:
    print(f"This password is good! Score: {str(score)} / 6")
elif score > 5:
    print(f"This password is strong! Score: {str(score)} / 6")
