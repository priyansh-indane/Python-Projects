#Creating password_check function
def password_check(PASSWORD):
    ## Check length of password.
    if len(PASSWORD) < 8:
        return "Please enter a password of 8 characters or more."
    
    ## Check all characters are present in PASSWORD.
    has_upper = any(char.isupper() for char in PASSWORD) # Rule 1
    has_lower = any(char.islower() for char in PASSWORD) # Rule 2
    has_digit = any(char.isdigit() for char in PASSWORD) # Rule 3
    
    ## Check All conditions are met using "AND" logic.
    if has_upper and has_lower and has_digit:
        return "Password is valid!"
    else:
        return "Password must contain uppercase, lowercase, and a digit."

## Get input from the user.
user_input = input("Please enter a valid password: ")

## Calling the function to check wheather password is valid or not.
result = password_check(user_input)
print(result)
