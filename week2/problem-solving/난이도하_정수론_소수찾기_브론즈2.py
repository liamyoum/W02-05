# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

"""
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

"""
입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""

"""
출력
주어진 수들 중 소수의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

def main():
  # 에라토스테네스의 체 사용
  N = int(input()) # 입력받는 값 개수
  num_list = list(map(int, input().split()))
  max_num = max(num_list) # 최댓값
  is_prime = [True] * (max_num + 1) # 0부터 max_num까지 True를 리스트에 넣어 저장

  is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아니므로 처음에 처리해주기

  for i in range(2, int(max_num ** 0.5) + 1): # 소수 카운터
    if is_prime[i]: # i가 소수일 경우
      for j in range(i * i, max_num + 1, i): # i의 배수들 전부 제거할 것
        is_prime[j] = False
  
  print(sum(is_prime[n] for n in num_list))

if __name__ == "__main__":
  main()