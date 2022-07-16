class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_sequences(root):
    if not root: return [[]]

    ret = []
    prefix = [root.val]

    left_seq = all_sequences(root.left)
    right_seq = all_sequences(root.right)

    for l in left_seq:
        for r in right_seq:
            sub_ret = []
            weave_lists(l, r, sub_ret, prefix)
            ret += sub_ret
    
    return ret

def weave_lists(first, second, sub_ret, prefix):
    if len(first) == 0 or len(second) == 0:
        sub_ret.append(prefix + first + second)
        return
    
    weave_lists(first[1:], second, sub_ret, prefix + [first[0]])
    weave_lists(first, second[1:], sub_ret, prefix + [second[0]])


def main():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(5)

    print(all_sequences(root))


if __name__ == "__main__":
    main()


