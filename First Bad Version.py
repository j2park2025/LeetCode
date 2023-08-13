# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # lis = [1, 2, 3, 4, 5] #lis = [1]
        left = 1
        right = n
        if n == 1:
            return n
        while left<=right: 
            mid = int((right+left)/2) # mid = 2 # mid = 3 
            #lis = [1, 2, 3, 4, 5], mid = 2, left = 0, right = 4 # mid = 3, left = 3, right = 4 
            if isBadVersion(mid)==False: #false = 정상 #ex1: yes ex1: no
                left = mid + 1 #left = 3, mid = 2, right = 4 
            elif isBadVersion(mid)==True: #true = malfunctioning #ex1: no ex1: yes
                if (isBadVersion(mid-1)==False) or (mid == 1): 
                    return mid
                else:
                    right = mid -1