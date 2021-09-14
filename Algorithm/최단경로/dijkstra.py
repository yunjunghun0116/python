from queue import PriorityQueue
# import heapq 한 후에 queue = [] 선언하고
# heapq.push(queue,1)
# heapq.pop(queue) 처럼 진행해도 heapq 자체가 minheap의 구조를 따라 push/pop을 진행하기때문에 
# 제대로 동작한다.

# queue = PriorityQueue() 
# queue의 구조를 확인하고싶을땐 print(queue.queue) 를 하면 나온다
# queue.put()/get()을 통해 push/pop을 할 수 있다

# 갈수있는노드 : 가중치 를 갖고있는 형태로 그래프구현
graph = {
    'A' : {'B':8,'C':1,'D':2},
    'B' : {},
    'C' : {'B':5,'D':2},
    'D' : {'E':3,'F':5},
    'E' : {'F':1},
    'F' : {}
}



def dijkstra(graph,start):
    # 1. 각각의 요소가 inf(무한대값) 을 가리키고있는 형태로 초기화한다.
    # 2. start포인트의 거리를 0으로 초기화한다.
    distances = {data:float('inf') for data in graph}
    distances[start] = 0
    queue = PriorityQueue() 
    # 거리와 data(ex 'A','B')를 [key,value] 의 형식처럼 집어넣어준다.
    queue.put([distances[start],start])

    while queue.qsize() != 0:
        # 내가 작성한 코드
        pop_data = queue.get()
        # pop_data 는 [8,'B'] 와 같은식으로 되어있고,
        # 'B'의 현재 최단거리는 8임을 나타내는 데이터형식이다.
        if pop_data[0]>distances[pop_data[1]]:
            # 그런데 내가 뽑은 이 데이터의 최단거리가
            # 내가 distance에 저장한 최단거리보다 클경우에는 밑의 과정을 굳이 거칠필요가 없기때문에
            # continue를 통해 그만해준다.
            print(pop_data[1],"에서 이 과정을 거치지 않음")
            continue

        for data in graph[pop_data[1]]: 
        # 우선순위 큐 에서 뽑은 데이터(최단거리) -> 갈수있는 모든 곳에 대해서 거리를 현재까지의 최단거리와 합친후
        # distances의 현재 저장된 거리보다 작을경우 
        # 예를 들면 1 -> 3 까지 바로가는데 5만큼 가중치가있지만
        # 1 -> 2 -> 3 거쳐가는데 가중치가 3이라고 하면
        # 처음과정에서는 distances에 5만 저장되지만 한번 더진행해보니 최단거리가 5가아닌 3이었고 이를 바꿔주는
        # 이러한 과정을 거칠경우 바꿔주는(최단거리로 업데이트해주는) 연산을 진행한다
            temp_num = pop_data[0] + graph[pop_data[1]][data] 
            if temp_num < distances[data]:
                distances[data] = temp_num
                queue.put([temp_num,data])

        
        # # 강의 코드
        # pop_distance,pop_name = queue.get()
        # for name,distance in graph[pop_name].items():
        #     new_distance = pop_distance + distance
        #     if new_distance< distances[name]:
        #         distances[name] = new_distance
        #         queue.put([new_distance,name])
    
    # 각 항목(ex 'A','B',...)등에 대한 최단거리가 저장된 dictionary형태를 리턴해준다
    return distances

print(dijkstra(graph,'C'))
