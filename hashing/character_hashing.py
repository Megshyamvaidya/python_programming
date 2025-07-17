s='Megshyamvaidya'
hash_map={}
for char in s:
    if char in hash_map:
        hash_map[char]+=1
    else:
        hash_map[char]=1
for char in hash_map:
    print(f'{char} appears {hash_map[char]}')