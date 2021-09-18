import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    odd_cnt = 0
    class_odd=[]
    even_cnt = 0
    class_even=[]
    while True:
        lst = list(map(str,sys.stdin.readline().split()))
        classes = int(lst[0])
        name = lst[1]
        if classes == 0 and name == "0":
            break
        if classes%2 == 0:
            class_even.append([classes,even_cnt,name])
            even_cnt+=1
        else:
            class_odd.append([classes,odd_cnt,name])
            odd_cnt+=1
            

    class_odd.sort()
    class_even.sort()
    data = [[] for _ in range(n+1)]

    for odd_data in class_odd:
        classes,cnt,name = odd_data
        if len(data[classes]) >= m:
            continue
        else:
            data[classes].append(name)

    for even_data in class_even:
        classes,cnt,name = even_data
        if len(data[classes]) >= m:
            continue
        else:
            data[classes].append(name)

    odd_result = []
    even_result = []


    def sorting(arr):
        if len(arr) <= 1:
            return list(arr)
        else:
            first,second = arr[0],arr[1]
           
            if len(str(first)) < len(str(second)):
                return list(arr)
            elif len(first) == len(second):
                result = [first,second]
                result.sort()
                return result
            else:
                result = [first,second]
                result.reverse()
                return result
            
    
    
    for i in range(1,len(data)):
        datas = sorting(data[i])
        if i%2 == 0:
            even_result.append((i,datas))
        else:
            odd_result.append((i,datas))
    
    for result in odd_result:
        index,data = result
        return_str = str(index)
        for i in range(len(data)):
            print(return_str,data[i])


    for result in even_result:
        index,data = result
        return_str = str(index)
        for i in range(len(data)):
            print(return_str,data[i])
    
    

    
if __name__ == '__main__':
    main()