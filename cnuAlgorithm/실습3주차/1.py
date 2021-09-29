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
    return isAnagram
    
    
def main():
    m,n = map(str,sys.stdin.readline().lower().strip().split())
    print(is_anagram(m,n))

if __name__ == '__main__':
    main()
