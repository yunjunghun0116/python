import sys

def multiple_sort(input_list):
    result = sorted(input_list, key=lambda x: (len(x),x))
    return result

def main():
    input_list = list(input().split(' '))
    print(multiple_sort(input_list))

if __name__ == '__main__':
    main()
