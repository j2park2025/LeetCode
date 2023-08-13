class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = (len(nums))-1 #left 0 right 0
        mid = int(right+left/2) # undefined (0+0/2)
        while (left<=right): # target when
            if (nums[mid] == target):
                return mid # supposed to print
            elif (nums[mid] > target): # ex1 = mid:2, nums[mid] = 3 > 9?
                right = mid-1
                mid = int(right+left/2)
                # remove the center number if that numbe is not the number
            elif (nums[mid] < target): # ex1 = mid:2, nums[mid] = 3 < 9 O
                left = mid+1 # left = 원래 0, mid = 2+1 left 가 3 right 는 아직 5
                mid = int(right+left/2) # 4
        # if (target<nums[0]) or (target>nums[len(nums)-1]):
        return -1
        # elif (len(nums)==1) or (len(nums)==2):
        #     for i in range(len(nums)):
        #         if (nums[i] == target):
        #             return i
        #     return -1
        # else:
        #     return -1
    '''

    when target is not in nums:
    1) when the target is not within the limit of nums[0] and nums[len(nums)]
    2) when the target is within the limit of the nums but is just not listed there

    nums = [int, int2, int3, int4......., intn]
    int(len(nums)/2) --> the 대충 반띵한 숫자
    target = 9 찾아야하는 숫자

    example 1:
    nums = [-1, 0, 3, 5, 9, 12]
    nums # [0,  1, 2, 3, 4,  5]

    numb = int(((len(nums which is 6))-1)/2) = 5/2 int = 3
    nums[3] = 5
    근데 5!=9, 5>=9 X, 5<9 --> numb = 3 + 2
    '''