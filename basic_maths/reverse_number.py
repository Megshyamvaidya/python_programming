N=int(input("Enter a number = "))
rev_num=0
while N>0:
    digit=N%10
    rev_num=(rev_num*10)+digit
    N=N//10

print("The reversed number is ",rev_num)