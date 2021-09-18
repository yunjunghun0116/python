# 모든 간선을 가중치를 기준으로 정렬하고
# 비용이 가장 작은 간선부터 양 끝의 두 정점을 비교한다(모든 노드가 연결될때 까지)
# 비용할때 두 정점의 최상위 정점을 확인하고, 서로 다를 경우에 두 정점을 연결한다 -> 사이클이 생기지 않을경우에 연결한다와 같은의미
# 사이클이 생기지 않는가를 판단하는것이 요건 -> Union-Find 알고리즘이 사용된다.
# 연결된 노드들의 집합과 나머지 노드들의 집합을 이용하는데
# 만약 이번에 비교하는 간선의 두 정점이 이미 연결된 노드들의 집합에 포함된다면 이 간선은 연결하면 안된다.
# 사이클이 생성되기때문에 간선을 무시한다


# Union-Find 알고리즘 -> 노드들 중에 연결된 노드를 찾거나 노드들을 서로 연결할때 사용
# 1. 초기화 > n개의 원소가 개별 집합으로 이루어지도록 초기화
# 2. Union > 두 개별집합을 하나의 집합으로 합침 -> 두 트리를 하나의 트리로 만드는 작업
# 3. Find > 두 노드가 서로 같은 집합에 있는지 확인하는과정 -> 그룹의 루트노드를 확인

# union-by-rank 기법 : 각 트리(노드)의 높이(depth/rank)를 기억해두고
# union시 두 트리의 높이가 다르면 높이가 작은 트리를 높이가 큰 트리에 붙힌다. -> 결국 높이가 큰 트리의 루트가 결국 높이가 작은 트리의 루트와 같게된다.
# 높이가 같으면 한쪽의 트리높이를 1 증가시켜주고 다른쪽의 트리를 해당 트리에 붙힌다. -> 자식노드에 추가되는것


graph = {
    'v':['A','B','C','D','E','F','G'],
    'edge':[
        #튜플의 형태로 저장
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (9,'B','D'),
        (8,'B','C'),
        (7,'B','E'),
        (8,'C','B'),
        (5,'C','E'),
        (5,'D','A'),
        (9,'D','B'),
        (7,'D','E'),
        (6,'D','F'),
        (7,'E','B'),
        (5,'E','C'),
        (7,'E','D'),
        (8,'E','F'),
        (9,'E','G'),
        (6,'F','D'),
        (8,'F','E'),
        (11,'F','G'),
        (9,'G','E'),
        (11,'G','F'),
    ],
}
parent = {}
rank = {}

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find_parent(x):
    # parent를 찾음과 동시에 parent에 변화가 생길경우 수정을 바로 해줌
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(start,end):
    root_start = find_parent(start)
    root_end = find_parent(end)
    if rank[root_start] > rank[root_end]:
        parent[root_end] = root_start
    elif rank[root_start] == rank[root_end]:
        rank[root_start] += 1
        parent[root_end] = root_start
    else :
        parent[root_start] = root_end

def kruskal(graph):
    mst = []
    # 부분집합으로 만드는 과정
    for node in graph['v']:
        make_set(node)  
    # 우선순위대로 정렬하는 과정
    edges = graph['edge']
    edges.sort()
    # 간선 연결
    for edge in edges:
        weight,start,end = edge
        if find_parent(start) != find_parent(end):
            union(start,end)
            mst.append(edge)

    return mst

print(kruskal(graph))
print(rank)