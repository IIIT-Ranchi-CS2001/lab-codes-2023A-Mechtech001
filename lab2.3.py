# String Manipulation 3rd Question (Check if a string is a palindrome)

S = input("Enter a string: ")

cleaned_input = S.replace(" ", "").lower()

is_palindrome = cleaned_input == cleaned_input[::-1]

# Output
if is_palindrome:
    print(S, "is a palindrome.")
else:
    print(S, "is not a palindrome.")