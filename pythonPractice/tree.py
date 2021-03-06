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

import queue
import random

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
                print(value,'탐색완료')
                return
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print('탐색실패')
        return 

    #LeafNode 삭제 ChildNode 1개인노드 삭제, 2개인노드삭제 총 3가지케이스 존재
    #childNode가 2개일때가 문제가 되는데
    #해결방법 1. 삭제할노드의 오른쪽자식중 가장작은값(가장 왼쪽에있는값)을 parendNode가 가리키도록하거나
    #2.왼쪽자식중 가장큰값을 가리키도록 한다.
    #둘다 방식은 똑같기때문에 오른쪽 자식중 가장 작은값을 가리키도록 할경우
    # 1.가장 작은값을 위로 올려줘야하기때문에 삭제할 노드의 parent노드가 가리킬수있도록 함
    # 2.해당 노드의 left는 삭제할노드의 left를 가리키도록함
    # 3.해당 노드의 right또한 삭제할노드의 right를 가리키도록함
    # 4.올려준 노드가 만약 right를 갖고있었으면 올려주기 이전의 parent노드가 올려준노드의 right를 가리키도록 하고
    # 5.만약 올려준노드의 child가 하나도없으면 올려주기 이전의 parent노드의 left = None으로 해주면 된다.
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
            print(value,'가 존재하지않습니다')
            return
        else:
            #LeafNode의 경우
            if currentNode.left == None and currentNode.right == None:
                #currentNode가 parenNode의 왼쪽인지 오른쪽인지를 알기위해
                if value == self.root.value:
                    self.root = None
                if currentNode.value < parentNode.value:
                    parentNode.left = None
                else:
                    parentNode.right = None
            #ChildNode를 한개 갖고있는경우
            #ChildNode를 왼쪽에 갖고있는지 or 오른쪽에 갖고있는지
            elif currentNode.left != None and currentNode.right == None:
                if value == self.root.value:
                    self.root = currentNode.left
                if currentNode.value < parentNode.value:
                    parentNode.left = currentNode.left
                else:
                    parentNode.right = currentNode.left
            elif currentNode.left == None and currentNode.right != None:
                if value == self.root.value:
                    self.root = currentNode.right
                if currentNode.value < parentNode.value:
                    parentNode.left = currentNode.right
                else:
                    parentNode.right = currentNode.right
            #ChildNode를 두개 갖고있는경우
            else:
                #temp는 삭제할 노드를 삭제했을때 빈자리를 채워줄
                #삭제할노드중 큰값중 가장 작은값을 나타내는 노드
                
                #temp : 삭제할 노드의 right 노드중 가장 작은값을 지닌 노드
                #밑의 코드는 삭제할 노드를 삭제한 후에 삭제한 위치에 temp를 갖다 놓는과정
                temp = currentNode.right
                temp_parent = currentNode.right
                while temp.left:
                    temp_parent = temp
                    temp = temp.left
                if temp.right != None:
                    temp_parent.left = temp.right
                else:
                    temp_parent.left = None
                temp.left = currentNode.left
                temp.right = currentNode.right

                #삭제할 노드가 root노드일경우
                if value == self.root.value:
                    self.root = temp
                elif currentNode.value < parentNode.value:
                    parentNode.left = temp
                else:
                    parentNode.right = temp
            print(value,'삭제 완료')
            del currentNode

    #dfs를 이용한 노드출력방식
    #왼쪽부터 체크하고, 가장 끝노드부터 체크,
    #왼쪽 맨아래부터 차근차근 체크해가며 검사하는방식
    data_list = []
    def print_node(self,node):
        if node.left:
            self.print_node(node.left)
        if node.right:
            self.print_node(node.right)
        self.data_list.append(node.value)

    #bfs를 이용한 노드출력방식
    #최상단노드부터 하나하나 내려가면서 체크하는방식
    def print_node_queue(self):
        node_queue = queue.Queue()
        node_queue.put(self.root)
        while node_queue.qsize() != 0:
            temp_node = node_queue.get()
            self.data_list.append(temp_node.value)
            if temp_node.left:
                node_queue.put(temp_node.left)
            if temp_node.right:
                node_queue.put(temp_node.right)


rootNode = Node(50)
my_tree = BinaryTree(rootNode)



#Random한 값을 많이 집어넣음으로써 모든 기능이 제대로 진행되는지 테스트하는과정
insert_nums = set()
search_nums = set()
delete_nums = set()
#0~99중 15개의 랜덤숫자 선택해서 집어넣기
while len(insert_nums) != 15:
    insert_nums.add(random.randint(0,99))
#고른 랜덤숫자15개를 이진트리에 삽입해주기
for num in insert_nums:
    my_tree.insert(num)

while len(search_nums) != 15:
    search_nums.add(random.randint(0,99))
for num in search_nums:
    my_tree.search(num)

#set의 형태를 list형태로 변환하는방법
# nums = list(nums)처럼 list(set타입의 자료) -> list타입으로 변환시켜준다.

while len(delete_nums) != 15:
    delete_nums.add(random.randint(0,99))
for delete_num in delete_nums:
    my_tree.delete(delete_num)

my_tree.print_node_queue()
print(my_tree.data_list)
# my_tree.print_node(my_tree.root)
# print(my_tree.data_list)
