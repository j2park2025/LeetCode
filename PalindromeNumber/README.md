#Palindrome Number

[Question Link](https://leetcode.com/problems/palindrome-number/)

The input value of the code is "x," which is the number that we need to assess whether it is a palindrome or not. 

This program first distinguishes out any negative values as they are all not palindromes. Then, it sets a variable called "rev" equal to 0 along with another variable called "orig" set to x (input). While x is not equal to 0, the rev value will be set equal to (rev*10 + x%10) (% is the calculation of the modulus of the value divided). Then, x will be redefined by being divided by 10 and rounded to the nearnest whole number (//). When the x value has been divided so many times that it becomes 0, the while code stops. The result will be printed as either true of false depending on whether the original number and the flipped number are the same. If they are the same, the result will be true. (Same for vice versa) The original code looks like the bottom for easier comprehension:

if x < 0:
    return False 
rev = 0
orig = x #121
while x != 0:
    rev = rev *10 + x%10 #1 -> 10 + 2
    x = x//10 #12 
return rev == orig