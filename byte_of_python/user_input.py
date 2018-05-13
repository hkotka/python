import re

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

user_input = input('Enter text: ')

#Remove special characters, empty spaces and puncutation marks from user input
user_input = re.sub('[^A-Za-z0-9]+', '', user_input)
user_input = user_input.lower()

if (is_palindrome(user_input)):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")

print(user_input)