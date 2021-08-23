size = int(input())
data = [int(input()) for i in range(size)]
now = data[size-1]
cnt = 1

for i in range(len(data)):
    pop_data = data.pop()
    if now < pop_data:
        now = pop_data
        cnt += 1
    if now == max:
        break
print(cnt)
