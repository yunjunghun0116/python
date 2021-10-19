import sys
import heapq

def solve(weights):
    weights_heap = []
    for i in weights:
        # 실제 최댓값이 weights_heap에는 최솟값으로 저장되게한다.
        # 이유는 heapq의 default가 minHeap이기때문
        heapq.heappush(weights_heap,(-i))

    while len(weights_heap) > 1:
        # 최댓값 두개를 꺼낸후에
        a = heapq.heappop(weights_heap)
        b = heapq.heappop(weights_heap)
        result = abs(a-b) #두 값의 차를 저장후
        # 만약 0일경우 두 소행성이 사라진것이기때문에 다음으로 넘어가고
        if result == 0:
            continue
        else:
            # 충돌하고 남았을경우 남은 값을 새로 넣어준다.
            heapq.heappush(weights_heap,(-result))
    
    if len(weights_heap) == 1:
        # 원소가 존재하면 -를 붙혀서 실제 남은값을 출력
        return -weights_heap[0]
    else:
        # 원소가 없다는것은 결국 모든 소행성이 사라진것이기때문에
        # 0을 리턴하면된다.
        return 0


def main():
    weights = list(map(int,sys.stdin.readline().strip().split()))
    print(solve(weights))

if __name__ == '__main__':
    main()
