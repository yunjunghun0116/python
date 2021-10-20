import sys
from collections import defaultdict

def firstCnt(graph):
    # 맨 처음의 그룹의 개수를 구하는 과정으로서
    # graph의 모든 key값을 진행해줌
    cnt = 0
    keys = []
    keys.extend(graph.keys())
    visited = []
    stack = []
    def dfs(i):
        start = keys[i]
        visited.append(start)
        stack.extend(graph[start])
        while stack:
            val = stack.pop()
            if val not in visited:
                visited.append(val)
                stack.extend(graph[val])
    for i in range(len(keys)):
        if keys[i] not in visited:
            dfs(i)
            cnt+=1

    return cnt

def check(graph_cnt,temp_graph):
    # 위의 firstCnt함수와 동일한 로직이지만
    # 이게 독점무역로인지 아닌지를 판단하기위한 기준값 -> 비교하는 기준은 그 무역로가 사라졌을때 그룹의 개수가 분명 1개이상 늘어나기때문
    # graph_cnt를 인자로 받아준 후 비교한다.
    cnt = 0
    keys = []
    keys.extend(temp_graph.keys())
    visited = []
    stack = []
    def dfs(i):
        start = keys[i]
        visited.append(start)
        stack.extend(temp_graph[start])
        while stack:
            val = stack.pop()
            if val not in visited:
                visited.append(val)
                stack.extend(temp_graph[val])
    for i in range(len(keys)):
        if keys[i] not in visited:
            dfs(i)
            cnt+=1

    if graph_cnt == cnt:
        return False
    else: 
        return True

def find(graph):
    firstCount = firstCnt(graph) #맨 처음의 그룹의 개수를 알아야 독점무역로인지 알 수 있기때문에 맨처음의 그룹의개수를 구하는함수
    result = []
    temp_graph = graph.copy() #그래프를 카피한다음
    # 무역로를 하나씩 지워가며 독점무역로인지 판단하기위한 과정이기때문에
    # 하나하나 지우는데 graph[key] = val일 경우 graph[key]와 graph[val]을 둘다 지워줘야
    # 제대로된 지우는 과정이 진행되기때문에
    for key in graph:
        length = len(graph[key])
        for i in range(length):
            # i는 graph[key]의 index이지만
            # graph[val]의 [key]값이 갖는 index를 알아야 지운후 재삽입이 가능하기때문에 index()로 찾는다.
            val = temp_graph[key][i] 
            temp_index = temp_graph[val].index(key) 
            temp_graph[key].pop(i)
            temp_graph[val].pop(temp_index)
            if check(firstCount,temp_graph): #여기서 true가 나올경우 그 무역로는 독점무역로라는 뜻
                result.append((key,val))
            temp_graph[key].insert(i,val)
            temp_graph[val].insert(temp_index,key)

    return result
def main():
    cities,cnt = map(int,sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(cnt):
        start,end = map(int,sys.stdin.readline().strip().split())
        # 문제 마지막조건을 보면 3 5, 5 3을 같은 무역로로 본다고한 조건때문에
        # 아래처럼 graph[3] = [5],graph[5] = [3] 의 과정처럼 진행
        graph[start].append(end)
        graph[end].append(start)

    results = defaultdict(list)
    result = find(graph) # 여기에는 독점무역로가 담겨있다.
    for i in range(len(result)):
        # 아래과정은 5 3, 6 4 와 같은값들을 모두 3 5, 4 6 처럼 바꿔주는것이고
        # 중복된값은 들어갈필요 없기때문에 체크후 결과 result에 넣어준다.
        start,end = result[i]
        if start > end:
            if start not in results[end]:
                results[end].append(start)
        else:
            if end not in results[start]:
                results[start].append(end)
    # defaultdict에 있는 값을 하나하나 끄집어내서 output_result에 넣어주기위한 과정
    output_result = []
    for key in results:
        for i in range(len(results[key])):
            # 안의 원소 하나하나 튜플형식으로 집어넣어준다.
            output_result.append((key,results[key][i]))
    # 오름차순정렬후 출력이 조건이기때문에 정렬후 출력
    output_result.sort()
    for i in range(len(output_result)):
        start,end = output_result[i]
        print(start,end)



if __name__ == '__main__':
    main()