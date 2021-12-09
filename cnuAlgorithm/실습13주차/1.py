import sys

def pibonacci(n):
    longarr = [0 for _ in range(100)]
    for i in range(n+1):
        if i == 1 or i == 2 :
            longarr[i] = 1
        else:
            longarr[i] = longarr[i-1] + longarr[i-2]
    return longarr[n]

def main():
    inputNum = int(sys.stdin.readline().strip())
    print(pibonacci(inputNum))

if __name__ == '__main__':
    main()
    