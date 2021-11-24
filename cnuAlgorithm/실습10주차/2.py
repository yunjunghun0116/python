import sys
from collections import defaultdict

def bellman_ford(edges,start,end,nodes):
    distance = defaultdict(int)
    for node in nodes:
        distance[node] = float('inf')
    distance[start] = 0
    result = []
    # start -> end를 도달하기위해 거칠수있는 모든 경우를 result에 담아 반환
    for i in range(len(nodes)-1):
        for node in nodes:
            for target,value in edges[node]:
                if distance[target] > distance[node] + value:
                    distance[target] = distance[node] + value
                    result.append([node,target])
    # 음수의 사이클이 발생할경우 해당 사이클의 무한루프가 돌아갈수있기때문에 이경우 Negative를 위한 False반환
    for node in nodes:
        for target,value in edges[node]:
            if distance[target] > distance[node]+value:
                return False
    return [distance,result]
def main():
    node_cnt,edge_cnt = map(int,sys.stdin.readline().strip().split())
    start,end = map(str,sys.stdin.readline().strip().split())
    nodes = list(map(str,sys.stdin.readline().strip().split()))
    edges = defaultdict(list)
    
    for _ in range(edge_cnt):
        s,e,c = map(str,sys.stdin.readline().strip().split())
        cost = int(c)
        edges[s].append([e,cost])
        
    result = bellman_ford(edges,start,end,nodes)
    
    if result != False:
        # 결과가 존재할경우(음수의 무한루프가 발생하지않을경우)
        distance = result[0]
        route = result[1]
        routes = defaultdict(list)
        results = []
        # routes에는 routes[출발] = [[도착점,비용]의 배열]
        # 이 기록되었고 비용을 출력하기위해 생성
        for s,e in route:
            check = False
            for target,value in edges[s]:
                if target == e and not check:
                    cost = value
            routes[s].append([e,cost])
        
        queue = [[[None,start],0]]
        while queue:
            current_route,cost = queue.pop(0)
            target = current_route[-1]
            for dest,c in routes[target]:
                if dest == end :
                    results.append([current_route+[dest],cost+c])
                else:
                    queue.append([current_route+[dest],cost+c])
        # start -> end까지 경로가 여러개나올경우 최단거리인 경로 하나만 택해야하기때문에
        # 최단경로를 final_result에 저장
        final_result = results[0]
        for r in results:
            if r[1] < final_result[1]:
                final_result = r
        
        for i in range(1,len(final_result[0])-1):
            check = False
            s,e = final_result[0][i],final_result[0][i+1]
            for t,c in routes[s]:
                if t == e and not check:
                    print(s,e,c)
                    break
    else:
        print('Negative')
    
   
if __name__ == '__main__':
    main()