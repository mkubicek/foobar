#
# Optimized solution for Ion Flux Relabelings
# Time O(logn)
# Space O(1)
#

def findParent(h, node):
    """ Find the postorder parent index of a given node in a perfect binary tree. """
    min_node_index = 1
    root = 2**h - 1
    if(node < min_node_index or node >= root):
        return -1
    # right child is always parent - 1
    right = root - 1
    # left child is always right child - (2^(h -1) - 1)
    left = right - ((2 ** (h - 1)) - 1)
    while(h > 1):
        h = h - 1
        if (right == node or left == node):
            return right + 1
        # left subtree contains only lower values than parent
        # right subtree contains only higher values than parent
        if (left > node):
            # descent left subtree
            right = left - 1
        else: # descent right subtree
            right = right - 1
        left = right - (2 ** (h - 1) - 1)
    return -1

def solution(h, q):
    return [findParent(h, node) for node in q]

if __name__ == '__main__':
    assert (solution(3, [7, 3, 5, 1])) == [-1,7,6,3]
    assert (solution(5, [19, 14, 28])) == [21,15,29]