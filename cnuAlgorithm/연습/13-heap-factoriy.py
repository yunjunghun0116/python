import sys
import heapq #default : 최소힙이기때문
def factory(stock,dates,supplies,k):
    import_count = 0
    stock_heap = []
    index = 0
    while (stock < k):
        for i in range(index,len(dates)):
            if dates[i] <= stock: #수입할 수 있다. 
                heapq.heappush(stock_heap,(-supplies[i],supplies[i]))
                index = i + 1
            else:
                break
        max_amount = heapq.heappop(stock_heap)[1]
        stock += max_amount
        import_count += 1
    return import_count


def main():
    initial_amount = int(sys.stdin.readline())
    import_date = list(map(int,sys.stdin.readline().strip().split()))
    import_amount = list(map(int,sys.stdin.readline().strip().split()))
    regular_import_date = int(sys.stdin.readline())

    print(factory(initial_amount,import_date,import_amount,regular_import_date))

if __name__ == '__main__':
    main()
