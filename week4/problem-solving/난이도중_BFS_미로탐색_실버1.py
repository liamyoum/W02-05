# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

import sys
from collections import deque
input = sys.stdin.readline

def main():
  N, M = map(int, input().split())

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left
  maze = [list(map(int, input().rstrip())) for _ in range(N)]

  def bfs():
    q = deque([(0, 0)])
    maze[0][0] = 2 # 방문 처리를 위해, 출력 조정 필요

    while q:
      x, y = q.popleft()

      if x == N - 1 and y == M - 1:
        return maze[x][y] - 1

      for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
          q.append((nx, ny))
          maze[nx][ny] = maze[x][y] + 1

  print(bfs())

if __name__ == "__main__":
  main()