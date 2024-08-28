'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    # 관리할 데이터는 최상위 root
    def __init__(self):
        self.root = None

    def insert(self, key):
        # root 가 없다면 삽입
        if self.root is None:
            self.root = Node(key)
        else:
            # 있다면 자리를 찾아서 삽입
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key: # 찾고자 하는게 더작으면 왼쪽을 고려
            if node.left is None:   # 왼쪽에 삽입 가능하면
                node.left = Node(key)   # 그냥 삽입
            else:   # 왼쪽에 데이터가 있다면
                self._insert(node.left, key)    # 재귀로 한번 더 내려감
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key: # 찾는 노드가 없거나 찾으면 노드 반환
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
