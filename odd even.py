def check_number():
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    elif num % 2 != 0:
        print(f"{num} is an Odd number.")

# Call the function
check_number()