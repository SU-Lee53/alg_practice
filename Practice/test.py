import random

def insertionSort(arr, size):
	for i in range(1, size):
		v = arr[i]
		for j in range(i, 0, -1):
			if arr[j-1] > v:
				arr[j], arr[j-1] = arr[j-1], arr[j]
			else:
				arr[j] = v
				break


arr = [random.randrange(100) for _ in range(30)]
print(arr)
insertionSort(arr, len(arr))
print(arr)


