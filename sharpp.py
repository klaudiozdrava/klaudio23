tab=[]

pro=input("Εισάγετε ένα αρχείο \n")

f=open(pro+".py","r", encoding="utf-8")

for line in f:
  
  tab.append(line)
  
  megethos=len(tab)
  
for i in range(0,megethos):
  
  print((tab[i].partition('#'))[0])
  
f.close()          

