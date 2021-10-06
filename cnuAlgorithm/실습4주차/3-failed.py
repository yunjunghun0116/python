import sys
from collections import defaultdict

def anagram(word):
    result = ''.join(sorted(word))
    return result


def main():
    input_words = list(map(str,sys.stdin.readline().strip().lower().split()))
    words_set = set()
    words_map = defaultdict(list)
    for i in range(len(input_words)):
        anagrams = anagram(input_words[i])
        if anagrams in words_set:
            words_map[anagrams].append(input_words[i])
        else:
            words_set.add(anagrams)
            words_map[anagrams].append(input_words[i])

    
    result = []
    find_set = set()
    for i in range(len(input_words)):
        anagrams = anagram(input_words[i])
        if anagrams in find_set:
            continue
        else:
            find_set.add(anagrams)
            result.append(words_map[anagrams])

    # 입력받은 값중 맨 앞의 값의 ascii코드에맞추어 정렬 진행 후에
    for i in range(len(result)):
        for j in range(len(result)-1-i):
            if ord(str(result[j][0][0]))>ord(str(result[j+1][0][0])):
                result[j],result[j+1] = result[j+1],result[j]
    
    # 각 원소들끼리도 오름차순으로 정렬해주기위해 첫번째 위치를 기준으로 정렬진행
    for i in range(len(result)):
        for j in range(len(result[i])):
            for k in range(len(result[i])-1-j):
                if ord(str(result[i][k][0]))>ord(str(result[i][k+1][0])):
                    result[i][k],result[i][k+1] = result[i][k+1],result[i][k]
    
    for i in range(len(result)):
        print_str = result[i][0]
        for j in range(1,len(result[i])):
            print_str = print_str + ' '+ result[i][j]
        print(print_str)
        



if __name__ == '__main__':
    main()
