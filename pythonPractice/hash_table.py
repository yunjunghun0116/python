class data:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class hash_table:
    def __init__(self):
        self.table = [0 for i in range(10)]
    
    def make_hash(self,data):
        return data%10

    def save_data(self,key,value):
        # ord Func - key의 맨 첫글자의 ASCII코드를 반환해준다
        # 해싱충돌을 linkedList로 구현해서 처리해주었다.
        hash_key = self.make_hash(key)
        if self.table[hash_key]!=0:
            temp = self.table[hash_key]
            while temp.next:
                temp = temp.next
            temp.next = data(key,value)
        else:
            self.table[hash_key] = data(key,value)

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
    myTable.save_data(i,i)
myTable.print_table()
