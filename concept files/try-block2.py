''' this code check the entered age and raise custom exceptions 
    if the age is negative or below 18. 
    The except block catches these exceptions and prints the corresponding error messages.'''

try:
    # Code that may raise an exception
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Access granted.")
except ValueError as v:
    print("Error:", str(v))
