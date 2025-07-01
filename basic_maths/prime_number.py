N=int(input("Enter a number ="))
count=0
for i in range (1,N+1):
    if N%i==0:
        count=count+1
if count==2:
      print("Entered number is prime ")
else:
     print("Entered number is not a prime number")