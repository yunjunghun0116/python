import sys
from collections import defaultdict
def solve(trains,train_line):
    visited = []
    stack = []
    visited.append(trains[0])
    stack.extend(train_line[trains[0]])
    # trains[0]에서부터 갈수있는 모든곳을 연결해본후 만약 모든 곳을
    # 방문한다면 visited의 원소 개수가
    # 모든 기차역의 개수와 동일하기때문에
    while stack:
        pop_data = stack.pop()
        if pop_data not in visited:
            visited.append(pop_data)
            stack.extend(train_line[pop_data])
    # 같은경우 True를 리턴해주고 아니면 False를 리턴해준다.
    if len(trains) == len(visited):
        return True
    else:
        return False
def main():
    n,m = map(int,sys.stdin.readline().strip().split())
    trains = list(map(str,sys.stdin.readline().split()))
    train_line = defaultdict(list)
    for _ in range(m):
        start,end = map(str,sys.stdin.readline().split())
        train_line[start].append(end)
        train_line[end].append(start)
    print(solve(trains,train_line))
    

if __name__ == '__main__':
    main()
