# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

def main():
  N, M, V = map(int, input().split()) # 4, 5, 1

  graph = [[] for _ in range(N + 1)]

  for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  for i in range(1, N + 1):
      graph[i].sort()
  
  def dfs(start):

    stack = []
    stack.append(start)

    visited = [False] * (N + 1)

    result = []
    while stack:
      node = stack.pop()

      if visited[node]:
        continue

      visited[node] = True
      result.append(node)

      for adjacent in reversed(graph[node]):
        if not visited[adjacent]:
          stack.append(adjacent)

    return result
  
  def bfs(start):

    q = deque()
    q.append(start)

    visited = [False] * (N + 1)
    visited[start] = True

    result = [start]
    while q:
      node = q.popleft()
    
      for adjacent in graph[node]:
        if not visited[adjacent]:
          q.append(adjacent)
          visited[adjacent] = True
          result.append(adjacent)
    
    return result

  print(*dfs(V))
  print(*bfs(V))
if __name__ == "__main__":
  main()