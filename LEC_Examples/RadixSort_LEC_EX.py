import random

random.seed('class_04')
array = [random.randrange(1000) for _ in range(50)]
l_arr = len(array)
print(f"Before Sort: {array}")
maxv = max(array)
print(f"Max Value: {maxv}")

div = 1
results = array[:]
while div <= maxv:
	counts = [0] * 10	# 자릿수 별 0~9까지만 갯수셈
	for v in array:
		digit = v // div % 10
		counts[digit] += 1

	for i in range(len(counts) - 1):
		counts[i+1] += counts[i]

	for i in range(l_arr-1, -1, -1):
		v = array[i]
		digit = v // div % 10
		counts[digit] -= 1
		ri = counts[digit]  # ri = result index
		results[ri] = v
	array = results[:]

	div *= 10

print("after sort: ", array)
exit()
# 3. radix Sort

counts = [0 for _ in range(maxv + 1)]	# 갯수를 셀 리스트
print("Counts Array Created: ", counts, len(counts))

for v in array:												# 갯수 세기
	counts[v] += 1
print("Elements Counts: ", counts, len(counts))

for i in range(len(counts) - 1):			# 갯수를 더해서 index로 바꿈
	counts[i + 1] += counts[i]

print("Element Index: ", counts)

# results = [None for _ in range(l_arr)]		# 정렬된 리스트가 별도로 필요함
results = [None] * l_arr
# results = array			# 이건 안됨. results에 array가 참조되어 들어오기 때문
# results = array[:]	# 이건 됨.  results 에 array가 slicing되어 복사되서 들어오기 떄문

for i in range(l_arr - 1, -1, -1):
	v = array[i]
	counts[v] -= 1
	ri = counts[v]	# ri = result index
	results[ri] = v

print("After Sort", results)