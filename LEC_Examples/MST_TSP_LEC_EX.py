from collections import defaultdict

edges = [
	(0, 4, 463), (0, 11, 347), (0, 12, 410), (0, 20, 294), (0, 21, 360),
	(1, 5, 61), (1, 10, 343), (1, 17, 395), (2, 6, 162), (2, 10, 431),
	(2, 16, 135), (2, 17, 415), (2, 18, 281), (2, 23, 435), (3, 4, 59),
	(3, 15, 230), (3, 21, 118), (4, 11, 393), (4, 15, 273), (5, 9, 341),
	(5, 10, 333), (5, 23, 427), (6, 10, 268), (6, 12, 432), (6, 14, 465),
	(6, 16, 298), (6, 18, 278), (6, 19, 199), (7, 9, 120), (7, 13, 257),
	(7, 24, 410), (8, 11, 275), (8, 12, 111), (8, 15, 407), (8, 19, 420),
	(8, 20, 481), (9, 10, 341), (9, 23, 253), (9, 24, 357), (11, 15, 141),
	(12, 16, 194), (12, 19, 410), (12, 20, 370), (12, 22, 324), (13, 14, 375),
	(13, 17, 323), (13, 22, 318), (13, 23, 83), (14, 19, 350), (14, 24, 211),
	(15, 21, 177), (16, 18, 348), (16, 20, 421), (18, 24, 377), (19, 22, 211),
	(19, 23, 376), (22, 23, 400), (23, 24, 335),
]
num_vertex = 25
start_index = 16

## Prim

# Build Graph from Input Edge List
# defaultdict: 첫번째 대괄호가 나올때 그 시점에 dict가 없으면 만들어줌
g = defaultdict(dict)	# == {u:dict() for u in rnage(self.n_cities)}
for u,v,w in edges:
	g[u][v] = w
	g[v][u] = w

# Prepare Data Structures
from heapdict import heapdict
D = heapdict()
completed = set()
origins = dict()

# start_index works before main loop
# start_index 까지의 비용은 0이다
# start_index 까지 가려면 start_index 를 통해서 가야한다
D[start_index] = 0
origins[start_index] = start_index

# Prim Main Loop
mst = []
while D:	# 비용이 알려진 것이 있는 동안
	v, w = D.popitem() #가장 작은 비용을 꺼낸다
	completed.add(v)	# v를 내륙에 포함시킨다
	u = origins[v]		# v까지 가려면 u를 통해 가야한다

	if u != v:	# 확정된 점이 시작점이 아니라면
		mst.append((u,v,w))		# u~v까지의 간선을 mst에 추가한다

	for adj, cost in g[v].items():	# 확정되는 점 v의 주위의 점들 adj에 대하여
		if adj in completed: continue	# adj가 이미 completed 안에 있으면 넘어가자
		if adj not in D or D[adj] > cost:		#adj가 D에 없거나 D에 있지만 비용이 비싸면
			D[adj] = cost		# adi까지 가는 비용은 cost이다
			origins[adj] = v		# adj까지 가려면 v를 통해서 가야한다

# print (mst)

## TSP

# Build Graph from MST
mg = defaultdict(set)
for (u,v,w) in mst:
	mg[u].add(v)
	mg[v].add(u)
# print(mg)

# Make Sequence
seq = [start_index]
curr = start_index
while True:
	if curr == start_index and not mg[start_index]: # 시작 위치에 돌아왔는데 더이상 갈곳이 없으면
		break
	for adj in mg[curr]:		# curr 주변의 살아있는 점들 adj에 대하여
		if adj not in seq:					# 방문경로 seq에 안들어있다면
			visit = adj
			mg[curr].remove(adj)
			break
	else:			# 위 loop에서 break한적이 없다면
		visit = mg[curr].pop()	# 아무거나 하나 꺼내자

	seq.append(visit) # seq에 visit를 추가하자
	curr = visit # visit가 새로운 curr가 되게 한다

# print(seq)
# Find Shortcut
visited = set()
index = 0
while index < len(seq):
	curr = seq[index]
	if curr in visited:	# curr가 visited 에 있으면 index는 건드리지 않고
		seq.pop(index)			# seq를 당긴다
	else:
		visited.add(curr)			# visited에 추가해준다
		index += 1

seq.append(start_index)
print(seq)







