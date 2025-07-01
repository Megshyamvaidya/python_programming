N=int(input("Enter a number = "))
original_number=N
sum=0
while N>0:
    last_digit=N%10
    sum=sum+(last_digit**3)
    N=N//10
print(sum)
if sum==original_number:
    print(f"Entered number {N} is armstrong number ")
else:
    print(f"Entered number is not an armstrong number")