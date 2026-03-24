# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

import sys
from collections import deque
input = sys.stdin.readline

def main():
  N = int(input())
  
  matrix = [list(map(int, input().split())) for _ in range(N)] # 칸에 적힌 숫자들 저장
  visited = [[False] * N for _ in range(N)]

  def dfs(x, y):

    # 1. 범위 체크
    if x < 0 or x >= N or y < 0 or y >= N:
      return False
    # 2. 방문 체크
    if visited[x][y]:
      return False
    # 3. 목적지 체크
    if x == N - 1 and y == N - 1:
      return True
    # 4. 방문 표시
    visited[x][y] = True
    # 5. 해당 칸에서 점프할 수 있는 범위
    jump = matrix[x][y]
    # 6. 오른쪽이나 아래쪽 한 곳이라도 갈 수 있으면 됨
    return dfs(x, y + jump) or dfs(x + jump, y)

  print("HaruHaru" if dfs(0, 0) else "Hing")
  # def bfs(coordinates):
  #   queue = deque()
  #   queue.append((0, 0))
  #   visited = set()

  #   while queue:
  #     curr = queue.popleft() # (0, 0) 에서 시작
  #     visited.add(curr)

  #     if curr == (N-1, N-1):
  #       return "HaruHaru"
      
  #     x, y = curr # 0, 0
  #     curr_val = matrix[x][y]

  #     if y + curr_val < N:
  #       right = (x, y + curr_val)
  #       if right not in visited:
  #         queue.append(right)
  #     if x + curr_val < N:
  #       below = (x + curr_val, y)
  #       if below not in visited:
  #         queue.append(below)
    
  #   return "Hing"
  
  # print(bfs((0, 0)))

if __name__ == "__main__":
  main()