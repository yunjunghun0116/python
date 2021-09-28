import sys

def is_anagram(s1,s2):
    if ''.join(sorted(s1)) == ''.join(sorted(s2)):
        return True
    return False
    
    
def main():
    input_cnt = int(sys.stdin.readline())
    for _ in range(0,input_cnt):
        #\n을 지운후 lowercase로 바꿔주고 공백을 없애준후에 진행한다.
        word1 = sys.stdin.readline().strip().lower().replace(' ','')
        word2 = sys.stdin.readline().strip().lower().replace(' ','')
        print(word1,word2)
        if is_anagram(word1,word2):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()
