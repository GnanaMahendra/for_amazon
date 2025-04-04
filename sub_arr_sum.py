def subarraySum(arr, target):
        # code here
        start = 0
        current_sum = 0
        found= False
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            while current_sum > target and start <= i:
                current_sum -= arr[start]
                start += 1
                
            if current_sum == target :
                
                return [start+1, i+1]
        return [-1]

nums = list(map(int,input().split()))
k = int(input())
print(subarraySum(nums,k))