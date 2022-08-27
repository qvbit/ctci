import collections
import matplotlib.pyplot as plt
import seaborn as sns


import random

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.size = 1
        self.left = None
        self.right = None

    def get_random_node(self):
        left_size = self.left.size if self.left else 0
        index = random.randint(0, self.size-1)
        
        # Go left if index is 0...left_size-1
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:  # In this case we select the root
            return self
        else:  # In this case we go to the right
            return self.right.get_random_node()
    
    def insert(self, d):
        """ Note that this construct a BST """
        if d <= self.val:  # Insert to the left
            if not self.left:
                self.left = TreeNode(d)
            else:
                self.left.insert(d)
        else: # d > self.val, insert to the right
            if not self.right:
                self.right = TreeNode(d)
            else:
                self.right.insert(d)
        self.size += 1
    
    def find(self, d):
        if d == self.val:
            return self
        elif d <= self.val:
            return self.find(self.left) if self.left else None
        else: # d > self.val
            return self.find(self.right) if self.right else None

    
    def __repr__(self):
        return f"### Data: {self.val}, Left: {self.left}, Right: {self.right} ###"


if __name__ == "__main__":
    node_vals = [20, 10, 30, 5, 15, 35, 3, 17]
    root = TreeNode(node_vals[0])

    for d in node_vals[1:]:
        root.insert(d)

    # Simulate 1000 runs of the function
    count = collections.Counter()
    for _ in range(100000):
        count[str(root.get_random_node().val)] += 1
    
    plt.bar(list(count.keys()), count.values())
    plt.show()

    

            




