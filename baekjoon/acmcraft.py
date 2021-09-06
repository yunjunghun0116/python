import sys

class Building:
    def __init__(self,data,prev = None,next = None):
        self.prev = prev
        self.data = data
        self.next = next

def main():
    testCnt = int(sys.stdin.readline())
    result = []
    for i in range(testCnt):
        buildingCnt,buildingRuleCnt = map(int,sys.stdin.readline().split())
        print(buildingRuleCnt)
    
if __name__ == '__main__':
    main()
    
    
    
