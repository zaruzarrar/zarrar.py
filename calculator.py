def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select a option")

print("1. Add")

print("2. Subtract")

print("3. Multiply")

print("4. Divide")

choice =(input("Enter your age: "))
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))


if choice == '1':
      print("Result:", num1 + num2)
elif choice == '2':
      print("Result:", num1 - num2)
elif choice == '3':
     print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid input")
