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
g = defaultdict(dict)
for u,v,w in edges:
	g[u][v] = w
	g[v][u] = w

# Prepare Data Structures
from heapdict import heapdict
D = heapdict()
completed = set()
origins = dict()

# start_index works before main loop
D[start_index] = 0
origins[start_index] = start_index

# Prim Main Loop
mst = []
while D:
	v, w = D.popitem()
	completed.add(v)
	u = origins[v]

	if u != v:
		mst.append((u,v,w))

	for adj, cost in g[v].items():
		if adj in completed: continue
		if adj not in D or D[adj] > cost:
			D[adj] = cost
			origins[adj] = v

## TSP

# Build Graph from MST
mg = defaultdict(set)
for (u,v,w) in mst:
	mg[u].add(v)
	mg[v].add(u)

# Make Sequence
seq = [start_index]
curr = start_index
while True:
	if curr == start_index and not mg[start_index]:
		break
	for adj in mg[curr]:
		if adj not in seq:
			visit = adj
			mg[curr].remove(adj)
			break
	else:
		visit = mg[curr].pop()

	seq.append(visit)
	curr = visit

# Find Shortcut
visited = set()
index = 0
while index < len(seq):
	curr = seq[index]
	if curr in visited:
		seq.pop(index)
	else:
		visited.add(curr)
		index += 1

seq.append(start_index)
print(seq)