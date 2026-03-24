# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
  N, M = map(int, input().split())

  # 그래프 이중 리스트로 초기화
  graph = [[] for _ in range(N + 1)]

  # 무방향 그래프 생성
  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  # 방문 노드 리스트
  visited = [False] * (N + 1)

  # connected component 개수
  cnt = 0
  
  def dfs(node):
    visited[node] = True

    for adjacent in graph[node]:
      if not visited[adjacent]:
        dfs(adjacent)
  
  for i in range(1, N + 1):
    if not visited[i]:
      cnt += 1
      dfs(i)
  
  print(cnt)

if __name__ == "__main__":
  main()