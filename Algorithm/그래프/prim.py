# 해당 정점을 기준으로 가장 가중치가 작은 간선을 선택해나가는 방식
# 노드와 연결된 모든 간선들중 가중치가 가장 작은 간선을 계속 연결해나가는방식
from collections import defaultdict
from heapq import *

edges = [
    (7,'A','B'),(5,'A','D'),
    (8,'B','C'),(9,'B','D'),(7,'B','E'),
    (5,'C','E'),
    (7,'D','E'),(6,'D','F'),
    (8,'E','F'),(9,'E','G'),
    (11,'F','G')
]

def prim(start_node,edges):
    #연결된 간선 저장소
    mst = []
    # 이미 연결된 노드들을 저장해주는 리스트
    adjacent_edges = defaultdict(list)
    for weight,node_1,node_2 in edges:
        adjacent_edges[node_1].append((weight,node_1,node_2))
        adjacent_edges[node_2].append((weight,node_2,node_1))
    #연결된 노드들
    connected_nodes = set(start_node)
    #가중치가 가장 낮은 간선이 추출하기 위한 list
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight,n1,n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))
            
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list,edge)
    return mst



print(prim('A',edges))