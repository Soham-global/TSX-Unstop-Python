# Comparison of two numbers
num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number you want to compare : "))

if(num1 > num2):
    print("num1 is greater than num2")
elif(num2 > num1):
    print("num2 is greater than num1")
else:
    print(f"{num1} is equal to {num2}")