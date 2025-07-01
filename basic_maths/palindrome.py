N=int(input("Enter a number ="))
original_number=N
reversed_number=0
while N>0:
    last_digit=N%10
    reversed_number=(reversed_number*10)+last_digit
    N=N//10
if original_number==reversed_number:
    print("Entered number is palindrome")
else:
    print("Entered number is not a palindrome number")