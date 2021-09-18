import sys

def main():
    stack = []
    while True:
        inputStr = sys.stdin.readline().rstrip()
        if inputStr == '고무오리 디버깅 시작':
            continue
        if inputStr == '문제':
            stack.append(1)
        elif inputStr == '고무오리':
            if len(stack) == 0:
                stack.append(1)
                stack.append(1)
            else:
                stack.pop()
        else:
            if len(stack) == 0:
                print('고무오리야 사랑해')
            else:
                print('힝구')
            break

    
if __name__ == '__main__':
    main()

