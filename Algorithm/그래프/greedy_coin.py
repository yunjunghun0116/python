# 최적의 해에 가까운 값을 구하기 위해 사용
# 여러 경우중 하나를 결정해야할때마다 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 최종적인 값을 구하는 방식
def coin(m):
    cnt = 0
    money = m
    coin_list = [1,50,100,500]
    coin_list.sort(reverse=True)
    for i in range(len(coin_list)):
        cnt += money//coin_list[i]
        money = money % coin_list[i]
    return cnt

print(coin(4720)) # 9 + 2 + 20

         