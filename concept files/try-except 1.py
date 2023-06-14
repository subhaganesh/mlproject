try:
    # Code that may raise exceptions
    x = int(input("Enter a number: "))
    result = 10 / x
    print("The result is:", result)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:                #---if the error dont falls into the above two errors it will output the error msg which was occured
    print("Error:", str(e))          
