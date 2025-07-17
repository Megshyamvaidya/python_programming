arr=[1,2,1,2,3,4,3,4,5,6,5,4,6,7,5,6,5,5,4,4,4]
hash_map={}
for num in arr:
    if num in hash_map:
        hash_map[num]+=1
    else:
        hash_map[num]=1
for key in hash_map:
    print(f"{key} occurs {hash_map[key]} times")