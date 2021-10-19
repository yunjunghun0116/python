import sys
import heapq #default : 최소힙이기때문

def solve(stock,k,dates,supplies):
    length = len(dates)
    supply_heap = []
    cnt = 0
    index = 0
    while stock < k:
        for i in range(index,length):
            if dates[i] <= stock:
                # -를 붙혀서 가장 큰값이 최솟값으로 저장되고,
                # 가장작은 값이 최댓값으로 저장되게 heappush를 진행
                heapq.heappush(supply_heap,-supplies[i])
                index = i+1
            else:
                break
        # 만약 for문을 돌지 않더라도 이미 쌓인 heap에서
        # stock >= k를 완료하지 못했기때문에 최댓값을 한번더 추출한 후에 더해준다
        # 즉 stock >= k가 되기전까진 heap에서 계속 꺼내는 과정을 진행한다.
        max_val = -heapq.heappop(supply_heap)
        # 꺼낸후 -를 붙혀서 더해줘야 양수의 최댓값이 저장된다.
        stock += max_val 
        cnt += 1 #횟수+1
    return cnt
    

def main():
    input_list = list(map(int,sys.stdin.readline().strip().split()))
    dates = list(map(int,sys.stdin.readline().strip().split()))
    supplies = list(map(int,sys.stdin.readline().strip().split()))
    stock,k = input_list[0],input_list[1]
    print(solve(stock,k,dates,supplies))

if __name__ == '__main__':
    main()
