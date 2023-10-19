from random import *

arr = [randint(0, 30) for _ in range(30)]
print(f"before: {arr}")

def mergeSort(left, right):
	if right <= left: return		# 우측 인텍스가 좌측인덱스보다 작거나 같음 == 정렬할게 없거나 1개임
	mid = (left + right) // 2		# 중앙값을 잡는다
	mergeSort(left, mid)
	mergeSort(mid+1, right)
	merge(left, mid+1, right)


def merge(left, right, end):		# 왼족:[left ~ right - 1], 오른쪽:[right ~ end]
	merged = []										# 임시 정렬 리스트
	l, r = left, right						# 왼쪽, 오른쪽 시작 인덱스
	while l < right and r <= end:	# 만약 한쪽이라도 더이상 남은 원소가 없으면 끝
		if arr[l] <= arr[r]:
			merged.append(arr[l])			# 왼쪽이 더 작으니까 왼쪽을 정렬에 추가
			l += 1										# 왼쪽 다음원소 입갤
		else:
			merged.append(arr[r])
			r += 1										# 위와 같음

	while l < right:							# 왼쪽에 원소가 남아있으면
		merged.append(arr[l])				# 정렬에 왼쪽 남은원소 싹다 추가
		l += 1
	while r <= end:								# 오른쪽에 원소가 남아있다면
		merged.append(arr[r])				# 정렬에 오른쪽 남은원소 싹다 추가
		r += 1

	arr[left:end+1] = merged			# 임시 리스트를 원래 리스트로 옮김



count = len(arr)
mergeSort(0, count - 1)
print(f"after: {arr}")
