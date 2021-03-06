#클래스
class Node:
    #생성자 : __init__(self) -> 생성자에서는 보통 해당 클래스가 다루는 데이터를 정의
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    #클래스 소멸시 호출되는 함수
    #이를 통해 프로그램이 다 끝나고 나면 객체를 삭제해나가면서
    #데이터 저장장소공간의 낭비를 줄일수 있다.
    def __del__(self):
        print(self.data,'Node is deleted')

#클래스
class NodeLinkedList:
    def __init__(self,data):
        self.head = Node(data)

    #마지막 노드를 찾아서 마지막노드의 next에 새로운 노드를 추가해주는 함수
    def add(self,data):
        if self.head.data == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    #원하는 인덱스를 찾아서 해당 위치에 노드를 추가하는 함수
    def insert(self,index,data):
        node = self.head
        for i in range(index-1):
            node = node.next
        temp = node.next
        node.next = Node(data)
        node = node.next
        node.next = temp


    #찾는 데이터를 삭제하는 함수
    def remove(self,data):
        #이 링크드리스트의 헤드가 존재하는지 확인
        if self.head == None:
            print('해당 값을 가진 노드가 없습니다.')
        #헤드의 데이터가 같을경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            #del 해줌으로써 저장공간의 효율성을 높일수있다
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
            print('해당 값을 가진 노드가 없습니다.')

    #원하는 data가 노드에 존재하는지 찾는 함수
    def find(self,data):
        node = self.head
        while node:
            if node.data == data :
                return True
            else:
                node = node.next
        return False

    #노드의 모든 data를 출력하는 함수
    def print_node(self):
        node = self.head
        while node:
            print(node.data)
            node=node.next

linkedList = NodeLinkedList(1)
linkedList.print_node()
for i in range(10):
    linkedList.add(i)
linkedList.print_node()
linkedList.remove(9)
linkedList.print_node()
print(linkedList.find(12345))
linkedList.insert(4,'wow')
linkedList.print_node()