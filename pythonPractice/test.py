import queue

my_queue = queue.Queue()
my_queue.put((1,'wow'))
my_queue.put((3,'wow'))
my_queue.put((2,'wow'))

for i in range(3):
    a = my_queue.get()
    print(a)

#개행문자
print('"I\'m a good boy"')

queue_list = list()
queue_list.append('wow')
print(queue_list[0])
print(queue_list.pop())
print(len(queue_list))

for i in range(30):
    queue_list.append(i)

for i in range(len(queue_list)):
    print(i)