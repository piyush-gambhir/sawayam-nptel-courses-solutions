class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def construct_tree(values, children):
    nodes = [TreeNode(val) for val in values]
    for idx, (left, right) in enumerate(children):
        if left != -1:
            nodes[idx].left = nodes[left]
        if right != -1:
            nodes[idx].right = nodes[right]
    return nodes[0]  # Return root of the tree


def sum_paths(node, curr_num=0):
    if not node:
        return 0

    # Update the current number
    curr_num = curr_num * 10 + node.value

    # If the current node is a leaf
    if not node.left and not node.right:
        return curr_num

    # Recursively get the sum for left and right subtrees
    left_sum = sum_paths(node.left, curr_num)
    right_sum = sum_paths(node.right, curr_num)

    return left_sum + right_sum


def root_to_leaf_sum(n, values, children):
    root = construct_tree(values, children)
    return sum_paths(root)


def main():
    n = int(input())  # number of nodes
    values = list(map(int, input().split()))  # node values
    children = [tuple(map(int, input().split()))
                for _ in range(n)]  # child indices

    print(root_to_leaf_sum(n, values, children), end='')


main()
