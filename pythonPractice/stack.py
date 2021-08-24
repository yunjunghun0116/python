import stack

my_stack = list()

for i in range(5):
    my_stack.append(i)

#재귀 연습
def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data - 1)
        print('returned',data)

recursive(4)

# -1번 인덱스는 결국 배열의 마지막 인덱스를 나타낸다
print(my_stack[-1])
