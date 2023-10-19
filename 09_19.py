# 1. Bubble sort
import random
from data_unsorted_a_lot import numbers
numbers = numbers[:100]

arr = [random.randint(0, 100) for _ in range(30)]
print("--Bubble Sort--")
print(f"before sorted {arr}")

for i in range(len(arr) - 1):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"after sorted {arr}")
print('\n')

# 2. Selection Sort
arr = [random.randint(0, 100) for _ in range(30)]
print("--Selection Sort--")
print(f"before sorted {arr}")

for i in range(len(arr)):
    minIndex = i
    for j in range(i, len(arr)):
        # 정렬되지 않은 부분의 최솟값 찾기
        if arr[j] < arr[minIndex]:
            minIndex = j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]



print(f"after sorted {arr}")
print('\n')
# 3. Insertion Sort
arr = [random.randint(0, 100) for _ in range(30)]
print("--Insertion Sort--")
print(f"before sorted {arr}")

for i in range(1, len(arr)):
    insert = i
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]:
            insert = j
        else:
            break

    temp = arr[i]
    for j in range(i, insert, -1):
        arr[j] = arr[j-1]
    arr[insert] = temp

print(f"after sorted {arr}")
print('\n')
