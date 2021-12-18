
# // Time Complexity : O(n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # TC : O(n) 
        # SC : O(n)
        
        last_seen = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != last_seen:
                last_seen = nums[i]
                count = 0
                
            if nums[i] == last_seen:
                count += 1
            
            if count > 2:
                nums[i] = "X"
                
        new_list = list(filter(('X').__ne__, nums))
        nums[:] = new_list[:]
        

