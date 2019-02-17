n=int(input("Εισήγαγε έναν αριθμό"))
factors=[]
#find prime numbers
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=1):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            factors.append(i)
    i=i+1
m=n
print("Η ανάλυση ως γινόμενο πρώτων ειναι:")
y=len(factors)# division
while(n>1):
    k=0
    for i in range (0,y):
        if k==0:
            if (n%factors[i]==0):
                n=(n/factors[i])
                if (n==1):
                    print(factors[i],"=",m,end='')
                else:
                    print(factors[i],"* ",end='')
                k=1

