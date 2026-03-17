# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
# 이거 PyPy3 으로 돌려야 돌아가는데..?

import sys

def sys_input():
  return sys.stdin.readline().rstrip()

def main():
  first_line = list(map(int, sys_input().split()))
  N, M = first_line[0], first_line[1]
  
  # 이전역의 번호와 다음역의 번호를 저장해놓는 배열
  # EX) prev[3] -> 3번 역의 이전 역
  # EX2) next[3] -> 3번 역의 다음 역
  prev = [0] * (10 ** 6 + 1) # 역 번호 최댓값
  next = [0] * (10 ** 6 + 1)
  result = []

  stations = list(map(int, sys_input().split()))

  for i, s in enumerate(stations): # O(N)
    # 첫 번째 요소일 때
    if i == 0:
      prev[s] = stations[-1]
      next[s] = stations[i + 1]
    # 배열 마지막 요소일 때
    elif i == len(stations) - 1:
      prev[s] = stations[i - 1]
      next[s] = stations[0]
    else: # 중간에 있는 요소들
      prev[s] = stations[i - 1]
      next[s] = stations[i + 1]

  # 공사 진행
  for _ in range(M):
    construction = sys_input().split()
    con_type = construction[0]
    i = int(construction[1])
    if len(construction) == 3:
      j = int(construction[2])

    if con_type == "BN": 
      result.append(next[i])
      x = next[i]
      next[i] = j
      prev[j] = i
      next[j] = x
      prev[x] = j
    elif con_type == "BP":
      result.append(prev[i])
      x = prev[i]
      prev[j] = x
      next[x] = j
      next[j] = i
      prev[i] = j

    elif con_type == "CN":
      x = next[i]
      y = next[x]
      result.append(x) 
      next[i] = y
      prev[y] = i
      
    elif con_type == "CP":
      x = prev[i]
      y = prev[x]
      result.append(x)
      prev[i] = y
      next[y] = i

  sys.stdout.write("\n".join(map(str, result)))

if __name__ == "__main__":
  main()