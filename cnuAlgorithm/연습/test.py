import sys
import re

def solve(input_str):
    p = re.compile('^\d{2}.\d{2}.\d{2}')
    num_list = p.findall(input_str)
    print(num_list)
def main():
    input_str = sys.stdin.readline().strip()
    print(solve(input_str))
    
    
if __name__ == '__main__':
    main()