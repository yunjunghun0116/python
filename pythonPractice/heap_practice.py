#### 힙 구조 ####
# 일반적으로 구현할때는 배열을 활용한다
# 배열은 인덱스 0번부터 시작하지만, 힙구현의 편의를 위해 root노드의 인덱스를 1로 지정하면 구현이 좀더 수월하다.
## 데이터에서 최댓값/최솟값을 빠르게 찾기 위해 고안된 완전 이진 트리
# 완전이진트리 : 노드삽입시 최하단 왼쪽노드부터 차례대로 삽입 -> 꽉찬 트리
## 힙 사용하는 이유
# 배열에 데이터를 넣고 최대/최솟값 찾을때 O(n)이 걸리지만
# 힙구조를 사용할경우 O(logn)이 걸린다
# 우선순위큐 처럼 최대/최소를 빠르게 찾아야하는 자료구조/알고리즘 구현에 활용된다
## 조건
# 1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다(작거나 같다) -> 최대힙(최소힙)
# 2. 완전 이진 트리 형태를 갖는다

import random

# push/pop 기능을 구현할때는 결국
# move_up/move_down을 통해 내려가거나 올라가야할(swap을 진행해줘야할곳)을 찾아야하기때문에
# 결국 move_up/down 함수구현이 가장 중요하다

class Heap:
    def __init__(self):
        # 구현의 편의를 위해 None의 값을 한번 추가해줌으로써 인덱스1부터 시작할수있도록 한다.
        self.heap_array = list()
        self.heap_array.append(None)

    # 최대힙의 경우 부모노드가 자식노드보다 커야하지만 무작정 append했을경우 작을수도있기때문에
    # 자식노드의 값이 부모노드의 값보다 클때 두 노드를 서로 스왑해줘야하기때문에
    # 이를 판단하기위한 작업 -> 스왑해줘야하는경우 true리턴 
    def move_up(self,index):
        #위로 올려줄 공간이 없을때
        if index <= 1:
            return False
        # 위로 올리기 위해선 부모노드의 값을 알아봐야하고,완전이진트리의 형태에서는
        # 부모 노드 인덱스 = 자식 노드 인덱스  // 2
        # 왼쪽 자식 노드 인덱스  = 부모 노드 인덱스 * 2
        # 오른쪽 자식 노드 인덱스  = 부모 노드 인덱스 * 2 + 1
        parent_index = index // 2
        if self.heap_array[index] > self.heap_array[parent_index]:
            # 올려줘야할때만 true를 리턴
            return True
        return False

    # push의 기능은 완전이진트리에서는 맨 밑에서부터 올라가는 구조를 거친다
    def push(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            print(data,'삽입완료')
            return
        self.heap_array.append(data)
        # 맨처음 None을 집어넣어주었기때문에 -1을 해준다.
        check_index = len(self.heap_array)-1
        while self.move_up(check_index):
            check_parent_index = check_index//2
            self.heap_array[check_index],self.heap_array[check_parent_index] = self.heap_array[check_parent_index],self.heap_array[check_index]
            check_index = check_parent_index
        print(data,'삽입완료')

    def move_down(self,index):
        left_index = index * 2
        right_index = index * 2 + 1
        heap_len = len(self.heap_array)
        # leftNode가 없을때
        # 이론적으로는 >= 가 아니라 > 이지만 구현을 위해 0번인덱스에 None을 넣어주었기때문에
        # len을 하면 None까지 포함한 전체 길이를 반환해주기때문에 ==일 경우에는 딱 그 위치에
        # data가 존재한다는 말이기때문에 존재하지않기위해서는 >=을 해주어야한다.
        if left_index >= heap_len :
            return False
        # rightNode가 없을때 -> leftNode는 존재한다는 말
        elif right_index >= heap_len :
            if self.heap_array[left_index] > self.heap_array[index]:
                return True
            else:
                return False
        # left/right 둘다있을때
        else:
            # left > right 일때
            if self.heap_array[left_index] > self.heap_array[right_index]:
                if self.heap_array[left_index] > self.heap_array[index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_index] > self.heap_array[index]:
                    return True
                else:
                    return False
        
    # pop의 기능은 가장 마지막에 추가된 원소를 root의 위치로 올린후에
    # child Node중 가장 큰 값과 바꿔준다 -> 위에서부터 천천히 내려가며 제자리 찾아가는 기능
    # push는 밑에서부터, pop은 위에서부터
    def pop(self):
        if len(self.heap_array) <= 1:
            print('데이터가 없습니다.')
            return
        #최댓값을 뽑아주고 -> return할때 사용
        pop_data = self.heap_array[1]
        #가장 마지막에 넣어준 data를 가져온다
        self.heap_array[1] = self.heap_array[-1]
        #마지막 인덱스에 해당하는 값을 지워준 후에
        del self.heap_array[-1]
        #맨위에서부터 차근차근 실행해나간다.
        index = 1
        print('pop실행')
        while self.move_down(index):
            left_index = index * 2
            right_index = index * 2 + 1
            #왼쪽과 바꿀것인지, 오른쪽과 바꿀것인지를 찾는과정
            swap_index = index
            #오른쪽이 존재하는지 확인 -> if의 조건은 오른쪽이 없으면 무조건 left와 바꾸기때문에 실행해준것
            if right_index >= len(self.heap_array):
                swap_index = left_index
            else:
                if self.heap_array[left_index]>self.heap_array[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index
            self.heap_array[index],self.heap_array[swap_index] = self.heap_array[swap_index],self.heap_array[index]
            index = swap_index
        print(pop_data,'최댓값 추출 완료')


        

my_heap = Heap()

for i in range(10):
    my_heap.push(random.randint(0,99))

print(my_heap.heap_array)
my_heap.pop()
print(my_heap.heap_array)

    