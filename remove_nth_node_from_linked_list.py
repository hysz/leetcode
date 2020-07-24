# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s -> %s"%(self.val, self.next)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # base cases
        if not head:
            return head
        
        # We want to track the node *before* the nth last,
        # as we'll alter its `next` field to eliminate the nth.
        node_before_nth_last = head
        n += 1
        
        # Run through the list, keeping track of `node_before_nth_last`
        node = head
        while node:
            node = node.next
            if n == 0:
                node_before_nth_last = node_before_nth_last.next
            else:
                n -= 1
        
        # remove the nth last
        if n != 0:
            # remove the first element
            head = head.next
        elif node_before_nth_last.next:
            node_before_nth_last.next = node_before_nth_last.next.next
            
        return head

print(Solution().removeNthFromEnd(ListNode(1), 1))
print(Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 2))
