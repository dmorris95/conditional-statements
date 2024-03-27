#Task 1

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the final number: "))

if number1 >= number2 and number1 >= number3:
    print("The largest number is: " + str(number1))
elif number2 >= number1 and number2 >= number3:
    print("The largest number is: " + str(number2))
elif number3 >= number1 and number3 >= number2:
    print("The largest number is: " + str(number3))


#Task 2
    
if number1 <= number2 and number1 <= number3:
    print("The smallest number is: " + str(number1))
elif number2 <= number1 and number2 <= number3:
    print("The smallest number is: " + str(number2))
elif number3 <= number1 and number3 <= number2:
    print("The smallest number is: " + str(number3))


#Task 3
    

if number1 == number2:
    print("We have numbers that are equal, the number is: " + str(number1))
elif number2 == number3:
    print("We have numbers that are equal, the number is: " + str(number2))
elif number1 == number3:
    print("We have numbers that are equal, the number is: " + str(number3))