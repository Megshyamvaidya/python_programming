def contains_duplicate(arr):
    hash_map={}
    for num in arr:
        if num in hash_map:
            return True
        else:
            hash_map[num]=1
    return False
arr=[1,2,3,3,4,5]
print(contains_duplicate(arr))