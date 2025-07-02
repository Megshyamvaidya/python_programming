def print_num(i,n):
    if i>n:
        return
    print(i)
    print_num(i+1,n)
print_num(1,10)