# Definition for singly-linked list.
class ListNode:
    val = 0
    next = None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%d -> "%(self.val) + str(self.next)

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        start = None
        prev = None
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            remainder = sum % 10
            carry = int(sum / 10)
            node = ListNode(remainder, None)

            # Set prev.next/start to this node, if necessary.
            if prev:
                prev.next = node
            else:
                start = node

            # Update `prev` to be this node
            prev = node

            # Iterate on l1/l2
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            
        # Handle carry over at end
        if carry:
            # If carry isset then start/prev isset.
            prev.next = ListNode(carry, None)
                
        return start



'''
a = ListNode(2, ListNode(4, ListNode(3, None)))
b = ListNode(5, ListNode(6, ListNode(4, None)))
print(Solution().addTwoNumbers(a, b))
'''     

'''
a = ListNode(9, None)
b = ListNode(5, ListNode(6, ListNode(4, None)))
print(Solution().addTwoNumbers(a, b))
'''

'''
a = ListNode(5, ListNode(6, ListNode(4, None)))
b = ListNode(9, None)
print(Solution().addTwoNumbers(a, b))
'''

'''
a = ListNode(9, ListNode(9, ListNode(9, None)))
b = ListNode(9, None)
print(Solution().addTwoNumbers(a, b))
'''

'''
print(Solution().addTwoNumbers(ListNode(1, None), None))
print(Solution().addTwoNumbers(None, ListNode(1, None)))
'''

        
        
        