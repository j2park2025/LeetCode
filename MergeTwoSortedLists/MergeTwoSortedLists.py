# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        node2 = ListNode(2)
        node1 = ListNode(1, node2)
        
        currentNode = node1 
        while currentNode.val != 1:
            currentNode = currentNode.next
        """
        resultnode = ListNode()
        curresult = resultnode 
        cur1 = list1 
        cur2 = list2 
        while ((cur1 != None) and (cur2 != None)):
            if ((cur1.val) >= (cur2.val)): # if 1 is greater than 1 :: cur1(1, 2, 4) cur 2(1, 3, 4) curresult(mt)
                curresult.next = cur2 # curresult's next value 에다가 current 2 를 put :: cur1(1, 2, 4) cur2(1, 3, 4) curresult(0, cur2)
                cur2 = cur2.next
            elif (cur1.val < cur2.val):
                curresult.next = cur1
                cur1 = cur1.next
            curresult = curresult.next
            # elif (cur1.val == cur2.val): #first, cur1(1->2) cur 2(1->3) curresult(0, 1, 1)
            #     curresult.next = cur1
            #     cur1 = cur1.next
            #     curresult = curresult.next
            #     curresult.next = cur2
            #     curresult = curresult.next
            #     cur2 = cur2.next
                
        
        if (cur1 == None):
            curresult.next = cur2
        elif (cur2 == None):
            curresult.next = cur1

        return resultnode.next
        
        

    