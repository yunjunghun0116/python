import heapq
from collections import defaultdict

graph_data = [[2,'A'],[5,'B'],[3,'C']]
heapq.heapify(graph_data)
for i in range(len(graph_data)):
    print(heapq.heappop(graph_data))
print(graph_data)

# dict에 해당 key가 없어도 초기화를 시켜놓음으로써 에러를 발생하지않을수있다.
list_dict1 = defaultdict(int)
print(list_dict1['key1'])
list_dict2 = defaultdict(list)
print(list_dict2['key2'])