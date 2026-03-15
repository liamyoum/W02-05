# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

def main():
  N = int(input()) # size
  blue_cnt = 0
  white_cnt = 0
  matrix = [list(map(int, input().split())) for _ in range(N)]
  
  def is_same(x, y, size):
    # matrix의 경우 재할당 아니고 읽기만 하는거라 따로 스코프 선언 필요 X
    base = matrix[x][y]
    # 가장 첫 번째 요소와 다른 요소들이 같은지 전부 체크
    for i in range(x, x + size):
      for j in range(y, y + size):
        if base != matrix[i][j]:
          return None
    # 파란색
    if base == 1:
      return 1
    # 흰색
    elif base == 0:
      return 0

  def divide_matrix(x, y, size):
    # 이 두 함수는 내부에서 값을 변경하기 때문에 nonlocal 선언해줘야함, 재할당하는거라서
    nonlocal blue_cnt
    nonlocal white_cnt

    same = is_same(x, y, size)
    if same == 1:
      blue_cnt += 1
      return
    elif same == 0:
      white_cnt += 1
      return
    
    half = size // 2
    divide_matrix(x, y, half)
    divide_matrix(x, y + half, half)
    divide_matrix(x + half, y, half)
    divide_matrix(x + half, y + half, half)

  divide_matrix(0, 0, N)
  print(white_cnt)
  print(blue_cnt)

if __name__ == "__main__":
  main()