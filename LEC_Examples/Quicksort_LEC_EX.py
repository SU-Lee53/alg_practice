import random
random.seed('class_04')

array = [random.randrange(100) for _ in range (30)]
l_arr = len(array)
print("Before Sort:", array,"length:", l_arr)

# 이번에는 앞선 mergeSort와 다르게 array를 전달받는다

def partition(arr, beg, end):
	# randint는 파이썬 내장함수중 거의 유일하게 양쪽이 모두 포함임(나머지는 보통 끝이 불포함) -> 헷갈린다 싶으면 그냥 randrange로 쓰면됨
	ri = random.randrange(beg, end)						# ri = random index -> pivot을 랜덤하게 고를것
	arr[beg], arr[ri] = arr[ri], arr[beg]			# 랜덤으로 정해진 pivot값을 맨 앞값과 바꾸어 가져온다
	pv = arr[beg]															# pv = pivot value

	p, q = beg, end		# 루프에서 증가시키고 검사할 예정이므로 beg를 그냥 넣어도 된다. 아니라면 beg에는 pivot이 있으므로 beg+1이 되어야 한다.
	while True:				# p가 q를 역전하면 루프 끝
		while True:			# p가 증가하는 루프, 먼저 증가하고 검사(반대로 해도 됨)
			p += 1
			# if p >= end: break		# p가 끝까지 도달했을때도 증가를 멈춰야한다. 그러나 어차피 q가 end를 절대 넘어갈 수 없으므로 할 필요 없다.
			if p >= q: break				# p가 q를 넘어가도 증가를 멈춰야한다.
			if arr[p] > pv:	break 	# arr[p]가 pv보다 큰게 발견되면 증가를 멈춘다. pv와 같은값은 left에 있어야 하므로 >=으로 비교하지 않는다
		while True:			# p가 감소하는 루프, 먼저 감소하고 검사(반대로 해도 됨)
			q -= 1
			if p > q: break					# p == q 인 위치는 pivot이 들어갈 자리이므로 p >= q가 아니다
			if arr[q] <= pv: break
		if p >= q: break					# 이미 p가 q보다 크거나 같아져 버렸다면 아래의 스왑을 수행해서는 안된다.
		arr[p], arr[q] = arr[q], arr[p]

	arr[q], arr[beg] = arr[beg], arr[q]		# 맨 왼쪽의 pv을 pivot index가 될 q로 옮겨주어야 한다.
	return q


# 전역변수 array와 이름을 헷갈리지 않도록
def quickSort(arr, beg, end):	# end: exclusive(불포함)
	# quickSort 구현
	# 1. pivot index를 구한다.
	# 2. pi 의 왼쪽을 정렬한다.
	# 3. pi 의 오른쪽을 정렬한다.
	size = end - beg						# end가 불포함이므로 size는 end - beg + 1이 아니다
	if size <= 1: return
	pi = partition(arr, beg, end)			# pi = pivot index
	quickSort(arr, beg, pi)						# end를 불포함하기로 하였으므로 pi-1이 아님
	quickSort(arr, pi + 1, end)				# 위와 마찬가지 이유로 start는 pi임

quickSort(array, 0, l_arr)
print("After Sort:", array)
