import sys
import heapq
from collections import defaultdict

def dijkstra(edges,start,end,nodes):
    route = defaultdict(list)
    distance = defaultdict(int)
    found = defaultdict(bool)
    for node in nodes:
        distance[node] = float('inf')
        found[node] = False
    distance[start] = 0
    queue = []

    # cost와 동선 순서로 큐에 집어넣는다
    heapq.heappush(queue,[0, [start]])
    while queue:
        pop_data = heapq.heappop(queue)
        # 동선의 마지막(pop된 위치) 를 True로 변환
        found[pop_data[1][-1]] = True
        for target,node_weight in edges[pop_data[1][-1]]:  
            # 이미 확인한곳이면 넘어간다.  
            if found[target] : 
                continue
            else:
                # 기록된 start -> target 의 거리가 start -> 동선 -> target 보다 cost가 클경우
                # 새로 업데이트해준다.
                if distance[target] > distance[pop_data[1][-1]]+node_weight:
                    distance[target] = distance[pop_data[1][-1]]+node_weight
                    route[target] = pop_data[1]+[target]
                    heapq.heappush(queue,[distance[target],route[target]])
            
    return route[end],distance[end]
    
    
def main():
    node_cnt,edge_cnt = map(int,sys.stdin.readline().strip().split())
    start,end = map(str,sys.stdin.readline().strip().split())
    nodes = list(map(str,sys.stdin.readline().strip().split()))
    edges = defaultdict(list)
    
    for _ in range(edge_cnt):
        s,e,c = map(str,sys.stdin.readline().strip().split())
        cost = int(c)
        edges[s].append([e,cost])
        edges[e].append([s,cost])
        
    route,distance = dijkstra(edges,start,end,nodes)
    print(''.join(route))
    print(distance)
        
    
        
    
    
    
   
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