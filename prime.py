n=int(input())
count=0
for i in range (1,n):
    if(n%i==0):
        count=count+1
        if(count==2):
            print(f"{i} is prime no")
        else:
            print(f"{i} is not prime no")

