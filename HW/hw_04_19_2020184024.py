import random
random.seed('class_04')
n_pts = 40
n_clusters = 5

class Point:
    def __init__(self):
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 1000)
    def __repr__(self):
        return f'({self.x},{self.y})'

pts = [ Point() for _ in range(n_pts) ]
print(f'Points = {pts}')

def distance_sq_between(i1, i2):
    p1, p2 = pts[i1], pts[i2]
    return (p1.x-p2.x)**2+(p1.y-p2.y)**2

from heapdict import heapdict
D = heapdict()      # (-distance_sq, k_th_center_index)
C = [] # centers

for k in range(n_clusters):
    # k번째 center 를 결정한다
    if k==0: #첫번째이면
        center = random.randrange(n_pts)
    else:
        center, _ = D.popitem()
    # center = random.randrange(n_pts) if k == 0 else D.popitem()[0]

    # 이번에 추가된 센터를 기록한다
    D[center] = 0, k
    C.append(center)

    # 모든 점에 대해 거리갱신을 (필요하면) 합니다
    for i in range(n_pts):
        # 방금 추가된 센터까지의 거리를 구해서
        dsq = distance_sq_between(center, i)
        # dists 딕셔너리에 갱신해준다
        if not i in D or -D[i][0] > dsq:
            D[i] = -dsq, k
            # Min-Heap 이므로 음수로 기록해야 최대값을 얻을 수 있으며,
            # 가까운 센터가 몇번째 센터인지도 함께 저장한다

    clusters = [ [] for _ in range(n_clusters) ]
    # n_clusters 개수만큼 빈 배열을 준비한다
    for i in range(n_pts): # 모든 점들에 대하여
        # 정점 i 가 몇번째 center 와 가까운지 알아내자
        ci = D[i][1]
        clusters[ci].append(pts[i])

print(f'D = {dict(D)}')
print(f'clusters = {clusters}')

from welzl import welzl
# 제일 큰 원의 반지름을 max_r 에 저장한다
max_r = 0
for ci in range(n_clusters):
    x, y, r = welzl(clusters[ci]) # 반지름 r 을 구한다
    print(f'{ci} - {len(clusters[ci]):2d} points: ({x:.1f}, {y:.1f}) r: {r:.1f}')
    if max_r < r: max_r = r

print(f'Max R = {max_r:.1f}')
