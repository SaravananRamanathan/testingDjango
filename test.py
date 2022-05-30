from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
       hashmap = {}
       for i in range(len(nums)):
           complement = target - nums[i]
           print(i,target,nums[i],complement)
           if complement in hashmap:
               return [i, hashmap[complement]]
           hashmap[nums[i]] = i
           

input_list = [2,8,19,15,1]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))