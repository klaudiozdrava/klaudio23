lower = int(input("Πρόσθεσε έναν αριθμό:\n "))
upper = int(input("Πρόσθεσε έναν αριθμό:\n "))
d = int(input("Πρόσθεσε έναν αριθμό:\n"))
lista=[]
flag=0
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           lista.append(num)
megethos=len(lista)
for i in range (0,megethos):
   for j in range(0,megethos):
      check=abs((lista[i]-lista[j]))
      if(check==d):
         print("Ο αριθμός",d," προκύπτει αν |",lista[i],"-",lista[j],"|")
         flag=1
         break
   if (flag==1):
      break
if (flag==0):
      print("Δεν βρέθηκε ζέυγος πρώτων αριθμών")
   
