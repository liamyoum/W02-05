# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190





def sys_input():
  return sys.stdin.readline().rstrip()




if __name__ == "__main__":
  main()


"""
import sys
from collections import deque

# 방향 벡터, 순서대로 2d matrix에서 위, 오른쪽, 아래, 왼쪽으로 한 칸 이동할 때 이동량
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# d에 따라 그 방향으로 한 칸 움직이는 함수
# 움직이다가 종료 조건 만나면 True 반환, 아니면 위치 업데이트 하고 False 반환

def move_snake(n: int, d: int, board:list[list[int]], snake: deque[tuple[int, int]]) -> bool:
  head_x, head_y = snake[0]
  dx, dy = DIRECTIONS[d]
  nx, ny = head_x + dx, head_y + dy
  # 보드 벽에 부딪히거나 자기 몸에 박았을 때
  if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 1:
    return True # 이게 True 여야 is_finished 가 True
  
  # 종료 조건 안 만났을 때
  if board[nx][ny] == 0:
    tail_x, tail_y = snake.pop() # 머리가 첫 번째 요소임
    board[tail_x][tail_y] = 0 # 보드에서 꼬리 있던 자리 0으로 업데이트
  
  board[nx][ny] = 1 # 머리가 새롭게 옮긴 자리 1로 업데이트
  snake.appendleft((nx, ny)) # 새로운 머리 위치 snake에 업데이트
  return False
  

def solve(n: int, apples: list[tuple[int, int]], commands: list[tuple[int, str]]) -> int:
  board = [[0] * n for _ in range(n)] # N * N 보드 생성, 빈칸 0
  for x, y in apples:
    board[x - 1][y - 1] = 2 # 사과는 2로 표현

  snake = deque([(0, 0)]) # 뱀을 표현, 뱀이 차지하고 있는 좌표 쌍을 갖고 있음
  board[0][0] = 1
  direction = 1 # 0: 상 1: 우, 2: 하, 3: 좌
  time = 0
  cmd_idx = 0

  while True:
    time += 1
    is_finished = move_snake(n, direction, board, snake)
    if is_finished:
      break
    
    if cmd_idx < len(commands) and commands[cmd_idx][0] == time:
      rotation = commands[cmd_idx][1]
      if rotation == "L":
        direction = (direction - 1) % 4
      else: # rotation == "D"
        direction = (direction + 1) % 4

      cmd_idx += 1 # 이거 꼭 if문 분기 안으로 들어와야함
    
  return time

def main() -> None:
  N = int(sys_input()) # 보드 크기
  K = int(sys_input()) # 사과 개수
  apples = [tuple(map(int, sys_input().split())) for _ in range(K)]
  L = int(sys_input()) # 방향 변환 횟수
  commands = [(int(cmd[0]), cmd[1]) for cmd in (sys_input().split() for _ in range(L))]

  answer: int = solve(N, apples, commands)
  print(answer)

"""