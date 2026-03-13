# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

"""
문제
N-Queen 문제는 크기가 N * N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 N이 주어진다. (1 <= N < 15)
"""

"""
출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""

def main():
  N = int(input())
  queen = [-1] * N
  count = 0

  isused_col = [False] * N
  isused_diag1 = [False] * (2 * N - 1)
  isused_diag2 = [False] * (2 * N - 1)

  def dfs(row):
      nonlocal count # global은 함수 바깥, 파일 최상단 스코프를 뜻하는 키워드고
      # nonlocal은 이 함수 바로 바깥 영역의 키워드

      if row == N:
          count += 1
          return

      for col in range(N):
          diag1 = row + col
          diag2 = row - col + N - 1

          # 이미 누가 사용중이면 못 놓음 (가지치기)
          if isused_col[col] or isused_diag1[diag1] or isused_diag2[diag2]:
              continue
          
          # 놓는다 (Choose)
          isused_col[col] = True # col 열은 이미 사용중
          isused_diag1[diag1] = True # diag1 대각선은 이미 사용중
          isused_diag2[diag2] = True # diag2 대각선은 이미 사용중
          # 다음 행 탐색 (Explore)
          dfs(row + 1)
          # 되돌린다 (Unchoose)
          isused_col[col] = False
          isused_diag1[diag1] = False
          isused_diag2[diag2] = False

  dfs(0)
  print(count)

if __name__ == "__main__":
  main()