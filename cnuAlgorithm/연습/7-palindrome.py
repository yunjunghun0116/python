import sys

def is_palindrome(s):
    #reverse화 해서 넘겨주기
    return s[::-1]
    
def main():
    input_cnt = int(sys.stdin.readline())
    word_list = []
    word_list = [sys.stdin.readline().strip() for i in range(0,input_cnt)]

    for s in word_list:
        print(is_palindrome(s) )


if __name__ == '__main__':
    main()
