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

def labelTreePostOrder(root):
    global i
    if root:
        labelTreePostOrder(root.left)
        labelTreePostOrder(root.right)
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
    labelTreePostOrder(root)
    buildChildParentDict(root)
    result = []
    for index in q:
        if index in childParentDict:
            result.append(childParentDict[index])
        else:
            result.append(-1)
    return result
    
if __name__ == '__main__':
    assert solution(3, [7, 3, 5, 1]) == [-1,7,6,3]
    assert solution(5, [19, 14, 28]) == [21,15,29]