class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Traverse down a binary tree, sum up all the nodes 
# in each branch, and display it in an array ordering 
# left to right that reflects the branch order
        
def branchSums(root):
    sums = []
    traverseTree(root, 0, sums)
    return sums
    
def traverseTree(node, total, sums):
    if node is None:
        return
    
    newTotal = total + node.value
    if node.left is None and node.right is None:
        sums.append(newTotal)
        return sums
    
    traverseTree(node.left, newTotal, sums)
    traverseTree(node.right, newTotal, sums)

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Depth-first search (DFS) is an algorithm for 
    # traversing or searching tree or graph data structures. 
    # The algorithm starts at the root node 
    # (selecting some arbitrary node as the root node in the case of a graph) 
    # and explores as far as possible along each branch before backtracking.

    def depthFirstSearch(self, array):
        array.append(self.name)
		
        for child in self.children:
            child.depthFirstSearch(array)
		
        return array