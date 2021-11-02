import sys
import heapq
# 가중치가 작은것들끼리 연결

def prim(edges,n):
    queue = []
    heapq.heappush(queue,[0,0,1])

    visited = [False for _ in range(n+1)]
    result = []
    sum = 0

    while queue:
        # h[0] = cost, h[1] = current_node, h[2] = next_node
        h = heapq.heappop(queue)
        if visited[h[2]] == True:
            continue
        else:
            visited[h[2]] = True
            sum+=h[0]
            result.append((h[1],h[2],h[0]))
            
            for e in edges[h[2]]:
                #여기서 하는 일은 next_node에서 갈수있는 모든 곳을 queue에 heappush하는작업이다
                #e[0]는 다음노드,e[1]은 cost를 의미한다
                if visited[e[0]] : continue
                else:
                    heapq.heappush(queue,[e[1],h[2],e[0]])
        
    return sum,result


def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    edges = [[]for _ in range(n+1)]

    for _ in range(m):
        u,v,c = map(int,sys.stdin.readline().split())
        edges[u].append([v,c])
        edges[v].append([u,c])
    print(prim(edges,n))

    

if __name__ == '__main__':
    main()

