import sys
import heapq
from collections import defaultdict
def prim(lines,start,costs):
    visited = [False for _ in range(len(costs))]
    sum = costs[start]
    queue = []
    heapq.heappush(queue,[0,0,start]) # cost 출발지점 도착지점을 기준으로 삼는데
    # python특성상 튜플의 첫번째인덱스의 값을 기준으로 heap적용을 하기때문에
    # 건설비용 출발지점 도착지점을 순서로 가져오게 한다
    while queue:
        pop_data = heapq.heappop(queue)
        cost,s,e = pop_data
        if visited[e]:
            continue
        else:
            visited[e] = True
            sum += cost
            # lines는 결국 딕셔너리형태이기때문에 현재 while문에서 
            # pop한 객체의 도착지점이 다음 queue에 heappush할땐 출발지점이 될 수있고
            # 그때 도착지점은 lines[도착지점]에 속한 배열원소 각각이 된다
            for ed in lines[e]:
                e_end,e_cost = ed
                if visited[e_end]:
                    continue
                else:
                    if e_cost < costs[e_end]: #통신망을 그대로세우는것보다 값이 쌀때만 queue에 넣어주는방식
                        heapq.heappush(queue,[e_cost,e,e_end])
    for i in range(len(costs)):
        if visited[i]:
            continue
        else:
            sum+=costs[i]
    return sum
    
def main():
    town_cnt,line_cnt = map(int,sys.stdin.readline().strip().split())
    costs = [0]
    # 입출력을 보면 0번인덱스가 1번마을 ,1번인덱스는 2번마을을 가리키기때문에
    # 1번인덱스가 1번마을,2번인덱스가 2번마을을 가리킬수있도록 설정
    costs.extend(list(map(int,sys.stdin.readline().strip().split()))) #index에 바로 접근할수있도록
    # cost의 index : 해당번째수 비용
    lines = defaultdict(list)
    for _ in range(line_cnt):
        start,end,cost = map(int,sys.stdin.readline().strip().split())
        lines[start].append([end,cost])
        lines[end].append([start,cost])
        
    min_val = sum(costs) #최소한 모든곳에서 직접 통신망구축하는곳보단 작야할것이기때문에 모든곳에 직접 구축하는곳의 cost 합
    for i in range(1,town_cnt+1):
        min_val = min(min_val,prim(lines,i,costs))
    print(min_val)
if __name__ == '__main__':
    main()