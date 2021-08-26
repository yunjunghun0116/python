#HashTable -> 공간과 탐색 시간을 맞바꾸는 방법
#해쉬테이블의 공간을 늘리면 늘릴수록 충돌할 확률자체가 낮아지기때문에
#충돌시간이 줄어들어서 결국 탐색시간이 줄어든다

#list를 만드는 새로운 방법
hash_table = list([0 for i in range(10)])

def make_hash(key):
    return key%10

#단순 해쉬테이블
#ord : ASCII코드 반환
def storage_data(data,value):
    #입력받은 데이터(string 여기서는 이름에 해당)의 첫글자의 ASCII코드를 이용해
    #해쉬화를 진행한 후, 해쉬테이블에 저장해준다.
    key = ord(data[0])
    hash_address = make_hash(key)
    hash_table[hash_address] = value
def get_data(data):
    key = ord(data[0])
    hash_address = make_hash(key)
    return hash_table[hash_address]

####SHA-1/256 ######
#import hashlib -> hashlib라는 라이브러리에서 가져오고
#data = 'input'.encode() -> byte형태로 변환시켜준후에
#hash_object = hashlib.sha1() -> sha1/sha256 을 이용하면된다.
#hash_object.update(data) 또한 data가 아닌 b'input'으로 하면 input이라는 string의 byte형태가 입력되게된다.
#print(hash_object.hexdigest()) -> 문자열의 형태로 해쉬화된 결과값이나오게된다
#만약 문자열이 16진수로 나타나게하고싶을때는
#int(hash_object.hexdigest(),16)을 이용해서 문자->상수 로 형변환이가능하다.

#해쉬충돌해결알고리즘 - 해싱한 결과가 같은경우가 존재할수있고,
#그경우 충돌이 발생할수있기에 해쉬테이블을 이용할때에는
#충돌해결알고리즘또한 고안해야한다.

def get_key(data):
    hash_key = hash(data)
    if hash_key < 0:
        return -hash_key
    return hash_key

def save_data(data,value):
    index_key = get_key(data)
    hash_address = make_hash(index_key)
    if hash_table[hash_address] != 0:
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0] == data:
                hash_table[hash_address][i][1] = value
                return
        hash_table[hash_address].append([data, value])
    else:
        hash_table[hash_address] = [[data,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = make_hash(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == data:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


save_data('Junghun','01012341234')
save_data('Dd', '1201023010')
save_data('Dh', '1201024243010')
save_data('Dc', '12010242430910')
save_data('Data', '3301023010')
print(hash_table)
print(read_data('Dd'))




