W=[[0,3,8,math.inf,-4],[math.inf,0,math.inf,1,7],[math.inf,4,0,math.inf,math.inf],[2,math.inf,-5,0,math.inf],[math.inf,math.inf,math.inf,6,0]]

L=[[math.inf for i in range(5)] for i in range(5)]

def extend_shortest_path(L,W):
	n = len(L)
	L_dash=[[math.inf for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				L_dash[i][j]=min(L_dash[i][j] , L[i][k]+W[k][j])
	return L_dash
def slow_all_pairs_shortest_path(W):
	n=len(W)
	base_L = W
	for m in range(1,n):
		L_temp=[[math.inf for i in range(n)] for i in range(n)]
		L_temp=extend_shortest_path(base_L ,W)
		base_L =L_temp
	return base_L 

def faster_all_pairs_shortest_path(W):
	n=len(W)
	base_L=W
	for m in range(1,n):
		L_temp=[[math.inf for i in range(n)] for i in range(n)]
		L_temp=extend_shortest_path(base_L ,base_L)
		base_L=L_temp
		m=2*m
	return base_L

	final_L=faster_all_pairs_shortest_path(W)
>>> final_L
[[0, 1, -3, 2, -4], [3, 0, -4, 1, -1], [7, 4, 0, 5, 3], [2, -1, -5, 0, -2], [8, 5, 1, 6, 0]]

