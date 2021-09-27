import sys

class Room:
    def __init__(self,start,end):
        self.start = start
        self.end = end

def main():
    size = int(sys.stdin.readline())
    roomList = []
    for _ in range(size):
        start,end = map(int,sys.stdin.readline().split())
        roomList.append(Room(start,end))
    sorted(roomList,key = lambda x : (x.end,x.start))

    cnt = 1
    end_time = roomList[0].end
    for i in range(1,size):
        if roomList[i].start >= end_time:
            cnt+=1
            end_time = roomList[i].end
         
    print(cnt)
    
    

    
if __name__ == '__main__':
    main()

