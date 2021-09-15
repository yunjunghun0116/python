import sys

def main():
    while True:
        input_num = int(sys.stdin.readline())
        if input_num == 0:
            break
        else:
            str_num = str(input_num)
            length = len(str_num)
            isbool = True
            for i in range(length//2+1):
                if str_num[i] == str_num[length-1-i]:
                    continue
                else:
                    isbool = False
            if isbool == True:
                print('yes')
            else:
                print('no')


if __name__ == '__main__':
    main()

