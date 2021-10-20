import sys
from collections import defaultdict

def solve(cups,cnt):
    visited = []
    my_queue = []
    visited.append(0) # 문제조건이 첫번째 컵에서 시작이기 때문에
    my_queue.extend(cups[0]) # 첫번째 컵에서 갈수있는 모든곳을 다 넣어준다.
    while my_queue:
        val = my_queue.pop(0)
        if val not in visited:
            visited.append(val)
            my_queue.extend(cups[val])
    # 여기까지 진행했을경우 0번째에서 갈 수 있는 모든곳이 연결되어있기때문에
    # 마지막 컵이 갈수있는 곳(visited 배열) 에 저장되어있는지 판단한다.
    if cnt-1 in visited:
        return True
    else:
        return False


def main():
    cups = defaultdict(list)
    cnt = int(sys.stdin.readline().strip())
    for i in range(cnt):
        input_lst = list(map(int,sys.stdin.readline().strip().split()))
        cups[i].extend(input_lst)
    print(solve(cups,cnt))

if __name__ == '__main__':
    main()