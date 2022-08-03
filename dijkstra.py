import heapq

def Dijkstra(s):
	dist[s]=0						# 자기 자신은 0
	heap = []
	heapq.heappush(heap, [0, s])	# 거리를 앞에 두어 거리 비교
	while heap:						# heap이 비어있지 않을 때 까지
		w, v = heapq.heappop(heap)
		for n, n_w in dij[v]:		# node 탐색
			n_w+=w
			if n_w < dist[n]:		# 거리가 이전보다 짧다면 거리 갱신 및 힙에 추가
				dist[n] = n_w
				heapq.heappush(heap,[n_w,n])

n = int(input()) 					# 노드의 개수
m = int(input()) 					# edge 개수
inf = 1000000000000 				# 1조 무한대보다는 작지만 그래도 큰 수
dij = [[] for i in range(n+1)]
dist = [inf]*(n+1)					# 결과가 저장 될 곳
for i in range(m):
	u, v, w = [int(j) for j in input().split()]
	dij[u].append([v, w])
# print(dij)

Dijkstra(0)                         # 시작 노드 0이라고 가정
for i in range(n):
	if dist[i] != inf:
		print("%d" % dist[i],end=" ")
	else:
		print("inf",end=" ")