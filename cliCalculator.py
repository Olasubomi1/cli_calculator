# A CLI calculator application

# Operations the calculator can perform
print("Welcome to my simple CLI calculator")
operations = ['+', '-',
              '/', '*', '%']


print("what operation would you like to perform. [+, -, /, *, %]")
# A while loop that re-iterates to get the type of operation and then performs the operation given the input
is_running = True
while(is_running):
    try:
        terminalInput = input(
            "Enter type of operation you would like to perform: ").strip().lower()
        if terminalInput in operations:
            pass
        else:
            continue
    except:
        print("Invalid operation")
    try:
        # Getting the first number
        first_number = float(input("enter first number: "))
        # Getting the second input
        second_number = float(input("enter second number: "))

    except:
        print("invalid number")
        continue

    if terminalInput in operations:
        if terminalInput == "+":
            print("your answer is: ", first_number + second_number)
        if terminalInput == "-":
            print("your answer is: ", first_number - second_number)
        if terminalInput == "/":
            print("your answer is: ", first_number / second_number)
        if terminalInput == "*":
            print("your answer is: ", first_number * second_number)
        if terminalInput == "%":
            print("your answer is: ", first_number % second_number)
    another_calculation = input(
        "Would you like to perform another calculation: [y/n]")
    if another_calculation == "y":
        continue
    else:
        is_running = False
print("Thank you for using our service. bye bye")
