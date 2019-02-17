import random

x=int(input("Παρακαλω εισάγετε σειρές"))
y=int(input("Παρακαλω εισάγετε στείλες"))
z=int(input("Παρακαλω εισάγετε βόμβες"))
ginomeno=x*y
if x==y:
    print("Δώσε διαφορετίκο συνδυασμό σειρών και στείλων")
elif z>ginomeno:
    print("Υπερβολικές βόμβες")
#board
else:
    tab=[]#building the board
    for i in range(x):
        ser=[]
        for j in range(y):
            ser.append(0)
        tab.append(ser[:])
    b_set=set()
    while z>0:
        i=random.randint(0,x-1)
        j=random.randint(0,y-1)
        if not((i,j) in b_set):
            b_set.add((i,j))
            z=z-1
    for elem in b_set:
        tab[elem[0]][elem[1]]=1
    for i in range(x):
        for j in range(y):
            print(tab[i][j],end=' ')
        print("\n",end='')

        
    
