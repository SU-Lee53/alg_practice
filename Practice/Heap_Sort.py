import random

# 힙 정렬
# 1. 전체 배열을 최대힙으로 만든다
# 2. 루트를 맨 마지막 인덱스로 보내고 얘 제외하고 다시 Heapify
# 3. 2번을 계속 반복
# 교수님의 예제에선 0번 인덱스부터 시작하지만 여기에선 1번 인덱스부터 시작해본다.

# 1번부터 시작하는 최대힙의 각종 요소들을 응용하여 정렬을 수행한다.
# -> tree size = 15
# -> n's parent = n // 2
# -> n's left child = 2n
# -> n's right child = 2n+1
# -> n is root = n == 1
# -> n has left child = 2n <= treesize


def Heapify(root, size):
	left = root * 2
	if left >= size: return		# 왼쪽 자식의 인덱스가 힙 사이즈보다 크다면 자식이 없는거니까 리턴
	child = left							# 부모의 자식들 중 더 큰 자식이 child에 들어간다
	right = root * 2 + 1			# 리턴 필요 X. 위에서 왼쪽이 없으면 반환했으니까 왼쪽이 없으면 오른쪽도 없음
	if right < size:					# right가 존재한다면(힙 size보다 작다면)
		if arr[right] > arr[left]:	# 오른쪽 자식이 왼쪽 자식보다 크다면(최대힙이니까 오른쪽이 더 커야함)
			child = right

	if arr[root] < arr[child]:	# 만약 부모가 자식보다 작다면 -> 위치 바꿔줘야함
		arr[root], arr[child] = arr[child], arr[root]
		Heapify(child, size)			# 아래로 내려간 부모를 루트로 다시한번 Heapify
															# 그러면 아래쪽으로 계속 Heapify가 진행되고 자식이 없을때 멈춤



arr = [random.randint(0, 100) for _ in range(101)]
arr[0] = 0
print(f"before sort : {arr}")
count = len(arr)

# 최초 최대힙 생성 수행
last_parent_index = count // 2 								# 자식이 있는 노드중 가장 마지막에 위치한 노드
for n in range(last_parent_index, 0, -1):			# l_p_i에서 뒤로 가면서(전부 자식이 있음) 마지막 1번 인덱스까지 Heapify
	Heapify(n, count)
# 이렇게 한번 최대힙을 만들면 마지막 원소는 정렬이 완료된것이므로 건드리지 않는다

# 끝에서부터 Heapify를 진행해야 다운힙(양쪽이 모두 힙상태일때 부모를 내려 힙을 만드는 과정)을 통해 힙을 만들 수 있다
last_sort_index = count - 1				# 1번부터 시작하므로 1번 Heapify후 마지막의 인덱스는 count
while last_sort_index > 1:			# 뒤에서 앞으로 정렬되므로 마지막으로 정렬된 인덱스가 앞까지 오면 끝
	arr[1], arr[last_sort_index] = arr[last_sort_index], arr[1]		# 힙의 루트노드와 마지막 인덱스를 스왑
	Heapify(1, last_sort_index)			# 루트의 원소가 바뀌었으므로 다시 Heapify를 하여 최대힙으로 만든다
	last_sort_index -= 1									# size == 마지막 정렬된 인덱스임

print(f"after sort : {arr}")

# 문제점: 0번 원소는 정렬이 안됨...