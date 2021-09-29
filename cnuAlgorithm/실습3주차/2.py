import sys

def solve(s : str):
    length = len(s)
    table = [[False for _ in range(length)]for _ in range(length)]
    for i in range(length):
        for j in range(length-i):
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest = s[j:i+j+1]
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest = s[j:i+j+1]

    return longest

def main():
    input_str = sys.stdin.readline().strip()
    print(solve(input_str))
    

    
if __name__ == '__main__':
    main()
