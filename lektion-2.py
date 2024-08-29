# Used to print a welcome.
print("Hello and welcome to my program!")
# used this built-in function input, to ask for your name.
# Users name
Name = input("Whats your name, write your name: ")

# uses f to inform the print and write out
# Prints a hello and the users name
print(f"Hello {Name}! How fun that your here! :)")

print("How old are you?")

Age = input("Write your age: ")
AgeConfirm = input(f"Your {Age}? Type yes or no to confirm: ")
print(f"Thank you, so your {Age} years old. Your older than i thought")

# Convert age to int before math
Age_converted = int(Age)
if Age_converted >= 15:
    print("You can drive a motor bike")
else:
    print("🥸")
