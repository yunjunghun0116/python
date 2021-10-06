import sys


def merge_sort(input_list,isUp):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list)//2
        left = input_list[:mid]
        right = input_list[mid:]
        left_list = merge_sort(left,isUp)
        right_list = merge_sort(right,isUp)
        return merge(left_list,right_list,isUp)
def merge(left,right,isUp):
    left_cnt = 0
    right_cnt = 0
    result = []
    left_length = len(left)
    right_length = len(right)
    while left_cnt < left_length and right_cnt < right_length:
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
    while left_cnt < left_length:
        result.append(left[left_cnt])
        left_cnt+=1
    while right_cnt < right_length:
        result.append(right[right_cnt])
        right_cnt+=1
    return result



def main():
    n,m,a = map(str,sys.stdin.readline().strip().split())
    input_list = list(map(str,sys.stdin.readline().strip().split()))
    words_cnt = int(n)
    merge_cnt = int(m)
    if a == 'A':
        isUp = True
    else:
        isUp = False
    result = merge_sort(input_list,isUp)
    print(result)

    


if __name__ == '__main__':
    main()
