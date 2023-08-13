class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        if (x<0):
            return False
        elif (x>=0) and (x<10):
            return True
        elif (x>=10):
            y = str(x) #'11'
            for i in range(len(y)//2): #0, 1, 2
                if(y[len(y)-(i+1)]!=y[i]): #if 1==1 if 2=
                    return False
            return True
        """

        if x < 0:
            return False 
        rev = 0
        orig = x 
        while x != 0:
            rev = rev *10 + x%10 
            x = x//10
        return rev == orig

            #12344321 
            #321
            # if (cue == False):
            #     return false
            # elif (cue == True):
            #     return true
            # 1) '121' string -> list
            # 2) 121%10*10
            # 121//10

            # (10 + 12%10)*10 = 120
            # 1

            # 120 + 1%10 = 121
'''
            integer = x # integer = 1000021
            counts = 0
            while x>=1: # counts = 7
                x=x/10
                counts+=1
            liist = []
            for i in range (counts):
                # (integer)-int(integer/10)
                liist.append((integer)-(int(integer/10))*10)
                integer = int(integer/10)
            ind = 0
            ll = len(liist) # 7
            for o in range (int(len(liist)/2)): #range = 3, 0, 1, 2
                if (liist[o]!= liist[ll-1-o]) and ((o+1)< int(ll/2)+1):
                    ind = 1
                    return False
                    break
            if ind == 0:
                return True
'''                    
# 9283-9280 og-step1*10 = one digit
# 928-920 step1-step2*10 = 10s
# 92