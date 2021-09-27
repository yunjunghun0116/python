import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    users = [[] for _ in range(n+1)]
    cnt = 0
    while True:
        room,name = sys.stdin.readline().split()
        if room == "0" and name == "0":
            break
        room = int(room)
        users[room].append((name,cnt))
        cnt+=1
    
    for i in range(1,n+1):
        #정렬하는 방법
        lst = sorted(users[i][:m],key = lambda x : (len(x[0]), x[0]))
        users[i] = lst
    
    
    odd_result = []
    even_result = []
    for i in range(1,n+1):
        if i % 2 != 0:
            for user in users[i]:
                name,cnt = user
                odd_result.append((i,name))
        else:
            for user in users[i]:
                name,cnt = user
                even_result.append((i,name))

    for i in range(len(odd_result)):
        print(odd_result[i][0],odd_result[i][1])
    for i in range(len(even_result)):
        print(even_result[i][0],even_result[i][1])
            
    
    
if __name__ == '__main__':
    main()

