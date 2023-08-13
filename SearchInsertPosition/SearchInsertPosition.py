class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)-1 #3
        left = 0
        mid = length #3
        right = length
        while (right-left)>=0: # mid = int((left + right) / 2)
            mid = int((left + right) / 2)
            # left = 0, right = 3, mid = 1
            if target==nums[mid]: # ex 1 if 5==6 no ex 2 if 2==6 no 
                return mid #
            elif target<nums[mid]: # ex 1 if 5<6 yes ex 2 if 2<6 yes
                right = mid-1 # half 3/2 = 1.5 right=1
            elif nums[mid]<target: # ex 2 
                left = mid+1
        return left

# 1, 2, 3, 4, 5, 6, *7*, 8, 9, 10, 11, 12, 13
# 13/2 = 6.5=7-1 = 6
# ex, target = 11
# 6*3/2 = 9
# if left right 