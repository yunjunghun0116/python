import sys
from collections import defaultdict

def anagram(word):
    result = ''.join(sorted(word))
    return result

def solve(word_list):
    # 같은 애너그램을 갖는경우 anagram함수를 진행했을때 받는 리턴값이 동일하기때문에 
    # 애너그램을 key로, 해당 word를 value로 저장하는데 이때 value는 여러개가 될수있기때문에 
    # list형태로 저장한다.
    word_map = defaultdict(list)
    for i in range(len(word_list)):
        word_map[anagram(word_list[i])].append(word_list[i])
    # map에 저장했으면 이제 같은애너그램끼리 묶인상태이기때문에 이를 result라는 array에 
    # 저장한 후에 리턴한다.
    result = []
    for words in word_map:
        result.append(word_map[words])
    return result

def sorting(result):
    # 얕은복사를 통해 정렬해도 원함수에 영향 안주게 한 후에
    check_list = result[:]
    result_list = []
    # 같은 애너그램끼리 정렬 해준후에 result_list에 저장을 해준다.
    for i in range(len(check_list)):
        new_list = sorted(check_list[i])
        result_list.append(new_list)
    return result_list

def main():
    word_list = list(map(str,sys.stdin.readline().strip().lower().split()))
    # 먼저 오름차순 정렬을 진행해준 후에
    words = sorted(word_list)
    # 아래 과정을 진행하게되면 sort_result에는 출력 순서대로
    # 그리고 같은 애너그램끼리도 정렬된 상태이기때문에
    result = solve(words)
    sort_result = sorting(result)
    print_result = []
    # 각 원소마다 string으로 처리해준다음 print_result에 저장해준후에
    for i in range(len(sort_result)):
        sort_str = sort_result[i][0]
        for j in range(1,len(sort_result[i])):
            sort_str = sort_str + ' '+ sort_result[i][j]
        print_result.append(sort_str)
    # print_result의 각 원소는 같은 애너그램끼리 정렬된 상태의 string형태로 저장되어있기때문에
    # 그대로 출력해주기만 하면 된다.
    for i in range(len(print_result)):
        print(print_result[i])



if __name__ == '__main__':
    main()
