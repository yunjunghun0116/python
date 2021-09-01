def main():
    while True:
        try:
            n = int(input(''))
            if n % 2 == 0:
               print('Hello, Coding Test!')
            else:
                print('Hello, Algorithm!')
        except EOFError:
            break

if __name__ == '__main__':
    main()

