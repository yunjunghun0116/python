#######용어######
# Node : 트리에서 데이터를 저장하는 기본요소,데이터와 다른 연결된 노드에 대한 Branch 정보(Left/Right)
# Root Node: 트리 최상단에 위치하는 노드
# Level : 최상위노드를 level0으로 할때 하위 branch로 연결된 노드의 깊이
# Parent Node - Child Node : 상단/하단에 위치한 두 노드
# Leaf Node(Terminal Node) : Child Node가 하나도 없는 노드
# Sibling : 동일한 Parent Node를 가진 노드
# Depth : 트리의 노드가 가질수 있는 최대 Level

#트리구조 : 노드와 Branch를 이용해서 사이클을 이루지 않도록 구성한데이터구조
#이진트리형태의 구조 -> 탐색/검색 알고리즘 구현을 위해 주로 사용

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = root

    def insert(self,value):
        current_node = self.root
        while True:
            if value <= current_node.value:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break
        print(value,'삽입 완료')

    def search(self,value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                print('탐색완료')
                return
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print('탐색실패')
        return 

    def delete(self,value):
        find = False
        currentNode = self.root
        parentNode = self.root
        while currentNode:
            if currentNode.value == value:
                find = True
                break
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        if find == False:
            return
        else:
            print('Case별로 삭제')
            #LeafNode 삭제 ChildNode 1개인노드 삭제, 2개인노드삭제 총 3가지케이스 존재
            #childNode가 2개일때가 문제가 되는데
            #해결방법 1. 삭제할노드의 오른쪽자식중 가장작은값(가장 왼쪽에있는값)을 parendNode가 가리키도록하거나
            #2.왼쪽자식중 가장큰값을 가리키도록 한다.
            if currentNode.left == None and currentNode.right == None:


rootNode = Node(8)
my_tree = BinaryTree(rootNode)
for i in range(15):
    my_tree.insert(i)
my_tree.search(17)
