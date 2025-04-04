def kthSmallest(arr,k):
        if len(arr) < k:
            return []
            
        set_l = list(set(arr))
        set_l.sort()
        
        return set_l[k-1]

num = list(map(int,input().split()))
k = int(input())
print(kthSmallest(num,k))