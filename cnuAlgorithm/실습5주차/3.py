import sys
import heapq

def solve(weights):
    weights_heap = []
    for i in weights:
        heapq.heappush(weights_heap,(-i))
    while len(weights_heap) > 1:
        a = heapq.heappop(weights_heap)
        b = heapq.heappop(weights_heap)
        result = abs(a-b)
        if result == 0:
            continue
        else:
            heapq.heappush(weights_heap,(-result))
    
    if len(weights_heap) == 1:
        return -weights_heap[0]
    else:
        return 0


def main():
    weights = list(map(int,sys.stdin.readline().strip().split()))
    print(solve(weights))

if __name__ == '__main__':
    main()
