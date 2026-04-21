
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if not node:
                return False
            if node.key == key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Case 1: No child
                if not node.left and not node.right:
                    return None
                # Case 2: One child
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Case 3: Two children
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.key = temp.key
                node.right = _delete(node.right, temp.key)
            return node
        self.root = _delete(self.root, key)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        print("BFS:", end=" ")
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor, _ in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        print("DFS:", end=" ")

        def _dfs(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor, _ in self.graph.get(node, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        print()



class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")


if __name__ == "__main__":

    print("----- BST -----")
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums:
        bst.insert(n)

    print("Inorder:", bst.inorder())
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting 20:", bst.inorder())

    bst.insert(65)
    bst.delete(60)
    print("After deleting 60:", bst.inorder())

    bst.delete(30)
    print("After deleting 30:", bst.inorder())

    print("\n----- GRAPH -----")
    g = Graph()
    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7),
        ('B','E',3), ('C','E',1), ('D','F',5),
        ('E','D',2), ('E','F',6), ('C','F',8)
    ]
    for u,v,w in edges:
        g.add_edge(u,v,w)

    g.print_graph()
    g.bfs('A')
    g.dfs('A')

    print("\n----- HASH TABLE -----")
    ht = HashTable(5)
    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, k*10)

    ht.display()

    print("Get 10:", ht.get(10))
    print("Get 7:", ht.get(7))
    print("Get 12:", ht.get(12))

    ht.delete(15)
    print("After deleting 15:")
    ht.display()