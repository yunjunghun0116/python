import sys
# 1 2 5
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8
# 트리와 연결되는것들중 가장 가중치가 작은것을 선택

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
def kruskal(vertex_list,edge_list):

    for u in vertex_list:
        make_set(u)

    edges = edge_list
    edges.sort()
    mst = [] #최소신장트리
    sum = 0

    for e in edges:
        cost,u,v = e
        if find(u) != find(v):
            union(u,v)
            mst.append(e)
            sum += cost

    return sum,mst

def main():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    vertices = []
    edges = []

    for i in range(1,n+1):
        vertices.append(str(i))
    for _ in range(m):
        u,v,c = map(int,sys.stdin.readline().split())
        edges.append((c,str(u),str(v)))
    
    print(kruskal(vertices,edges))
    

if __name__ == '__main__':
    main()

