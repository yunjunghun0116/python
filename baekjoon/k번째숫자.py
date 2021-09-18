# 이분탐색 : left,right,mid 를 통해 탐색할 범위를 줄여나가며 탐색하는방법
# 시작자리와 끝자리를 각각 left,right로 한 후에 조건에 맞춰 mid를 기준으로 왼쪽을 탐색할것인지
# 오른쪽을 탐색할것인지를 판단해야하고, 그 과정은 문제마다 다르고
# 이번 문제에서는 find를 통해 내가 찾으려고 하는 값보다 작은 값들의 개수를 찾는데
# mid//i 가 생각보다 중요하다
# 3,7 을 입력받았을경우 각 행마다 작은 값의 개수는 아무리 많아봐야 3개이다.
# 따라서 find += 할때 만약 작은게 2개면 그대로 넣되 4/1 처럼 3보다 큰수가 나올경우에
# 3으로 초기화해주기위해 min 함수를 사용했다
# 일단 mid는 시작과 끝을 설정해서 중간값을 임의로 예측한것이다.
# 이 값은 배열에 있을수도있고 없을수도있지만 작은값의 개수를 통해 범위가 왼쪽인지 오른쪽인지는 판단할수있다


def main():
    # 입력받는과정
    n = int(input())
    k = int(input())
    left = 1
    right = k
    while left < right:
        find = 0
        mid = (left+right)//2

        for i in range(1,n+1):
            find += min(mid//i,n)
        if find < k :
            left = mid + 1
        else :
            right = mid 
    result = (left+right)//2
    print(result)



if __name__ == '__main__':
    main()

