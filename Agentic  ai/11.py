'''Lst1=[10,20,30]
Lst2=[40,50,60]
Lst3=Lst1+Lst2
print(Lst1)
print(Lst2)
print(Lst3)'''

'''Lst=[10,20,30,40,50,60,70]
print(Lst[0])
print(Lst[::])
print(Lst[1:5])
print(Lst[::2])
print(Lst[-2:-5:])
print(Lst[-2:-5:-1])
print(Lst[::-1])'''

profits=[200,450,300]
max_profit=profits[0]
for p in profits:
    if p>max_profit:
        max_profit=p
print("Highest  Profit:",max_profit)
