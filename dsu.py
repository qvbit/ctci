class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]  # Each node is its own parent initially
        self.size = [1 for _ in range(size)]

    def find(self, x):
        """ Optimzied find (Path Compression) so that nodes that are encountered by find call become depth 1 from leader"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """ Optimized union (union-by-rank) so we make the smaller CC a follower of the bigger CC"""
        px, py = self.find(x), self.find(y)
        if px == py:  # Already in same connected component, nothing to do except return
            return px
        
        if self.size[px] > self.size[py]:  # Make sure y is always the biggest CC
            px, py = py, px

        self.parent[px] = py
        self.size[py] += self.size[px]
        return py
        
