import sys
import collections
def compareCollections(p,f):
    i = collections.Counter(p) - collections.Counter(f)
    # map의 형태로 저장되며 key : count 의 형식으로 저장되고,
    # key에 실질적인 이름이 저장되고, - 를 통하면 있는것들중에서는 사라지지만
    # 없는이름에 대해서는 진행되는것이 없다
    return list(i.keys())

def main():
    participants = list(map(str,sys.stdin.readline().strip().split()))
    finishers = list(map(str,sys.stdin.readline().strip().split()))
    # list를 반환받았을때 * 을 붙혀주게되면 알아서 split해서 출력해준다.
    print(*compareCollections(participants,finishers))

if __name__ == '__main__':
    main()
