from random import randint, shuffle

arr = [randint(0, 100) for _ in range(100)]
print(f"before: {arr}")


def insertionSort(left, right):		# 성능향상을 위한 삽입정렬
	for i in range(left+1, right +1):
		temp = arr[i]
		j = i - 1
		while j >= left and arr[j] > temp:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = temp


def quickSort(left, right):
	if right < left + 8:
		return
	pivot = partition(left, right)
	quickSort(left, pivot - 1)		# pivot보다 왼쪽 그룹을 다시 quickSort
	quickSort(pivot + 1, right)		# pivot보다 오른쪽 그룹을 다시 quickSort
	# pivot은 위치가 고정되있으므로 포함시키지 않는다


def partition(left, right):
	pi = randint(0, count - 1)						# pi = Pivot Index
	pivot = arr[pi]			# pivot = value

	p, q = left, right + 1		# 비교 인덱스

	while True:					# p가 q를 역전할때까지
		while True:				# 왼쪽에서 pivot보다 큰값을 찾을때까지
			p += 1
			if q < p: break
			if p > right or arr[p] >= pivot: break
			# 왼쪽에서 pivot보다 큰 값을 찾았다

		while True:				# 오른쪽에서 pivot보다 작은값을 찾을때까지
			q -= 1
			if q < p: break
			if q < left or arr[q] <= pivot: break
			# 오른쪽에서 pivot 보다 큰 값을 찾았다

		if p >= q: break	# p와 q가 만날때까지 진행

		arr[p], arr[q] = arr[q], arr[p]
		# 이제 p 이하에는 pivot보다 작은값만, q 이상에는 pivot보다 큰값만 있다

	# 이제 pivot의 위치를 확정시킨다
	# pivot은 왼쪽 그룹 중 가장 큰값이므로 q위치로 옮긴다(왼쪽이 p ~ q, 오른쪽이 q+1 ~ end)
	# left가 q와 같다면 pivot보다 작은것이 하나도 없다는 뜻이므로 옮길 필요가 없다
	if left != q:
		arr[left], arr[q] = arr[q], arr[left]

	return q	# 결정된 pivot의 위치를 리턴한다

def GetPivot(left, right):
	_left, _mid, _right = arr[left], arr[left+right//2], arr[right]
	avg = (_left + _mid + _right) // 2
	diff = 100
	index = 0
	for i in count:
		temp = arr[i] - avg
		if temp < diff:
			index = i
			diff = temp

	return arr[index]

count = len(arr)
quickSort(0, count-1)
insertionSort(0, count - 1)
print(f"after: {arr}")

# print("now only insertionsort")
# shuffle(arr)
# print(f"before: {arr}")
#
# insertionSort(0, count - 1)
#
# print(f"after: {arr}")


