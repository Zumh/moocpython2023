# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

# def sum_of_nodes(root: Node):
#     node_sum = root.value 

#     # go to the left branch
#     if root.left_child is not None:
#         node_sum += sum_of_nodes(root.left_child)

#     # go to the right branch
#     if root.right_child is not None:
#         node_sum += sum_of_nodes(root.right_child)
    
#     return node_sum

def greatest_node(root: Node):
    node_max = root.value 

    # traverse all the left branch and compare every number like linear search for the left branch
    # just to find greatest value from the left branch
    if root.left_child is not None:
        next_value = greatest_node(root.left_child)
        if node_max < next_value:
            node_max = next_value

    # we carry on the greatest value from the left with node_max
    # we then find greatest value from the right branch
    # we compare against to current max value from the left
    # once we done searching from the right we updae the current max value
    # if we have a max value from the right branch
    if root.right_child is not None: 
        next_value = greatest_node(root.right_child)
        if node_max < next_value:
            node_max = next_value
    return node_max

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.left_child.left_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))


