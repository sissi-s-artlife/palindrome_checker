print("Hello welcome to Palindrome Checker! Tell me the word you want to check.")
def is_palindrome(input_string):
    # Convert the input string to lowercase and remove spaces
    clean_string = ''.join(input_string.lower().split())

    # Check if the cleaned string is the same as its reverse
    return clean_string == clean_string[::-1]


# Get user input
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

