
'''weight=float(input("enter weight in kg:"))
height=float(input("enter height in meters:"))
bmi=weight/(height**2)
if bmi<18.5:
    category="underweight"
elif bmi<25:
    category="normal"
elif bmi<30:
    category="overweight"
else:category="obese"
print("BMI:", bmi)
print("category:", category)'''

'''units=int (input("enter the units used:"))
if units<=100:
    bill=units*1
elif units<=200:
    bill=100*1+(units-200)*2
else:
    bill=100*1+100*200+(units-200)*5
    print("electricity Bill:₹",bill)'''




'''a=int(input("enter the first angle:"))
b=int(input("enter the second angle:"))
c=int(input("enter the third angle:"))
if a==b and b==c and c==a:
    print("Eqilateral Traingle")
elif a==b or b==c or c==a:
    print("Isosceles Traingle")
else:
    print("Scalene Traingle")'''

age= int(input("enter the age:"))
if age>=18:
    print("allowed for match")
    if age>=18 and age<30:
        print("2$ ticket price")
    elif age>=30 and age<60:
        print("1$ ticket price")
    else:
        print("o$ ticket price")
else:
    print("not allowed for match")
  