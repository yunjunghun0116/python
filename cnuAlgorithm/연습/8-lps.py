import sys

def longest_palindrome(s):
    table = [[False for _ in range(len(s))] for _ in range(len(s))]
    longest = 0

    for i in range(len(s)):
        for j in range(len(s)-i):
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest = i + 1
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest = i+1

    return longest
    
def main():
    input_cnt = int(sys.stdin.readline())
    for _ in range(0,input_cnt):
        s = sys.stdin.readline().strip().lower()
        print(longest_palindrome(s))


if __name__ == '__main__':
    main()
