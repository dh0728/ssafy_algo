import sys
sys.stdin=open('5176_re_input.txt')

# def insert_left_tree(n,index):
#     if bin_tree[index]==None:
#         bin_tree[index]=n
#     else:
#         if bin_tree[index] < n:
#             last_n=bin_tree[index]
#             bin_tree[index]=n
#             insert_left_tree(last_n,index*2)
#         else:
#             insert_left_tree(n,index*2)
#
#
#
# # 주어진 배열이 오름차순일때만 가능할 듯
# def insert_node(n,index):
#     if bin_tree[index]==None: #루프노드에 값 없으면 값 넣기
#         bin_tree[index]=n
#     elif bin_tree[tree_l]==None:
#         insert_left_tree(n,index)
#     else:
#         if n < bin_tree[index]: #값이 루프노드보다 작다면
#             if index*2 < tree_l: # 왼쪽 자식노드가 있으면
#                 insert_node(n,index*2)
#         else: # 값이 루프노드보다 크다면 오른쪽으로
#             if index*2 < tree_l:
#                 insert_node(n, index*2+1)

class Node:
    def __init__(self, key):
        self.key = key
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root =None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
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
            if node.key >=10:
                print(node.key%10, end=' ')
            else:
                print(node.key, end=' ')
            self._inorder_traversal(node.right)


T=int(input())
for tc in range(1,T+1):
    code=input()
    N=int(code[0]) # self 계산용 숫자
    dec_list=[]

    # 암호문 2자리씩 10진수로 변환
    for i in range(1,len(code),2):
        dec_list.append(int(code[i:i+2],16))
    # print(dec_list)

    # 암호문 위치에 따라 빼기
    for i in range(len(dec_list)):
        dec_list[i]-=(i+1)*N
    # print(dec_list)

    tree_l=len(dec_list)
    bin_tree=[None]*(len(dec_list)+1)

    bst=BinarySearchTree()

    for num in dec_list:
        bst.insert(num)
    print(f'#{tc}',end=' ')
    bst.inorder_traversal()
    print()




