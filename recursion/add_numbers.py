def add(a,b):
    if b==0: #base case "stops the function"
        return a
    return add(a+1,b-1) #-->this will keep calling until a specified condition is met
result=add(3,6) #function called 
print(result)



