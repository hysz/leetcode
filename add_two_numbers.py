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
        l1_idx = 0
        l2_idx = 0
        carry = 0
        first = None
        prev = None
        while l1 and l2:
            sum = l1.val + l2.val + carry
            remainder = sum % 10
            carry = int(sum / 10)
            node = ListNode(remainder, None)
            if prev:
                prev.next = node
            else:
                first = node
            prev = node
            l1 = l1.next
            l2 = l2.next
            
        # Handle case where l1 has more digits than l2
        while l1:
            sum = l1.val + carry
            remainder = sum % 10
            carry = int(sum / 10)
            node = ListNode(remainder, None)
            if prev:
                prev.next = node
            prev = node
            l1 = l1.next

        # Handle case where l2 has more digits than l1
        while l2:
            sum = l2.val + carry
            remainder = sum % 10
            carry = int(sum / 10)
            node = ListNode(remainder, None)
            if prev:
                prev.next = node
            prev = node
            l2 = l2.next
            
        # Handle carry over at end
        if carry:
            # can skip some checks; if carry is set then we've already set `prev` and `first`
            prev.next = ListNode(carry, None)
                
        return first
        print(first)



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
        
        
        