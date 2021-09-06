def main():
    max = 0
    while True:
        try:
            n = int(input('Input Num : '))
            if n > max:
                max = n
        except EOFError:
            break
        print('Max : ',max)

if __name__ == '__main__':
    main()

