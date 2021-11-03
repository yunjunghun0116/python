import sys
from collections import defaultdict
def solve(trains,train_line):
    visited = []
    stack = []
    visited.append(trains[0])
    stack.extend(train_line[trains[0]])
    while stack:
        pop_data = stack.pop()
        if pop_data not in visited:
            visited.append(pop_data)
            stack.extend(train_line[pop_data])

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
