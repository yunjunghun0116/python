import sys

def bubbleSort(input_list,words,cnt,isUp):
    # n : 개수, m : 진행횟수, isUp : true일경우 오름차순, 아니면 내림차순
    swap_cnt = 0
    return_list = input_list[:]
    for i in range(words):
        isSwap = False
        for j in range(words-1-i):
            if isUp:
                if ord(return_list[j])>ord(return_list[j+1]):
                    return_list[j],return_list[j+1] = return_list[j+1],return_list[j]
                    isSwap = True
            else:
                if ord(return_list[j])<ord(return_list[j+1]):
                    return_list[j],return_list[j+1] = return_list[j+1],return_list[j]
                    isSwap = True
            
        if isSwap:
            swap_cnt+=1
            if swap_cnt == cnt:
                return return_list
    
    return return_list


def main():
    n,m,a = map(str,sys.stdin.readline().strip().split())
    input_list = list(map(str,sys.stdin.readline().strip().split()))
    words = int(n)
    cnt = int(m)
    if a == 'A':
        isUp = True
    else:
        isUp = False
    result_list = bubbleSort(input_list,words,cnt,isUp)
    result_str = result_list[0]
    for i in range(1,len(result_list)):
        result_str = result_str + ' '+result_list[i]
    print(result_str)


if __name__ == '__main__':
    main()
