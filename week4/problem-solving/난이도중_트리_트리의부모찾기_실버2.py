# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline

def main():
  N = int(input())

  graph = [[] for _ in range(N + 1)]

  for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
  
  visited = [False] * (N + 1)
  parent = [0] * (N + 1)

  def dfs(node):
    visited[node] = True

    for adjacent in graph[node]:
      if not visited[adjacent]:
        parent[adjacent] = node
        dfs(adjacent)

  dfs(1)

  for i in range(2, N + 1):
    print(parent[i])    

if __name__ == "__main__":
  main()