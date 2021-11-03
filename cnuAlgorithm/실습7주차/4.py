import sys
import re
def isDiff(input_num):
    check_num = input_num[::-1]
    check_num_lst = list(check_num)
    for i in range(len(check_num_lst)):
        if check_num_lst[i] == '6':
            check_num_lst[i] = '9'
        elif check_num_lst[i] == '9':
            check_num_lst[i] = '6'
    check_num = ''.join(check_num_lst)
    if int(input_num) != int(check_num):
        return True
    else:
        return False
def solve(cnt):
    p  = re.compile('[01689]+')
    result = 0
    for i in range(1,cnt+1):
        s = p.findall(str(i))
        if len(s)!= 0 and  len(s[-1]) == len(str(i)):
            if(isDiff(str(i))):
                result+=1
    return result
    
def main():
    cnt = int(sys.stdin.readline())
    print(solve(cnt))

if __name__ == '__main__':
    main()
