def print_num(n):
    if n==0: #base case
        return
    print(n)
    print_num(n-1)
print_num(12)