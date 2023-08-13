#Two Sum

[Question Link](https://leetcode.com/problems/two-sum/)

In this question, you are given a set of list of numbers and a target number. You must find a pair of numbers from the list given that add up to the target number. 

First, you need to order the numbers in an increasing order. Then, letting the smallest value be Min and the largest value be Max, you will try adding the two numbers to see if they add up to the target number. If Max + Min is less than the target number, you will change the Max value to one space left. 

An example will help better explain this. 
For instance, 