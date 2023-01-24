class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def getParents(root, valuetoSearch):
    if not root:
        return []
    if root.value == valuetoSearch:
        return [root.value]
    leftPath = getParents(root.left, valuetoSearch)
    if leftPath:
        return [root.value] + leftPath
    rightPath = getParents(root.right, valuetoSearch)
    if rightPath:
        return [root.value] + rightPath
    return []




if __name__ == '__main__':

#Create a tree

    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.right = Node(9)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)
    root.right.right.left = Node(4)

    valuetoSearch = 11
    path = getParents(root, valuetoSearch)
    print("Path: ", path)


# Output: Path:  [2, 7, 6, 11]


# Worst-case time complexity: O(n)

# Best-case time complexity: O(1) when the first node is the one we are looking for

# Average-case time complexity: O(n)

# This algorithm the worst case, best case and average case time complexities are all O(n), because the function visits each node once and performs a constant number of operations on each node. 