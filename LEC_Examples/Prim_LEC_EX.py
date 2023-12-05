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
# prim은 간선중심인 Kruskal과 달리 정점 중심의 알고리즘
# 주변 점들을 확인하고 가장 가중치가 적은 정점을 가져온다
# 이때 주변 점들을 가장 확인하기 좋은 형태는 adjacency list 형태이므로 위 edge list를 변경해야한다
# adjacenct list는 dictionary of dictionary 형태가 가장 Best

mst = []
# g = [dict() for _ in range(num_vertex)]		# 정점 수만큼의 빈 dictionary를 만듬
import collections
#	g = dict() 		#	{ v:dict() for _ in range(num_vertex)}		# v(dict)를 key로 하는 dictionary 생성
# 위는 collections의 defaultdict(dict)로 수행 가능
g = collections.defaultdict(dict)	# 비어있는 value에는 빈 dict를 넣음, 과제는 이걸로 ㄱㄱ
# 이 g가 adj list

# s, e, w == start, end, weight
for s, e, w in edges:	# edge list를 adjacency list로 만드는 loop
	# d = g[s] = w
	# d.append({e,w})	-> 이 2줄은 아래 1줄과 같음
	g[s][e] = w
	g[e][s] = w		# 추가적인 과정 필요없도록 하기 위해서 가중치를 반복저장(인접행렬이 대칭이면 2번저장하는것과 유사)

import heapdict	# pip으로 설치 필요함

D = heapdict.heapdict()	# D에는 adj:weight 저장
origins = dict()	# ~까지 가려면 여기서부터 가야한다는 정보. 쉽게말해 from임 fr:{to:weight}
completed = set()	# 확정된 내륙(mst)를 저장할 집합

start_index = 15
completed.add(start_index)

# for adj, weight in g[start_index].items(): # 시작점 주위의 점들과의 정보를 초기에 넣고 시작함
# 	D[adj] = weight
# 	origins[adj] = start_index
# 아래 main loop에서 위 내용이 반복되므로 그냥 안하고 아래만 추가함
D[start_index] = 0	# 이거만 넣어놓으면 알려진게 이거밖에 없으므로 메인루프 시작시 알아서 start_index의 정보(현재 0)이 튀어나옴

# main loop
while D: # D 안에 원소가 하나라도 남아있다면 이라는 의미	# len(D) >= 0:	# 더이상 알려진 다리(간선) 정보가 없다면 끝
	# fix_to: 여기까지 다리를 짓자, fix_w: 이 다리의 가중치
	fix_to,fix_w = D.popitem()	# popitem: 가장 비용이 작은 value를 끄집어냄
	completed.add(fix_to)
	if fix_to != start_index:	# 최초 1회는 추가 안함
		fix_fr = origins[fix_to]		# fix_to까지 가려면 어디서 출발? -> origins 리스트가 그걸 알려줌
		mst.append((fix_fr, fix_to, fix_w))
	# 지금까지 간선 확정. 이제 확정된 점 주위의 정보 갱신
	for adj, adj_w in g[fix_to].items():		# adj = 도착점
		# 아래의 4가지를 수행한다.

		# 1. already in mst? : ignore
			# 이미 MST에 연결되어있으면 갱신 필요없다
		if adj in completed: continue
		# 2. not adj in D: add
			# 지금까지 알려지지 않았던 정보라면 추가한다
		# 3. D[adj] <= adj_w(fix_to ~ adj) : ignore
			# 지금 확정된 점부터 주변점 거리보다 이미 알려진 거리가 더 작다면 갱신할 필요가 없다
		# 4. 3. D[adj] > adj_w(fix_to ~ adj) : update
			# 지금 확정된 점부터 주변점의 거리보다 이미 알려진 거리가 더 크다면 갱신한다
		# 2,3,4번은 python의 특징을 이용하여 축약가능 -> dict에서 add와 update는 동일
		if not adj in D or D[adj] > adj_w:
			D[adj] = adj_w
			origins[adj] = fix_to	# adj까지 가려면 지금 확정된 점부터 출발해야함

print(mst)