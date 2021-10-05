import sys
from collections import defaultdict

def main():
    size = int(sys.stdin.readline())
    words = []
    words_map = defaultdict(list)
    words_set = set()
    for _ in range(size):
        input_str = sys.stdin.readline().strip()
        if input_str in words_set:
            continue
        else:
            words.append(input_str)
            words_set.add(input_str)
    for i in range(len(words)):
        length = len(words[i])
        words_map[length].append(words[i])

    result = []
    for i in words_map:
        result.append((i,words_map[i]))
    result.sort()
    for i in range(len(result)):
        result[i][1].sort()
        for j in range(len(result[i][1])):
            print(result[i][1][j])

    

    

if __name__ == '__main__':
    main()
