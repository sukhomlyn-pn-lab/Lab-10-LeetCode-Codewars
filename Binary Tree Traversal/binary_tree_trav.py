class Node:
    """
    Class of tree
    """
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right




# Pre-order traversal
def pre_order(node:Node):
    if not isinstance(node, Node):
        return []
    data_list = []
    data_list.append(node.data)
    if node.left is None and node.right is None:
        return data_list
    data_list.extend(pre_order(node.left))
    data_list.extend(pre_order(node.right))
    return data_list


# In-order traversal
def in_order(node:Node):
    if not isinstance(node, Node):
        return []
    data_list = []
    if node.left is None and node.right is None:
        data_list.append(node.data)
        return data_list
    data_list.extend(in_order(node.left))
    data_list.append(node.data)
    data_list.extend(in_order(node.right))
    return data_list

# Post-order traversal
def post_order(node:Node):
    if not isinstance(node, Node):
        return []
    data_list = []
    if node.left is None and node.right is None:
        data_list.append(node.data)
        return data_list
    if node.left is not None:
        data_list.extend(post_order(node.left))
    if node.right is not None:
        data_list.extend(post_order(node.right))
    data_list.append(node.data)
    return data_list
