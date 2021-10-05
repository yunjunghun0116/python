import sys
import re

def solve(input_list):
    p = re.compile('(\D+)(\d+)')
    for i in range(len(input_list)):
        print(p.match(input_list[i]).group(1))
        print(p.match(input_list[i]).group(2))
    input_list.sort(key=lambda x : (p.match(x).group(1).lower(),int(p.match(x).group(2))))
    return input_list
def main():
    cnt = int(sys.stdin.readline().strip())
    for i in range(cnt):
        input_list = ['img12.png','img10.png','img02.png','img1.png','IMG01.GIF','img2.JPG']
        print(solve(input_list))

if __name__ == '__main__':
    main()
