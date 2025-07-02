def print_Megshyam(n):
    if n==0:
        return
    print("Megshyam") #prints first
    print_Megshyam(n-1) #recursive call later
print_Megshyam(5)


def print_vivek(n):
    if n==0:
        return
    print_vivek(n-1) #recursive call first
    print("vivek") #prints after recursion 
print_vivek(5)