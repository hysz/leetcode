from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%s -> %s"%(self.val, self.next)
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # sanity check
        if not lists:
            return None

        # fetch first non-null entry
        master = None
        while not master and lists:
            master = lists.pop(0)
        
        # merge, using "merge" step from mergesort.
        for l2 in lists:
            if not l2:
                continue

            # we want to set it up such that l1.val <= l2.val for the first entry,
            # otherwise we have to think about adjusting the `master` in the merge step below.
            l1 = None
            if l2.val < master.val:
                l1 = l2
                l2 = master
                master = l1
            else:
                l1 = master
            
            # merge 'em. We set `last = None` because we know that l1.val <= l2.val on the first iteration.
            last = None
            while l1 and l2:
                #print("%d <= %d"%(l1.val, l2.val))
                if l1.val <= l2.val:
                    last = l1
                    l1 = l1.next
                else:
                    last.next = l2
                    l2 = last.next.next # same as l2.next, used for consistency w next line.
                    last.next.next = l1
                    last = last.next
            
            # cut & paste any remaining from l2
            # we've worked our way through the master lost.
            # so `last.next` will be null.
            if l2:
                last.next = l2

        return master

#print(Solution().mergeKLists([ListNode(1), ListNode(2)]))
#print(Solution().mergeKLists([ListNode(1, ListNode(3)), ListNode(2)]))
print(Solution().mergeKLists([ListNode(1, ListNode(3)), ListNode(1, ListNode(2))]))
#print(Solution().mergeKLists([]))
#print(Solution().mergeKLists([None,ListNode(1)]))
#print(Solution().mergeKLists([ListNode(1), ListNode(0)]))