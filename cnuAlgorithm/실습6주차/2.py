import sys
from collections import defaultdict
def solve(cups,cnt):
    visited = []
    my_queue = []
    visited.append(0)
    my_queue.extend(cups[0])
    while my_queue:
        val = my_queue.pop(0)
        if val not in visited:
            visited.append(val)
            my_queue.extend(cups[val])
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
    keys = []
    keys.extend(cups.keys())
    print(keys)

if __name__ == '__main__':
    main()