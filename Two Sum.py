class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        position = {}
        for n in range(len(nums)):
            if nums[n] in position:
                position[nums[n]].append(n)
            else:
                position[nums[n]] = [n]


        nums.sort()
        for i in range (len(nums)):
            if (nums[left] + nums[right])>target:
                right-=1
            elif (nums[left] + nums[right])<target:
                left+=1
            elif (nums[left] + nums[right])==target:
                return [position[nums[left]][0], position[nums[right]][-1]]
            # [[0], [1]]
            # if run == True: 
            #     break
            # for j in range (i+1, len(nums)):
            #     if run == True:
            #         break
            #     if ((nums[i] + nums[j])==target):
            #         run = True
            #         return [i, j]
    # {6: [0], 8: [1], 5:[2, 4], 7:[3], 10:[5]}
    # 6, 8, 5, 7, 5, 10 -> 14
 #   smaller --> (from the front)
 #   greater <-- (from the back)