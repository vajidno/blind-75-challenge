def containsDuplicate(arr:list[int])->bool:
    num_set = set()
    for i in range(len(arr)):
        if arr[i] not in num_set:
            num_set.add(arr[i])
        else:
            return True
    return False        

print(containsDuplicate([1,2,3,1]))