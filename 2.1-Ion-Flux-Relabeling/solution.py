#
# Brute force solution for Ion Flux Relabeling
# Time O(n)
# Space O(n)
#
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        
i = 1
childParentDict = {}
    
def buildTree(h, root):
    if h > 1:
        root.right = buildTree(h - 1, Node())
        root.left = buildTree(h - 1, Node())
    return root

def traverseAndNumberTreePostOrder(root):
    global i
    if root:
        traverseAndNumberTreePostOrder(root.left)
        traverseAndNumberTreePostOrder(root.right)
        root.value = i
        i = i + 1

def buildChildParentDict(root):
    if root.left and root.right:
        childParentDict[root.left.value] = root.value
        childParentDict[root.right.value] = root.value
        buildChildParentDict(root.left)
        buildChildParentDict(root.right)

def solution(h, q):
    global i
    i = 1
    root = buildTree(h, Node())
    traverseAndNumberTreePostOrder(root)
    buildChildParentDict(root)
    result = []
    for index in q:
        if index in childParentDict:
            result.append(childParentDict[index])
        else:
            result.append(-1)
    print(result)
    
if __name__ == '__main__':
    solution(3, [7, 3, 5, 1])
    solution(5, [19, 14, 28])