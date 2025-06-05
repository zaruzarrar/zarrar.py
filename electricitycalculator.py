units=float(input("Enter the units consumed"))
if(units < 50):
    amount=units*3.95
    surcharge=75
elif(units<= 100):
       amount=units*7.74
       surcharge=85
elif(units<= 200):
       amount=units*14.16
       surcharge=95
else:
      amount=units*36.89
      surcharge=125
total=amount+surcharge
print("Your bill is :",total)

       

