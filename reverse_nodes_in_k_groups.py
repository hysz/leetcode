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
        ##print("parent 1 - ", parent1)
        ##print("parent 2 - ", parent2)

        child1 = parent1.next
        child2 = parent2.next

        ##print("c1: ", child1)
        ##print("c2: ", child2)

        # swap parents -- important to swap parents first!
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
        
        # seems kinda like 
        curk = k
 
        fakehead = ListNode(9999999, head)

        next_top = fakehead
        while next_top and next_top.next:
            top = next_top
            #print("Starting NYA")
            #print("-----------")
            current_k = k
            while current_k >= 2:
                #print("TOP: ", top)
                #print("Current K: ", current_k)
                # iterate to the (n-1)th node. We'll alter its `next`
                
                node = top
                # find parent of who we'll swap with
                for i in range(1, current_k):
                    node = node.next
                    if not node:
                        break
                    
                # couldn't countdown k
                #print("node ", node)
                if not node or not node.next:
                    #print("hmm be we eatin")
                    next_top = None
                    break
                    
                ##print("stop at %s"%(node))

                Solution.swapNodes(top, node)

                # iterate top
                top = top.next

                if current_k == k:
                    #print("WANT HERE: ", node)
                    next_top = node if k == 2 else node.next
                
                current_k -= 2
                
                #print(fakehead.next)
                #print("---- end k group -----")
                
            
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

