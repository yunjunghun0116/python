import sys

def main():
    size = int(sys.stdin.readline())
    cup = [0 for _ in range(size+1)]
    dp = [0 for _ in range(size+1)]
    for i in range(size):
        cup[i+1] = int(sys.stdin.readline())
    else:
        for i in range(1,size+1):
            if i == 1:
                dp[i] = cup[i]
            elif i == 2 :
                dp[i] = cup[i]+cup[i-1]
            else:
                dp[i] = max(dp[i-3]+cup[i-1]+cup[i],dp[i-2]+cup[i],dp[i-1])


    print(dp[-1])


if __name__ == '__main__':
    main()

