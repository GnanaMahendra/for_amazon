def findDuplicates(arr):
    # code here
    arr_set = set(arr)
    
    fr={}
    result = []
        
    for num in arr:
        if num in fr:
            fr[num] += 1
        else:
            fr[num] = 1
                
    for key in fr:
        if fr[key] > 1:
            result.append(key)
    return result

nums = list(map(int,input().split()))
print(findDuplicates(nums))