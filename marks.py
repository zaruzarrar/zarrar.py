print("Please Enter  Your marks:")
English=int(input("Enter Your marks in English:"))
Maths=int(input("Enter Your marks in Maths:"))
Coding=int(input("Enter Your marks in Coding:"))
Science=int(input("Enter Your marks in Science:"))
Chemistry=int(input("Enter Your marks in Chemistry:"))
Total= English+Maths+Coding+Science+Chemistry
percentage=Total/500
P=percentage*100
print('The final percentage is',P)
