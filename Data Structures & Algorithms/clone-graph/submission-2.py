"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if not node:
                return None
            #if we already created the node
            if node in old_to_new:
                return old_to_new[node]
            
            # create new and add in hashmap
            clone = Node(node.val)
            old_to_new[node] = clone

            #recurcively create and attach neighbors 
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone
        
        return dfs(node)
