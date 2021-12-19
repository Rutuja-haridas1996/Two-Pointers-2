
# // Time Complexity : O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Three line explanation of solution in plain english

# // Your code here along with comments explaining your approach


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) :
        """Do not return anything, modify nums1 in-place instead."""
        # TC : O(c)
        # SC: O(1)  
        p1 = m - 1
        p2 = n - 1
        for i in range(len(nums1)-1,-1,-1):
            if p2 < 0:
                break;
            
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
