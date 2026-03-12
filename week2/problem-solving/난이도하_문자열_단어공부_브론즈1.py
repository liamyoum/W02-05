# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

"""
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
"""

"""
입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.
"""

"""
출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""

import sys
input = sys.stdin.readline
from collections import Counter

def main():
  s = input()[:-1] # \n이 딕셔너리에 저장되는 것을 방지
  # alphabet마다 빈도수 저장한 딕셔너리 생성 (다 대문자)
  c_dict = Counter(s.upper())

  # 최빈값 찾기
  max_frequency = max(c_dict.values())
  
  # 최빈값을 가진 글자가 복수일 수 있으니, 최빈값 가진 글자들을 모두 리스트에 저장
  max_frequency_alphabet = [k for k, v in c_dict.items() if v == max_frequency]

  print(max_frequency_alphabet[0]) if len(max_frequency_alphabet) == 1 else print('?')

# 2와 3을 한 번에 할 방법... 즉, 문자열 순회하면서 최빈값과 최빈값 가진 문자 개수와 최빈값 가진 문자라는 3개의 상태를 한 번에 관리
def main2():

  c_dict = {}
  max_frequency = 0 # 최빈값
  max_char = '' # 최빈값을 가진 문자
  max_count = 0 # 최빈값을 가진 문자의 개수
  s = input()[:-1] # 개행 문자 제거

  # 1. 문자열 순회하면서 카운트
  for c in s:
    c = c.upper()
    if c in c_dict:
      c_dict[c] += 1
    else:
      c_dict[c] = 1
    
    current_frequency = c_dict[c]

    if max_frequency < current_frequency:
        max_frequency = current_frequency
        max_count = 1
        max_char = c
    elif max_frequency == current_frequency:
        max_count += 1
    # 딕셔너리 완성 + 최빈값 계산 및 최빈값 가진 문자 개수까지 계산 완료

  print('?') if max_count > 1 else print(max_char)


if __name__ == "__main__":
  main()