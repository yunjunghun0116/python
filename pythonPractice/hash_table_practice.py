# 해싱충돌시 연결리스트로 구현하기위해서는 저장시 데이터의 next가 있어야하고
# 그래서 next를 갖고있는 데이터객체를 클래스로 만들어주었다.
class data:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

#해쉬테이블은 배열에 비해서 데이터를 읽는 속도가 빠르다
#또한 중복확인이 쉽다는 장점이 있지만,
#일반적으로 배열보다 저장공간이 더 많이 필요하다(해쉬충돌때문)
#따라서 검색이 많이필요하거나, 저장/삭제/읽기가 빈번할경우
#또한 캐쉬를 구현할때 많이 사용된다.
class hash_table:
    def __init__(self):
        self.table = [0 for i in range(10)]
    
    def make_hash(self,data):
        return data%10

    def save_data(self,key,value):
        # ord Func - key의 맨 첫글자의 ASCII코드를 반환해준다/단 문자의경우에만 가능하고
        # 그로인해서 key가 숫자의 형태일경우 쓸수없다.
        # 해싱충돌을 linkedList로 구현해서 처리해주었다.
        hash_key = self.make_hash(key)
        if self.table[hash_key]!=0:
            temp = self.table[hash_key]
            while temp.next:
                temp = temp.next
            temp.next = data(key,value)
        else:
            self.table[hash_key] = data(key,value)
    
    def delete_data(self,key,value):
        hash_key = self.make_hash(key)
        if self.table[hash_key] != 0:
            temp = self.table[hash_key]
            while temp:
                if temp.value == value:
                    self.table[hash_key] = temp.next
                    del temp
                    print('삭제완료')
                    return
                if temp.next and temp.next.value == value:
                    if temp.next.next:
                        temp.next = temp.next.next
                    else:
                        temp.next = None;
                    print('삭제완료')
                    return
                temp = temp.next
        print('삭제할 데이터가 존재하지 않습니다.')

    def print_table(self):
        for i in range(len(self.table)):
            print(i,'번째')
            temp = self.table[i]
            if temp != 0:
                while temp:
                    print(temp.value)
                    temp = temp.next
        
myTable = hash_table()
for i in range(15):
    myTable.save_data(i,i*i)
myTable.print_table()
myTable.delete_data(1,1)
myTable.print_table()
