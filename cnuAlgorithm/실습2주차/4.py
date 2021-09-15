import sys

# 5,5 -> 16

def stair(n,m):
    # n : 계단수, m : 최대 계산 수
    cnt = [0 for i in range(n+1)]
    # 시작지점에서 한번에 갈 수 있는 모든 단계에 1을 추가해준다
    for i in range(1,m+1):
        cnt[i] = 1
    # 모든단계가 가질 수 있는 모든 값을 저장해주는데
    for i in range(1,n+1):
        # 현재 위치까지 한번에 올 수 있는 위치의 모든 값들을 더해준다
        for j in range(1,m+1):
            if i-j <= 0:
                continue
            else:
                cnt[i] += cnt[i-j]

    
    # 배열의 마지막 원소가 결국엔 구하고자 하는 답
    return cnt[-1]
        
    
def main():
    n,m = map(int,sys.stdin.readline().split())
    print(stair(n,m))
    
if __name__ == '__main__':
    main()
