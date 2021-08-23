#HashTable -> 공간과 탐색 시간을 맞바꾸는 방법
#해쉬테이블의 공간을 늘리면 늘릴수록 충돌할 확률자체가 낮아지기때문에
#충돌시간이 줄어들어서 결국 탐색시간이 줄어든다

#list를 만드는 새로운 방법
hash_table = list([0 for i in range(10)])

def make_hash(key):
    return key%10

#ord : ASCII코드 반환
def storage_data(data,value):
    key = ord(data[0])
    hash_address = make_hash(key)
    hash_table[hash_address] = value
def get_data(data):
    key = ord(data[0])
    hash_address = make_hash(key)
    return hash_table[hash_address]
    
storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

print(get_data('Dave'))

#해쉬충돌해결알고리즘 - 해싱한 결과가 같은경우가 존재할수있고,
#그경우 충돌이 발생할수있기에 해쉬테이블을 이용할때에는
#충돌해결알고리즘또한 고안해야한다.

#1.개방해싱 - 충돌시 링크드리스트를 통해 추가로 뒤에 연결시키기
def get_key(data):
    return hash(data)

#실제로는 돌아가지않으나 Node처럼 next의 형태를 구현하기만 하면 될듯
def save_data(data,value):
    index_key = get_key(data)
    hash_address = make_hash(index_key)
    if(hash_table[hash_address] != 0):
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0] == index_key:
                hash_table[hash_address][i][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = make_hash(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


save_data('Junghun','01012341234')
save_data('Dd', '1201023010')
save_data('Data', '3301023010')
read_data('Junghun')




