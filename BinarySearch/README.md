# Leet Code 

[Question Link](https://leetcode.com/problems/binary-search/)

![Binary Search Diagram Simple Explanation](./BinarySearchIMG.png "Binary Search Diagram")

Binary search can work when there is a list of numbers in an increasing order. With a minimum and a maximum values of the list, the number in the middle (not the arithmetic mean but the mean of the number of terms) will be compared with the number that we are trying to find. 

Let:
- M = the middle term
- T = the number that we are tying to find
- Min = Minimum value
- Max = Maximum value

If M is smaller than T, then the Min value will be set to the previous M value (Max will stay the same).
If opposite (M is greater than T), then the Max value will be set to the previous M value (Min will stay the same). 

For example, if the list of numbers = [1, 4, 5, 9, 13, 19, 28, 37, 41] and the Target (T) value is 5, the starting M value will be 9. Min value is 1, and Max value is 41.
Since T is smaller than M (5<13), the new Max will be 13. The Min value will still be 1. 
With that information, we have a new M value. M=5. We found the target value. 

