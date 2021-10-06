import sys

# 전역변수 current_cnt는 합병이 몇번 이뤄질것인지를 정하는것
current_cnt = 0
def merge_sort(input_list,isUp,merge_cnt):
    # input_list의 길이가 1인경우는 즉 원소가 하나이기때문에 그대로
    # 리턴해주면 된다.
    if len(input_list) <= 1:
        return input_list
    else:
        # input_list의 원소가 여러개의 경우는(2개 이상)
        # left,right를 나누어 진행해줄것이고, 그 기준은
        # 중간값(mid) 를 통해서 진행한다.
        mid = len(input_list)//2
        left = input_list[:mid]
        right = input_list[mid:]
        # left,right가 각각 mergesort가 진행되면 그떈 정렬된상태로
        # 반환되기때문에 그대로 merge를 진행하면 된다.
        left_list = merge_sort(left,isUp,merge_cnt)
        right_list = merge_sort(right,isUp,merge_cnt)
        # merge는 합병과정으로서 left_list,right_list를 
        # 정렬하면서 합치는 과정을 진행한다.
        return merge(left_list,right_list,isUp,merge_cnt)
def merge(left,right,isUp,merge_cnt):
    # 여기서 전역변수가 쓰이는데 merge_cnt는 몇번진행할지를 받는 변수이고
    # current_cnt는 합병이 몇번 진행되었는지를 알려주는 함수이고
    global current_cnt
    if merge_cnt <= current_cnt:
        # 만약 current_cnt 즉 합병이 merge_cnt와 같거나 많아질경우
        # (사실상 같은경우/많아질수가 없음 같은경우에서 끊기기때문에)
        # 합병을 진행하지않고 left+right 배열 즉 합병이전배열그대로 반환한다.
        return left+right
    left_cnt = 0
    right_cnt = 0
    result = [] # left와 right를 정렬해서 집어넣어줄 배열(리턴배열)
    left_length = len(left)
    right_length = len(right)
    # 아직 merge_cnt만큼 합병을 진행하지 않았다면 
    # 이제부터 합병을 진행해주는데 먼저 left,right 둘중 하나가 완전히 result라는
    # 배열 안으로 정렬하며 넣어준다.
    while left_cnt < left_length and right_cnt < right_length:
        # isUp은 오름차순으로 할지, 내림차순으로 할지 정하는거고 true의 경우
        # 오름차순, false의 경우는 내림차순으로 정렬하는것이다.
        if isUp:
            if ord(left[left_cnt]) > ord(right[right_cnt]):
                result.append(right[right_cnt])
                right_cnt+=1
            else:
                result.append(left[left_cnt])
                left_cnt+=1
        else:
            if ord(left[left_cnt]) < ord(right[right_cnt]):
                result.append(right[right_cnt])
                right_cnt+=1
            else:
                result.append(left[left_cnt])
                left_cnt+=1
    # 만약 left가 아직 result에 다들어가지 않았다면 나머지부분 그대로 집어넣어주고
    while left_cnt < left_length:
        result.append(left[left_cnt])
        left_cnt+=1
    # 같은 방식으로 right가 아직 result에 다들어가지 않았을경우도 그대로 집어넣어준다.
    while right_cnt < right_length:
        result.append(right[right_cnt])
        right_cnt+=1
    # 위에서 그냥 넣어주는 이유는 만약 left가 다 들어갔다면 right의 나머지부분은 결국 left의 최댓값보다
    # 크다는 말이기때문에 그대로 넣어주면 된다.

    # 전역변수 current_cnt에 1을 추가해준다 -> 중단타이밍 정하는 부분
    current_cnt+=1
    return result



def main():
    n,m,a = map(str,sys.stdin.readline().strip().split())
    input_list = list(map(str,sys.stdin.readline().strip().split()))
    words_cnt = int(n)
    merge_cnt = int(m)
    # 오름차순인지 내림차순인지를 정하는 부분
    if a == 'A':
        isUp = True
    else:
        isUp = False
    # 위에서 merge_sort를 진행한 후에 들어오는 부분은 merge_cnt만큼만 진행된 후의 
    # 부분 결과를 리턴해주고, 이부분을 result로 받았기때문에
    # result를 str화 해서 출력조건에 맞게 출력하는 과정
    result = merge_sort(input_list,isUp,merge_cnt)
    return_str = result[0]
    for i in range(1,len(result)):
        return_str = return_str + ' ' + result[i]
    print(return_str)

    


if __name__ == '__main__':
    main()
