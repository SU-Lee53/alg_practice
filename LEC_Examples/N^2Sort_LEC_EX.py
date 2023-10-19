from random import randint, shuffle

print("<Bubble Sort>")
arr = [randint(0, 50) for _ in range(10)]
print('before : ', arr)

count = len(arr)
end = count - 1
while end > 0:
    last = 1
    for i in range(end):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            last = i + 1
        end = last - 1

print('after : ', arr, end='\n\n')

print("<Selection Sort>")
shuffle(arr)
print('before : ', arr)

count = len(arr)
for a in range(count-1):    # 마지막 1개 남았을땐 비교해서 자리 바꿀필요가 없다
    min_value = arr[a]
    min_at = a
    for b in range(a+1, count):
        if min_value > arr[b]:
            min_value = arr[b]
            min_at = b
    arr[a], arr[min_at] = arr[min_at], arr[a]

print('after : ', arr, end='\n\n')

print("<Insertion Sort>")
shuffle(arr)
print('before : ', arr)

for i in range(1, count):
    v = arr[i]
    j = i
    while j > 0:
        if arr[j-1] > v:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        else:
            arr[j] = v
            break

print('after : ', arr, end='\n\n')

print("<Shell Sort>")
shuffle(arr)
print('before : ', arr)
g = len(arr)
GAPS = []
while g > 1:
    g = g // 3
    GAPS.append(g)

print(GAPS)

while True:
    for start in range(gap, count):
        v = arr[start]
        i = start



print('after : ', arr, end='\n\n')
