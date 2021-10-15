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
                heapq.heappush(supply_heap,-supplies[i])
                index = i+1
            else:
                break
        print(index,cnt,stock) 
        # 만약 for문을 돌지 않더라도 이미 쌓인 heap에서
        # stock >= k를 완료하지 못했기때문에 최댓값을 한번더 추출한 후에 더해준다
        max_val = -heapq.heappop(supply_heap)
        stock += max_val
        cnt += 1
    return cnt
    

def main():
    input_list = list(map(int,sys.stdin.readline().strip().split()))
    dates = list(map(int,sys.stdin.readline().strip().split()))
    supplies = list(map(int,sys.stdin.readline().strip().split()))
    stock,k = input_list[0],input_list[1]
    print(solve(stock,k,dates,supplies))

if __name__ == '__main__':
    main()
