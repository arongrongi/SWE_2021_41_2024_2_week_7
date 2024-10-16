from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
    
    num_arr = {}
    
    for i, num in enumerate(nums):
        
        result = target - num
        
        if result in num_arr:
            return [num_arr[result], i]
        
        num_arr[num] = i
    
    return []
