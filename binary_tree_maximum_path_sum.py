import heapq
import sys

class Node:
    value: None
    edges: None
    rank: 0

    def __init__(self, value, edges = []):
        self.value = value if value else 0
        self.edges = edges
        self.rank = -2^31
    
    def __lt__(self, other):
        return self.rank < other.rank

    def __repr__(self):
        return "%s"%(self.value)#: %s"%(self.value, self.edges)

class Solution:
    def solve(self, binary_tree):
        '''
        # a priority queue used for running dijkstras algo
        priority_queue = []

        # construct queue from binary tree
        nodes = []
        node_queue = [Node(binary_tree[0])]
        i = 1
        while len(node_queue) > 0:
            parent = node_queue.pop(0)
            if not parent:
                continue

            if i < len(binary_tree):
                # create left child
                left_value = binary_tree[i]
                if left_value:
                    left = Node(left_value, [parent])
                    parent.edges.append(left)
                    node_queue.append(left)
                else:
                    node_queue.append(None)

                # create right child
                right_value = binary_tree[i + 1]
                if right_value:
                    right = Node(right_value, [parent])
                    parent.edges.append(right)
                    node_queue.append(right)
                else:
                    node_queue.append(None)

                i += 2
            
            # add parent to priority queue for processing
            priority_queue.append(parent)
        
        
        print(priority_queue)

        heapq.heapify(priority_queue)
        while priority_queue:
            node = heapq.heappop(priority_queue)
        '''

        # We'll solve using floyd-warshall
        

        #whi
        
        #print(priority_queue)

print(Solution().solve([-10,9,20,None,None,15,7]))



        