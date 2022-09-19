""" Node class that keeps track of rank information as well """
class RankNode:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None
        self.left_size = 0

    def insert(self, d):
        if d <= self.data:  # Insert to the left and incremement left_size. Note also how we insert equality to the left so that duplicates will increment left_size too
            if self.left:  # Recursively call on the left subtree
                self.left.insert(d)
            else:
                self.left = RankNode(d)
            self.left_size += 1
        else:  # Insert to the right, don't touch left_size
            if self.right:  # Recursively call on the right subtree
                self.right.insert(d)
            else:
                self.right = RankNode(d)
    
    def get_rank(self, d):
        if d == self.data:
            return self.left_size
        elif d < self.data:  # Go left
            if not self.left: return -1  # This d does not exist
            return self.left.get_rank(d)  # Note how we are discarding the right subtree and root in our rank computation
        else:  # Go right
            right_rank = -1 if not self.right else self.right.get_rank(d)
            if right_rank == -1: return -1  # Note how right rank could be -1 from either this tree having its right subtree empty or the recursion on the right subtree not being able to find d
            return self.left_size + 1 + right_rank  # Count the left subtree size + 1 for the root + the result of recursing on the right subtree


class NumberStream:
    def __init__(self):
        self.root = None
    
    def track(self, num):
        if not self.root:
            self.root = RankNode(num)
        else:
            self.root.insert(num)
    
    def get_rank_of_number(self, num):
        return self.root.get_rank(num)


if __name__ == "__main__":
    ns = NumberStream()
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    for num in stream:
        ns.track(num)
    
    print(ns.get_rank_of_number(1))
    print(ns.get_rank_of_number(3))
    print(ns.get_rank_of_number(4))











