import sys

def is_anagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')   
        c1[pos] +=1 
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')   
        c2[pos] +=1 
    isAnagram = True
    j = 0
    while j < 26 and isAnagram:
        if c1[j] != c2[j]:
            isAnagram = False
        j+=1
    print(c1)
    print(c2)
    return isAnagram
    
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
