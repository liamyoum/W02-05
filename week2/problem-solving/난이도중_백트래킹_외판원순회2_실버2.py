# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

"""
문제
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다. 
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외)
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 
비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. 
W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.
항상 순회할 수 있는 경우만 입력으로 주어진다.
"""

"""
출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
"""

import sys
input = sys.stdin.readline


def main():
  N = int(input()) # 도시의 수, N, 최대 10
  W = [list(map(int, input().split())) for _ in range(N)] # 행렬 완성
  min_cost = [10 ** 8]
  visited = [False] * N

  def backtrack(cur, cost, cnt):

    # 이미 비싸면 가지치기
    if cost > min_cost[0]:
      return

    # base case
    if cnt == N:
      if W[cur][0] != 0 and min_cost[0] > cost + W[cur][0]:
        min_cost[0] = cost + W[cur][0]
      return

    for i in range(N):
      # 아직 안 가봤고 길 있으면
      if not visited[i] and W[cur][i] != 0:
        # 선택
        visited[i] = True
        # backtrack
        backtrack(i, cost + W[cur][i], cnt + 1)
        # 취소
        visited[i] = False

  visited[0] = True
  backtrack(0, 0, 1)

  print(min_cost[0])

if __name__ == "__main__":
  main()