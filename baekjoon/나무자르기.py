import sys

def solve(trees,need):
    left = 1
    right = max(trees)
    while left <= right:
        mid = (left+right)//2
        get_trees = 0
        for tree in trees:
            if tree >= mid:
                get_trees += tree - mid
        if get_trees >= need:
            left = mid + 1
        else:
            right = mid - 1
    return right



def main():
    len,need = map(int,sys.stdin.readline().strip().split())
    trees = list(map(int,sys.stdin.readline().strip().split()))
    print(solve(trees,need))

if __name__ == '__main__':
    main()
