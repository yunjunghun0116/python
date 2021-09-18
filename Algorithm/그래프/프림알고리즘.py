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
# set을 통해 이미 연결된 노드인가를 판단함 -> set 자료구조 이용
# vs.kruskal 
# kruskal algorithm : union-find 기법을 통해
# 부모노드를 찾아본 후에 같은경우에 이미 연결되었구나를 판단
# rank에 따라 연결해줌
# 반면에 prim알고리즘은 set() 을 통해서 연결된노드인가를 판단하고,
# 그다음 연결 안되어있으면 PriorityQueue 자료구조를 이용해서
# 최소가중치를 가진 간선을 연결해준다.
def prim(start_node,edges):
    #연결된 간선 저장소
    mst = []
    #간선들을 저장해주는것 (1,a,b) -> a->b,b->a 둘다 1로 저장해주는 과정을 거치는것
    #출발과 끝이 정해지지 않은 무방향그래프이기때문
    #즉 모든 간선을 저장해놓는 저장소이다
    adjacent_edges = defaultdict(list)
    #제대로된 edges -> 모든 경로를 저장해주는 과정
    for weight,node_1,node_2 in edges:
        adjacent_edges[node_1].append((weight,node_1,node_2))
        adjacent_edges[node_2].append((weight,node_2,node_1))

    #연결된 노드들을 저장해주기 위한 저장소
    connected_nodes = set(start_node)

    #가중치가 가장 낮은 간선이 추출하기 위한 list
    candidate_edge_list = adjacent_edges[start_node]
    print('CandidateEdgeList',candidate_edge_list)
    heapify(candidate_edge_list)

    while candidate_edge_list:
        # candidate_edge_list중 가장 간선의 길이가 짧은것을 뽑은 후에
        weight,n1,n2 = heappop(candidate_edge_list)
        print(n1,n2,weight,'데이터 pop')
        # 사이클을 형성하지않을경우에
        if n2 not in connected_nodes:
            #연결해주는 과정진행
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))
            
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    print(edge[1],edge[2],edge[0],'데이터 push')
                    heappush(candidate_edge_list,edge)
    return mst



print(prim('F',edges))