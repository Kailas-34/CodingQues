# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        res = output
        carry = 0
        while l1 or l2 or carry:
            temp = carry
            
            if l1:
                temp = l1.val+temp
                l1 = l1.next
            if l2:
                temp = l2.val+temp 
                l2 = l2.next
            
            carry = temp//10
            num = temp % 10

            print(num)
            output.next = ListNode(num)
            output = output.next
        
        return res.next






        
