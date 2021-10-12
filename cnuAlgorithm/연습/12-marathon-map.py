import sys
from collections import defaultdict

def solve(p_list,c_list):
    result = []
    word_map = defaultdict(list)
    for p in p_list:
        map_key = len(p)
        word_map[map_key].append(p)
    for c in c_list:
        map_key = len(c)
        for i in range(len(word_map[map_key])):
            if word_map[map_key][i] == c:
                word_map[map_key].remove(c)
                break
    for key in word_map:
        for value in word_map[key]:
            result.append(value)
    return result

def main():
    participant = list(map(str,sys.stdin.readline().strip().split()))
    completion = list(map(str,sys.stdin.readline().strip().split()))
    print(*solve(participant,completion))
if __name__ == '__main__':
    main()
