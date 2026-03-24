# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
  # 테스트 케이스 개수 K를 입력 받는다.
  K = int(input())
  # 테스트 케이스 만큼 반복문을 돈다.
  for _ in range(K):
    # 반복문 안에서 V와 E를 입력 받는다.
    V, E = map(int, input().split())
    # 그래프 이중 리스트와 노드의 색상을 저장할 색상 배열을 만든다.
    graph = [[] for i in range(V + 1)]
    color = [0] * (V + 1)
    # E 개수만큼 돌면서 양방향으로 그래프 연결
    for _ in range(E):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)
  
    # DFS 돌리기
    # 현재 노드 x를 인자로 받음
    def dfs(x):
      for adjacent in graph[x]:
        if color[adjacent] == 0:
          color[adjacent] = -color[x]
          if not dfs(adjacent):
            return False
        
        elif color[adjacent] == color[x]:
          return False
      
      return True
    
    is_bipartite = True
    
    for i in range(1, V + 1):
      if color[i] == 0:
        color[i] = 1
        if not dfs(i):
          is_bipartite = False
          break
    
    print("YES" if is_bipartite else "NO")

if __name__ == "__main__":
  main()