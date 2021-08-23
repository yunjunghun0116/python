import stack

my_stack = list()

for i in range(5):
    my_stack.append(i)

def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data - 1)
        print('returned',data)

recursive(4)

