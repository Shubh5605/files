1# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result 
def divide(num1, num2):
    if num2 ==0:
        return("Error! Division by zero")
    else:
        return num1/num2
def multiply(num1, num2):
    return num1 * num2
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
print("Please select operation -\n"  \
      "1. Divide\n" \
      "2. Multiply\n" \
      "3. Add\n" \
      "4. Subtract\n")
select = int(input("Select operation from 1, 2, 3, 4 :"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if select == 1:
    print(num1,"/", num2,"=",divide(num1,num2))
elif select == 2:
 print(num1,"*", num2,"=",multiply(num1,num2))
elif select == 3:
     print(num1,"+", num2,"=",add(num1,num2))
elif select == 4:
     print(num1,"-", num2,"=",subtract(num1,num2))
else:
     print('Invalid input')

     
