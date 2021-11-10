import sys
import heapq

def kruskal(nodes,edges):
    parent = {}
    rank = {}
    def make_set(v): #parent가 맨처음에 자기자신을 가리킬수있도록
        parent[v] = v
        rank[v] = 0
    def find(v):
        if parent[v] == v: #만약 parent가 자기자신을 가리킬경우 그대로 리턴
            return v
        else:
            parent[v] = find(parent[v]) #아닐경우 parent를 가지고 다시 find실행
            return parent[v]
    def union(u,v): # 두개의 노드를 합치는 과정
        root1 = find(u)
        root2 = find(v)
        if root1 != root2: # parent가 서로 다를경우 사이클이 발생하지않는다는의미
            # 아래는 rank에따라서 parent를 수정(rank가 낮은것이 높은것에 붙을수있도록)
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
    sum = kruskal(nodes,edges)
    print(sum)
    
    
    
if __name__ == '__main__':
    main()