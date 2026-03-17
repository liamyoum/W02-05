# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

def main():
  arr = list(map(int, input().split()))
  A, B, C = arr[0], arr[1], arr[2]

  # B가 약 21억까지 가니까, O(B) = 2 * 10^9.
  # B를 log 처리해야 시간 초과 X
  # B는 A의 exponent

  """
  1. 이 함수는 무엇을 반환하는가? ->  A^b % C를 반환
  재귀함수의 인자는 보통 문제 크기를 줄이기 위해 바뀌는 것이므로
  줄어드는 값은 인자로 꼭 전달
  재귀에서는 부모-자식 한 레벨 관계만 이해하고 재귀 함수 잘 정의하는 것에만 집중
  """
  def power(b): # 줄어드는 값만 인자로 전달

    # base case
    if b == 1:
      return A % C

    half = power(b // 2) # half = A ** (b // 2) % c
    # 더 작은 문제의 답을 어떻게 조합하는가?
    if b % 2 == 0:
      return half * half % C
    else:
      return A * half * half % C
    
  print(power(B))
if __name__ == "__main__":
  main()