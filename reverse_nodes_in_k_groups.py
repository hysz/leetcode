from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s -> %s"%(self.val, self.next)

class Solution:

    # swap children between parents
    def swapChildren(parent1, parent2):
        # cache children
        child1 = parent1.next
        child2 = parent2.next

        # swap parents -- important to swap parents first, o/w we'll get some recursion below.
        parent1.next = child2
        parent2.next = child1 if parent2 != child1 else parent2.next

        # swap grandchildren 
        child1_next = child1.next
        child1.next = child2.next
        child2.next = child1_next if child1_next != child2 else child1
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # base case
        if k == 1:
            return head
        
        # we need to use parent nodes to swap, so we create a fake head to avoid special-casing the head.
        fakehead = ListNode(9999999, head)

        # Run algo
        next_parent1 = fakehead
        while next_parent1 and next_parent1.next:
            parent1 = next_parent1

            # We reverse two at a time, starting at the outside and moving in.
            # For example (k=2): [1,2,3,4] -> [4,2,3,1] -> [4,3,2,1].
            # I went with this strategy bc I think it results in the least amount of swaps.
            current_k = k
            while current_k >= 2:
                parent2 = parent1
                # Find the 2nd parent whose child we'll swap with the child of `parent1`
                # (because pointers go from parent -> child, we need to find parents, not the actual that will be swapped).
                for i in range(1, current_k):
                    parent2 = parent2.next
                    if not parent2:
                        break
                    
                # Check if we don't have a full k group
                if not parent2 or not parent2.next:
                    next_parent1 = None # avoid an infinite loop
                    break
                    
                # Swap 'em children!
                Solution.swapChildren(parent1, parent2)

                # Iterate on `parent1` to swap next most inward pair.
                parent1 = parent1.next

                # Keep track of who the next parent1 will be (after the current k group)
                if current_k == k:
                    # There's a special case when k=2. Didn't dig too deep.
                    next_parent1 = parent2 if k == 2 else parent2.next
                
                # Decrement k to decrease the distance of the swap on the next iteratio (bc we're moving inward).
                current_k -= 2
            
        return fakehead.next


###print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2))
###print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 3))
###print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 4))

# Test reversing twice for one k group
###print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 4))

# Test reversing thrice for one k group
###print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 6))

# Test reversing two groups.
##print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2))

# Test reversing one group with an extra nod at the end.
##print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2))



#print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3))



print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1))

