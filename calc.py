

num1 = int(input("Enter the first number you want to include in this operation. >"))
num2 = int(input("enter the second number you want to include in this operation. >"))
operator = input("What is the operand you would like to use? (enter in the sign for it, e.g exponent = **, addition = +) >")
print("Please note that if you are using exponents, the first number you enter is going to be the base, and the second the power.")

if operator == "+":
    print(f"The result of {num1} being added to {num2} is {num1+num2}")
if operator == "/":
    print(f"The result of {num1} being divided by {num2} is {num1/num2}")
if operator == "-":
    print(f"The result of {num1} subtracted by {num2} is {num1-num2}")
if operator == "**":
    print(f"The result of {num1} raised to the power of {num2} is {num1**num2}")
if operator == "*":
    print(f"The result of {num1} and {num2} being multiplied is {num1 * num2}")
if operator not in ["+","-","/","**","*"]:
    print("Invalid operator. Maybe you meant to choose a different option?")

other_stuff = bool(input("Do you want to continue to use the calculator for other functions? Type in True if yes, and False if no. "))

while other_stuff:
    print("We have other operations that you can use as well.")
    print("odd-even - checks if a number is odd or even \n prime - is the number a prime?")
    new_ops = input("What is your choice here?")
    if new_ops == "odd-even":
        inp = int(input("What is the number you would like to check?"))
        result = "odd" if inp%2 != 0 else "even"
        print(f"The number {inp} is {result}.")
    if new_ops == "prime":
        inp = int(input("What is the number you would like to check? "))
        output_list = []
        n = 1
        for i in range(2,inp):
            n += 1
            output_list.append(n * i)
        if inp not in output_list:
            print(f"{inp} is prime.")
        else:
            print(f"{inp} is not prime.")
        
        