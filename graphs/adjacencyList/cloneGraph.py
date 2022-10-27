"""
Problem Statement:
    - Given a reference of a node in a connected undirected graph.
    - Return a deep copy of the graph
    - Each node contains val and a list of Node neighbors

    Example:
        adjList = [[2,4],[1,3],[2,4],[1,3]]

        1 -> 2
        1 -> 4

        2 -> 1
        2 -> 3

        3 -> 2
        3 -> 4

        4 -> 1
        4 -> 3
"""
class Node:
    def __init__(self, val=0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class CloneGraph:
    def __init__(self, originalGraph):
        self.original = originalGraph

    def cloneGraph(self, node):
        clone = {}

        def dfs(curr):
            # if current node exists in clone, return the copy
            if curr in clone:
                return clone[curr]

            # create deep copy of the current node
            clone[curr] = Node(curr.val)

            # iterate through the neighbors of the current node
            for nei in curr.neighbors:
                # do a recursive dfs on neighbors
                clone[curr].neighbors.append(dfs(nei))

            # return the clone of the curr node
            return clone[curr]
        return dfs(node)

node = Node(1)
nodeTwo = Node(2)
nodeThree = Node(3)
nodeFour = Node(4)

# 1 <-> 2
node.neighbors.append(nodeTwo)
nodeTwo.neighbors.append(node)

# 2 <-> 3
nodeTwo.neighbors.append(nodeThree)
nodeThree.neighbors.append(nodeTwo)

# 3 <-> 4
nodeThree.neighbors.append(nodeFour)
nodeFour.neighbors.append(nodeThree)

# 1 <-> 4
node.neighbors.append(nodeFour)
nodeFour.neighbors.append(node)

graph = CloneGraph(node)
print(graph.cloneGraph(node).neighbors[0].val)

# Time: O(N) where n is the size of the graph
# Space: O(N)