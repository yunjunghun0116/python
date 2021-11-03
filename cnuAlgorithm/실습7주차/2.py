import sys

def solve(base,stations):
    result = 0
    # 모든 기지에서부터 각 기지와 전력소간 최단거리를 구한후
    for b in base:
        distance_min = float('inf')
        for s in stations:
            distance_min = min(distance_min,abs(b-s))
        # 여기서 distance_min이 최단거리이기때문에
        # 그 최단거리들사이 최댓값을 출력해주면 그 값이 결국 모든 기지가
        # 전력공급망에 포함하는 최소한의 추가전력생산량이다.
        result = max(result,distance_min)
    return result
    
def main():
   base = list(map(int,sys.stdin.readline().strip().split()))
   stations = list(map(int,sys.stdin.readline().strip().split()))
   print(solve(base,stations))

if __name__ == '__main__':
    main()
