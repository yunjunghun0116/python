# 최적의 해에 가까운 값을 구하기 위해 사용
# 여러 경우중 하나를 결정해야할때마다 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 최종적인 값을 구하는 방식
# 여기서 볼수있듯 단점은 항상 최적의 경우의 값을 구하는것은 아니기때문에 근사치를 구할때 많이 사용된다

# 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는문제
# 각 물건마다 가치와 무게를 갖고있다

def bag(k):
    # 무게/가치 순으로 입력받음
    data_list = [(10,10),(15,12),(20,10),(25,8),(30,5)]
    # 가치를 무게로 나눈값을 기준으로 정렬하는데 reverse = true를 줌으로써 가치가 가장 높은놈부터 정렬하는것
    data_list = sorted(data_list,key=lambda x:x[1]/x[0],reverse=True)

    max_val = 0
    can_size = k
    for data in data_list:
        while can_size>=data[0]:
            can_size -= data[0]
            max_val += data[1]
    return max_val

print(bag(85))
