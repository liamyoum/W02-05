# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

import sys
input = sys.stdin.readline
from collections import deque

def main():
  N = int(input())
  # 모든 작업을 완료하기 위해 필요한 최소 시간 구하기
  
  # 선행 관계를 나타내기 위해 그래프 생성 필요
  graph = [[] for _ in range(N + 1)]
  # 작업 별 걸리는 시간을 저장할 time 배열 생성 필요
  time = [0] * (N + 1)
  # 진입차수 정보 저장할 indegree 배열 생성 필요
  indegree = [0] * (N + 1)
  # 작업 별 최소 완료 시각을 저장할 dp 배열 생성 필요
  dp = [0] * (N + 1)

  # graph, time, indegree 초기값 저장
  for i in range(1, N + 1):
    line = list(map(int, input().split()))
    time[i] = line[0]
    indegree[i] = line[1]
    for prerequisite in line[2:]:
      graph[prerequisite].append(i)
  
  # topological sort 문제는 queue로 구현한다.
  
  # 큐 생성
  q = deque()
  # indegree = 0 인 node들을 queue에 먼저 다 enqueue
  for i in range(1, N + 1):
    if indegree[i] == 0:
      q.append(i)
      # 진입 차수가 없으면 최소 완료 시각은 그 작업 소요 시간과 동일하다.
      dp[i] = time[i]
  
  while q:
    cur = q.popleft()

    # 인접한 노드를 순회하면서 간선을 제거하고, dp[nxt]를 업데이트
    for nxt in graph[cur]:
      dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
      indegree[nxt] -= 1

      # 만약 인접 노드도 진입차수가 0이 되었다면, queue에 enqueue
      if indegree[nxt] == 0:
        q.append(nxt)
  
  print(max(dp))

if __name__ == "__main__":
  main()