import random
random.seed('class_04')
array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(f"Before Sort: {array}")


# 1. Heap Sort

# 파이썬 기본제공 힙 생성 함수
# array = list(map(lambda e: -e, array))	# 기본제공 heapify가 min힙만 만들어주므로 max힙을 만들기 위해 원소를 음수로 바꿈
# array = list(map(lambda e:(-e, e), array))	# 위와 같지만 원래 리스트 보존을 위해 음수로 바꾼것과 튜플로 묶음
# print(array)
# import heapq
# heapq.heapify(array)
# print(f"heapified {array}")

def downHeap(root, size):
	ch = root * 2 + 1  # left child의 index

	# pyramid of doom vs early return
	# pyramid of doom: 들여쓰기가 너무 많은 코드, early return: pyramid of doom이 되지 않도록 조기에 리턴
	# ~~가 존재하면 ~~수행보다, ~~가 존재하지 않으면 return하는것이 더 좋음
	if ch >= size: return

	if ch + 1 < size and array[ch] < array[ch+1]:  # right child가 존재
			ch = ch + 1

	if array[root] >= array[ch]: return

	array[root], array[ch] = array[ch], array[root]
	downHeap(ch, size)
	# 함수의 끝에서만 재귀호출 -> tail recursion
	# 많은 컴파일러들이 tail recursion 은 재귀형태가 아니도록 바꿔주는 경우가 있으므로 이경우 성능향상이 생길수도 있음(다 그런건 아님)


for i in range(l_arr // 2 - 1, -1, -1):  # 다운힙은 절반만 진행해도 됨, range의 2번째 인자는 미포함이기 때문에 0까지 돌리려면 -1로 호출해야함
	downHeap(i, l_arr)

print(f"First Heapified: {array}")

heapSize = l_arr		# 루프를 돌때마다 heapSize를 하나씩 줄여나감
for i in range(l_arr-1, 0, -1):	# 마지막 1개 남았을때는 수행하지 않아도 됨
	heapSize -= 1
	array[0], array[heapSize] = array[heapSize], array[0]
	print(f"#{l_arr - i}", array)
	downHeap(0, heapSize)

print(f"After Sort: {array}")
