for i in range(5):
    for j in range(5):
        if(i==0 or j==0 or j==4 or i==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
