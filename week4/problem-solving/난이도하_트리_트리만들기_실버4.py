# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

"""
문제
n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.
항상 정답이 존재하는 경우만 입력으로 주어진다.
트리는 사이클이 없는 연결 그래프이고, 리프는 차수가 1인 노드를 의미한다.
"""

"""
입력
첫째 줄에 n과 m이 주어진다. (3 ≤ n ≤ 50, 2 ≤ m ≤ n-1)
"""

"""
출력
첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다. 트리의 정점은 0번부터 n-1번까지 이다.
"""

import sys
input = sys.stdin.readline

def main():
  n, m = map(int, input().split())
  
  if m == 2:
    for v in range(n - 1): # 간선 개수는 노드 개수 - 1
      print(v, v + 1)
  
  elif m >= 3:
    leaf_to_add = m - 2
    hub_node = 1
    for v in range(n - leaf_to_add - 1):
      print(v, v + 1)
    
    for v in range(n - leaf_to_add, n):
      print(hub_node, v)

if __name__ == "__main__":
  main()