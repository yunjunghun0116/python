class Node:
    def __init__(self,data,prev = None,next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleLinkedList:
    def __init__(self,data=None):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            #새로운 노드를 만들어 마지막노드의 next에 넣어주고
            #prev가 있기때문에 새로만든 노드의 prev에 마지막노드를 넣어준다
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def insert_before(self,data,before_data):
        if self.head == None:
            self.insert(data)
        if self.head.data == before_data:
            node = self.head
            new = Node(data)
            new.next = node
            node.prev = new
            self.head = new
        else:
            node =self.head
            while node:
                if node.next:
                    if node.next.data == before_data:
                        temp = node.next
                        new = Node(data)
                        node.next = new
                        new.prev = node
                        new.next = temp
                        temp.prev = new
                        print('삽입완료.')
                        return
                node = node.next
            print('before_data가 존재하지않습니다.')

                    
                    

    def delete(self,data):
        if self.head == None:
            print('해당 데이터가 없습니다.')
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
        else:
            node = self.head
            while node:
                if node.data == data:
                    if node.next:
                        temp = node
                        prev_node = node.prev
                        next_node = node.next
                        prev_node.next = next_node
                        next_node.prev = prev_node
                        del temp
                        return
                    #선택한 노드가 맨 마지막 노드일 경우
                    #tail에서 변화가 발생하기때문에 tail노드를 바꿔주어야한다.
                    else:
                        temp = node
                        prev_node = node.prev
                        prev_node.next = None
                        self.tail = prev_node
                        del temp
                        return
                else:
                    node = node.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def print_list_reverse(self):
        node = self.tail
        while node:
            print(node.data)
            node = node.prev

double_linked_list = DoubleLinkedList(3)
for i in range(15):
    double_linked_list.insert(i)
double_linked_list.delete(11)
double_linked_list.delete(14)
double_linked_list.print_list()
double_linked_list.insert_before(152,0)
double_linked_list.print_list()
double_linked_list.print_list_reverse()

