try:
    # Code that may raise exceptions
    x = int(input("Enter a number: "))
    result = 10 / x
    print("The result is:", result)
except Exception as e:
    print("Error:", str(e))   #----this code takes all kind of error msg and return it as a str