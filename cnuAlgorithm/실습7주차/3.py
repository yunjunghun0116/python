import sys
import re
def solve(input_str):
    mac1 = re.compile('[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}-[0-9a-fA-F]{2}')
    mac2 = re.compile('[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}')
    ip  = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
    mac1_lst = mac1.findall(input_str)
    mac2_lst = mac2.findall(input_str)
    ip_lst = ip.findall(input_str)
    if len(mac1_lst) == 1:
        return 'MAC'
    elif len(mac2_lst) == 1:
        return 'MAC'
    elif len(ip_lst) == 1:
        check_iplst = ip_lst[-1].split('.')
        for i in range(len(check_iplst)):
            check_num = int(check_iplst[i])
            if check_num >= 256 or check_num < 0:
                return 0
        return 'IP'
    else:
        return 0
def main():
    while True:
        input_str = sys.stdin.readline().strip()
        if input_str == '':
            break
        print(solve(input_str))
    

if __name__ == '__main__':
    main()
