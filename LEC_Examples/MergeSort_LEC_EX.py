import random
random.seed('class_04')

array = [random.randrange(100) for _ in range (30)]
l_arr = len(array)
print("Before Sort:", array,"length:", l_arr)

# 이번 mergeSort는 array를 전달받지 않고 시작과 끝을 전달받는다. 필요한 부분만 정렬해야할 때가 있기 때문


def merge(start, mid, end):	# mid is in left, end is inclusive
	merged = []
	l, r = start, mid+1
	while l <= mid and r <= end:		# l과 r이 모두 원소가 남아있을때까지, mid는 왼쪽에 있으므로 l <= mid, end는 오른쪽에 포함되므로 r <= end
		if array[l] <= array[r]:			# Stable 하려면 비교가 <= 가 되어야함
			merged.append(array[l])
			l += 1
		else:
			merged.append(array[r])
			r += 1

	# 위 루프를 빠져나오면 2개 배열중 하나는 원소가 남아있게 된다.
	# 그러므로 아래의 과정으로 남을 원소들을 merged에 넣어주어야 한다.
	# while l <= mid:									# 왼쪽에 원소가 남아있다면
	# 	merged.append(array[l])
	# 	l += 1
	# while r <= end:									# 오른쪽에 원소가 남아있다면
	# 	merged.append(array[r])
	# 	r += 1
	#
	# 위 과정은 아래의 과정으로 대체가 가능하다
	if l <= mid:					# 왼쪽에 원소가 남아있다면
		merged += array[l:mid+1]	# mid 포함이므로 mid+1		# append로 넣으면 배열에 배열이 통째로 들어가므로 배열 합치기로 넣어주어야한다.
		array[start:end + 1] = merged  # 파이썬에서 slicing은 뒤쪽 원소는 미포함이므로 end + 1을 해주어야 한다.
	else:
		# merged += array[r:end+1]	# end 포함이므로 end + 1
		# 여기서 원래 배열에 합치려면 범위가 바뀌어야한다.
		array[start:r] = merged

	# 아래 원래 배열에 넣는 과정은 위에서 수행 가능하다
	# array[start:end + 1] = merged  # 파이썬에서 slicing은 뒤쪽 원소는 미포함이므로 end + 1을 해주어야 한다.



def mergeSort(start, end):	# end: inclusive(포함)
	# mergeSort 구현
	# 1. 왼쪽 절반을 정렬한다.
	# 2. 오른쪽 절반을 정렬한다.
	# 3. merge(병합) 한다.

	# size = end - start + 1		# 끝을 포함하기로 하였다면 Size는 end-start에서 +1을 해주어야 한다
	# if size <= 1: return			# 10~9까지 정렬과 같은 잘못된 호출의 경우 size가 음수가 될수 있음
	# 													# 위와같은 경우 보통 버그임을 알리고 프로그램을 종료하는것이 좋음
	# 위 2줄은 아래 1줄로 요약가능
	if start >= end: return

	mid = (start + end) // 2	# mid is in left
	mergeSort(start, mid)
	mergeSort(mid + 1 , end)
	merge(start, mid, end)
	return


mergeSort(0, l_arr-1)
print("After Sort:", array)