from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s -> %s"%(self.val, self.next)

class Solution:

    # swap chilren between parents
    def swapNodes(parent1, parent2):
        print("parent 1 - ", parent1)
        print("parent 2 - ", parent2)

        # swapping nodes is messy ... There are four cases.
        # 1. Swapping adjacent nodes.
        # 2. Swapping non-adjacent nodes.
        # 3. Swapping nodes where the 2nd node is the end of the list.

        child1 = parent1.next
        child2 = parent2.next

        print("c1: ", child1)
        print("c2: ", child2)

        # swap parents -- important to swap parents first!
        parent1.next = child2
        parent2.next = child1 if parent2 != child1 else parent2.next

        # swap grandchildren 
        child1_next = child1.next
        child1.next = child2.next
        child2.next = child1_next if child1_next != child2 else child1
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        # seems kinda like 
        curk = k
 
        

        fakehead = top = ListNode(9999999, head)
        for i in range(k, 0, -2):
            print(i)
            # iterate to the (n-1)th node. We'll alter its `next`
            
            node = top
            while node and i > 1:
                node = node.next
                i -= 1
                
            # couldn't countdown k
            if i > 1:
                break
                
            print("stop at %s"%(node))

            Solution.swapNodes(top, node)

            # iterate top
            top = top.next if top else head.next
            
        return fakehead.next


#print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2))
print(Solution().reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 3))