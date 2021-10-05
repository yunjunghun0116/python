import sys

def main():
    size = int(sys.stdin.readline())
    words = []
    words_set = set()

    for _ in range(size):
        input_str = str(sys.stdin.readline().strip())
        if input_str in words_set:
            continue
        else:
            words.append(input_str)
            words_set.add(input_str)
    
    result = sorted(words,key=lambda x:(len(x),x))
   
    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    main()