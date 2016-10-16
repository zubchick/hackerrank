""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    def rec(node, range_):
        if node is None:
            return True

        left, right = range_

        if not (left < node.data < right):
            return False

        return (rec(node.left, (left, node.data)) and
                rec(node.right, (node.data, right)))

    return rec(root, float('-inf'), float('+inf'))
