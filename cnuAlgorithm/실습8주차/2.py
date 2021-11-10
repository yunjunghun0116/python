import sys
import heapq

def kruskal(nodes,edges):
    parent = {}
    rank = {}
    def make_set(v):
        parent[v] = v
        rank[v] = 0
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v] = find(parent[v])
            return parent[v]
    def union(u,v):
        root1 = find(u)
        root2 = find(v)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2 
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    for node in nodes:
        make_set(node)
    sum = 0
    for i in range(len(edges)):
        pop_data = heapq.heappop(edges)
        cost,u,v = pop_data
        if find(u) != find(v):
            union(u,v)
            sum += cost
    return sum

def main():
    edges = []
    node_cnt,edge_cnt = map(int,sys.stdin.readline().split())
    nodes = list(map(str,sys.stdin.readline().strip().split()))
    for i in range(edge_cnt):
        s,e,c = list(map(str,sys.stdin.readline().strip().split()))
        cost = int(c)
        heapq.heappush(edges,[cost,s,e])
    temp_edges = edges[:] #edges를 복사한후에
    result = float('inf')
    check = kruskal(nodes,edges)
    results = []
    for i in range(len(temp_edges)):
        sub_temp_edges = temp_edges[:] #edge를 하나씩 빼가며 구분해보기 위한 복사
        sub_temp_edges.pop(i) #edge를 하나씩 빼보며 확인해보지만
        sum = kruskal(nodes,sub_temp_edges)
        if sum > check: #최단거리보단 커야하기때문에 check(최단거리)보다 클경우만 추가를 해준다.
            results.append(sum)
        
    print(min(results)) #이곳에는 결국 모든 최단거리보다 큰 연결값이 들어있기에 최솟값을출력하면
    # 그 값이 두번째로 작은 최단거리신장트리이다.
    
    
    
if __name__ == '__main__':
    main()