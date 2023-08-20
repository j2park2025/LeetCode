#Two Sum

[Question Link](https://leetcode.com/problems/two-sum/)

In this question, you are given a set of list of numbers and a target number. You must find a pair of numbers from the list given that add up to the target number. 

First, you need to order the numbers in an increasing order. Then, letting the smallest value be Min and the largest value be Max, you will try adding the two numbers to see if they add up to the target number. If Max + Min is less than the target number, you will change the Max value to one space left. 

An example will help better explain this. 
For instance, if the given set of list of numbers is [2,7,11,15] and the target value is 9, the output will be [0,1]. The program will start by processing 2+15, which is more than the target value. Therefore, the greater number, which is in location [3], will -1 and move to [2] = 11. Then, the program will repeat its process of adding 2+11 and 2+7 until it reaches the target number of 9. 