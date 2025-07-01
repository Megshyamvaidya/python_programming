N=int(input("Enter a number= "))
count=0 
while N>0:
    N=N//10
    count=count+1
print("Number of digits=",count)