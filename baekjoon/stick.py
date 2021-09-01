import sys

def main():
    size = int(sys.stdin.readline())
    data = [int(sys.stdin.readline()) for i in range(size)]
    now = data[size-1]
    cnt = 1

    for i in range(len(data)):
        pop_data = data.pop()
        if now < pop_data:
            now = pop_data
            cnt += 1
        if now == max:
            break
    print(cnt)
    
if __name__ == '__main__':
    main()

