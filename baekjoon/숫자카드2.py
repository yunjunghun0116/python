import sys
from collections import defaultdict

def main():
    nums_len = int(sys.stdin.readline().strip())
    nums = list(map(int,sys.stdin.readline().strip().split()))
    count_len = int(sys.stdin.readline().strip())
    counts = list(map(int,sys.stdin.readline().strip().split()))
    nums_map = defaultdict(int)
    for i in nums:
        nums_map[i]+=1
    result = []
    for i in counts:
        result.append(nums_map[i])
    print(*result)

if __name__ == '__main__':
    main()

