import sys
import heapq

def dijkstra(edges,V,start,end):
    INF = float('inf')
    # 각각 V+1로 설정하는 이유는 숫자가 1부터 시작하기때문
    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    queue = []
    found = [False for _ in range(V+1)]
    # 저장값은 cost/목표노드 로 저장해야함
    heapq.heappush(queue,[0, start])

    while queue:
        pop_data = heapq.heappop(queue)
        found[pop_data[1]] = True
        for target,node_weight in edges[pop_data[1]]:    
            if found[target] : 
                continue
            else:
                # 맨처음엔 inf값으로 설정되어서 무조건 리셋해줘야함
                if distance[target] > distance[pop_data[1]]+node_weight:
                    distance[target] = distance[pop_data[1]]+node_weight
                    heapq.heappush(queue,[distance[target],target])
            
    return distance[end]
    
def main():
    # V는 노드의 수, E는 간선의 수
    V,E = map(int,sys.stdin.readline().strip().split())
    # start는 시작노드, end는 도착노드
    start,end = map(int,sys.stdin.readline().strip().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        # 출발/도착/가중치
        i,j,c = map(int,sys.stdin.readline().strip().split())
        edges[i].append([j,c])
        
    print(dijkstra(edges,V,start,end))

if __name__ == '__main__':
    main()
    
# 6 9
# 1 6
# 1 2 5
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8