import sys

def solve(base,stations):
    result = 0
    for b in base:
        distance_min = float('inf')
        for s in stations:
            distance_min = min(distance_min,abs(b-s))
        result = max(result,distance_min)
    return result
    
def main():
   base = list(map(int,sys.stdin.readline().strip().split()))
   stations = list(map(int,sys.stdin.readline().strip().split()))
   print(solve(base,stations))

if __name__ == '__main__':
    main()
