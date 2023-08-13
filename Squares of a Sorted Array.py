class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        # for i in range(len(nums)):
        #     front = abs(nums[i])*abs(nums[i]) #16
        #     back = abs(nums[len(nums)-1-i])*abs(nums[len(nums)-1-i]) #100
        #     if front>back: # 16>100 X
        #         result.append(front)
        #     elif front<back: #16<100 O
        #         result.append(back)
        #     elif front==back:
        #         result.append(front)
        #         result.append(back)
        #     if (len(result)==len(nums)):
        #         break
        # result.reverse()
        # return result

        f = 0
        b = 0
        while (len(result)!=len(nums)):
            front = abs(nums[f])*abs(nums[f]) # 1) f=0, 4*4=16 2) f=0 16 3) 1*1=1 4) 1
            back = abs(nums[len(nums)-1-b])*abs(nums[len(nums)-1-b]) # 1) b=0, nums[5-1-0=4]=10*10=100 2) b=1 nums[5-1-1=3] 3*3=9 3) 9 4) 0*0=0
            if front>back: # 1) 16>100 no 2) 16>9 yes 3) 1>9 no 4) 1>0 yes
                result.insert(0, front) # result=[16,100] result=[1,9,16,100]
                f += 1
            elif front<back: #16<100 yes 2) 1<9 yes
                result.insert(0, back) # result=[100] result=[9,16,100]
                b += 1
            elif front==back:
                if f!=(len(nums)-1-b):
                    result.insert(0, front)
                    result.insert(0, back)
                    f += 1
                    b += 1
                elif f==(len(nums)-1-b):
                    result.insert(0, front)
                    break
            if (len(result)==len(nums)): #no #no #no
                break
        return result