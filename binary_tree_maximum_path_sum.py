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

class Value:
    value = 0
    max_single_path = 0
    max_value = 0

    def __init__(self, value):
        self.value = value if value else 0

    def __repr__(self):
        return "[%s, %s, %s]"%(self.value, self.max_single_path, self.max_value)

class Solution:
    def solve(self, binary_tree):
        # a priority queue used for running dijkstras algo
        value = [Value(v) for v in binary_tree]
        dist = [[0 for j in range(0, len(binary_tree))] for i in range(0, len(binary_tree))]

        # `dist` array from binary tree
        nodes = []
        node_queue = [binary_tree[0]]
        parent_idx = 0
        i = 1
        '''
        while len(node_queue) > 0:
            parent = node_queue.pop(0)
            value[parent_idx].value = parent if parent else 0
            dist[parent_idx][parent_idx] = value[parent_idx]

            if i < len(binary_tree):
                node_queue.append(binary_tree[i])
                node_queue.append(binary_tree[i + 1])

            if not parent:
                parent_idx += 1
                continue

            if i < len(binary_tree):
                # create left child
                left_value = binary_tree[i]
                if left_value:
                    dist[parent_idx][i] = parent + left_value
                    #dist[i][parent_idx] = parent + left_value
                else:
                    left_value = 0

                # create right child
                right_value = binary_tree[i + 1]
                if right_value:
                    dist[parent_idx][i + 1] = parent + right_value
                    #dist[i + 1][parent_idx] = parent + right_value
                else:
                    right_value = 0

                dist[i][i + 1] = parent + left_value + right_value
                dist[i + 1][i] = parent + left_value + right_value

                i += 2
                parent_idx += 1
        '''
        print(dist)

        # track greatest cost while we do this
        print("********")
        print(value)
        highest_path = -2^31

        # my child = 2 * idx_in_current_row + 2^current_row_number


        print("------")

        for i in range(len(dist) - 1, -1, -1):

            if 2*i + 1 > len(dist) - 1:
                value[i].max_value = value[i].value
                value[i].max_single_path = value[i].value
                continue


            
            max_value_candidates = [value[2*i + 1].max_single_path, value[2*i + 2].max_single_path, value[i].value, value[2*i + 1].max_single_path + value[2*i + 2].max_single_path + value[i].value]
            print(max_value_candidates)
            
            max_single_path_candidates = [value[2*i + 1].max_single_path, value[2*i + 2].max_single_path, value[i].value]
            print(max_single_path_candidates)

            value[i].max_value = sorted(max_value_candidates)[-1]
            value[i].max_single_path = sorted(max_single_path_candidates)[-1]

            if value[i].max_value > highest_path:
                highest_path = value[i].max_value 


            '''
            print("%s: "%(i), neighbors)


            
            for j in neighbors:
                if j >= len(dist):
                    continue
                for k in neighbors:
                    if k >= len(dist):
                        continue
                    # check if current entry should be replaced
                    if i != j and dist[i][j] < dist[i][k] + dist[k][j] - value[k]:
                        #print("dist[%d,%d] = %d < dist[%d][%d] + dist[%d][%d] - value[%d] = %d + %d - %d = %d"%(i, j, dist[i][j], i, k, k, j, k, dist[i][k], dist[k][j], value[k], dist[i][k] + dist[k][j] - value[k]))
                        dist[i][j] = dist[i][k] + dist[k][j] - value[k]
                    if dist[i][j] > highest_path:
                        highest_path = dist[i][j]
            '''
        

        print("------")
        print(value)
        return value

        #print(dist)
        #print(highest_path)

print(Solution().solve([-10,9,20,None,None,15,7]))



        