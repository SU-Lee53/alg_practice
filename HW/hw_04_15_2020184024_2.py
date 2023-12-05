# _2 Chained Matrix Multiplication

d = [5,9,3,7,2,6,3,9,3]	# 5*9, 9*3, 3*7, 7*2, 2*6, 6*3, 3*9, 9*3
mc = len(d) - 1

INF = float('inf')
C = [[0 for _ in d] for _ in d]
P = [[0 for _ in d] for _ in d]

for sps in range(2, mc + 1):
	for s in range(1, mc - sps + 2):
		e = s + sps - 1
		mult = INF
		for k in range(s, e):
			t = C[s][k] + C[k+1][e] + d[s-1] * d[k] * d[e]
			if mult > t:		# 갱신해야한다면
				mult = t
				P[s][e] = k
		C[s][e] = mult

def getMultStr(s,e):
	if s == e: return f'A{s}'
	p = P[s][e]
	return f'({getMultStr(s,p)} x {getMultStr(p+1, e)})'


print(f'곱셈수={C[1][mc]} 수식={getMultStr(1,mc)}')


