class Node:
    """
    Class of tree
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_by_levels(node:Node):
    if not isinstance(node, Node):
        return []
    hight_data = {}
    def check_data_high(node: Node, hight = 0):
        if hight not in hight_data:
            hight_data[hight] = []
        hight_data[hight].append(node.value)
        if node.left is not None:
            check_data_high(node.left, hight+1)
        if node.right is not None:
            check_data_high(node.right, hight+1)
    check_data_high(node)
    return [data for value in hight_data.values() for data in value]
