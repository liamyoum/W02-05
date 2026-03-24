# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
from collections import deque
input = sys.stdin.readline

def main():
  V = int(input()) # 컴퓨터의 수
  E = int(input()) # 연결 수

  # 그래프를 인접 리스트로 구현
  graph = [[] for _ in range(V + 1)]

  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프라 양쪽 다 추가해야함

  def bfs(start):
    queue = deque([start])
    
    # visited도 bool 리스트로 변환
    visited = [False] * (V + 1)
    visited[start] = True

    infected = 0

    while queue:
      computer = queue.popleft()

      for adjacent in graph[computer]:
        if not visited[adjacent]:
          visited[adjacent] = True
          queue.append(adjacent)
          infected += 1
    
    return infected
  
  print(bfs(1))

if __name__ == "__main__":
  main()