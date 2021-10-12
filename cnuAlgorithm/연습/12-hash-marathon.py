import sys
import collections
def compareCollections(p,f):
    i = collections.Counter(p) - collections.Counter(f)
    return list(i.keys())

def main():
    participants = list(map(str,sys.stdin.readline().strip().split()))
    finishers = list(map(str,sys.stdin.readline().strip().split()))
    # list를 반환받았을때 * 을 붙혀주게되면 알아서 split해서 출력해준다.
    print(*compareCollections(participants,finishers))

if __name__ == '__main__':
    main()
