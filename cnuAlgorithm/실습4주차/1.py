import sys

def bubbleSort(input_list,words,cnt,isUp):
    # words : 문자 길이, cnt : 진행횟수, isUp : true일경우 오름차순, 아니면 내림차순
    swap_cnt = 0
    return_list = input_list[:]
    for i in range(words):
        # isSwap은 버블정렬이 몇번 진행되는지 카운팅하기위해서 넣음
        isSwap = False
        for j in range(words-1-i):
            # 버블정렬의 과정
            if isUp: # isUp은 true일떄 오름차순,false일때 내림차순으로 정렬해주기위한 부울변수
                if ord(return_list[j])>ord(return_list[j+1]):
                    return_list[j],return_list[j+1] = return_list[j+1],return_list[j]
                    isSwap = True
            else:
                if ord(return_list[j])<ord(return_list[j+1]):
                    return_list[j],return_list[j+1] = return_list[j+1],return_list[j]
                    isSwap = True
        if isSwap:
            # 만약 버블정렬이 진행되었으면(swap이 진행되었으면)
            swap_cnt+=1 #swap_cnt를 1 증가시키고
            if swap_cnt == cnt:
                # 만약 버블정렬을 cnt만큼 진행했을경우 그즉시 bubblesort를 멈추고
                # return_list를 리턴한다(여기서 리턴되는건 cnt만큼만 진행했을때의 결과)
                return return_list
    # cnt보다 일찍 정렬이 끝난경우 완전히 정렬된 형태의 list를 리턴해준다
    return return_list


def main():
    n,m,a = map(str,sys.stdin.readline().strip().split())
    input_list = list(map(str,sys.stdin.readline().strip().split()))
    words = int(n) # 문자열의 길이 : 버블정렬의 경우 최대 길이가 중요하기때문
    cnt = int(m) # 버블정렬을 몇번 진행할것인지
    if a == 'A': # 오름차순으로 할건지 내림차순으로 할건지를 체크하는부분
        isUp = True
    else:
        isUp = False

    # bubbleSort 함수를 진행했을경우 리턴되는건 cnt만큼 진행했을때의 
    # 중간결과 혹은 완전히 정렬된 리스트를 받아온다.
    result_list = bubbleSort(input_list,words,cnt,isUp)
    # result_list를 출력조건에 맞게 출력하기위한 변수 result_str에 넣어준다.
    result_str = result_list[0]
    for i in range(1,len(result_list)):
        result_str = result_str + ' '+result_list[i]
    print(result_str)


if __name__ == '__main__':
    main()
