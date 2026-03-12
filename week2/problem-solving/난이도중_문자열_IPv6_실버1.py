# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

"""
문제
IPv6은 길이가 128비트인 차세대 인터넷 프로토콜이다.
IPv6의 주소는 32자리의 16진수를 4자리씩 끊어 나타낸다. 이때, 각 그룹은 콜론 (:)으로 구분해서 나타낸다.
예를 들면, 다음과 같다.
2001:0db8:85a3:0000:0000:8a2e:0370:7334

32자리의 16진수는 사람이 읽고 쓰기에 불편하고, 대부분의 자리가 0이기 때문에 아래와 같이 축약할 수 있다.
    1. 각 그룹의 앞자리의 0의 전체 또는 일부를 생략 할 수 있다. 위의 IPv6을 축약하면, 다음과 같다
    2001:db8:85a3:0:00:8a2e:370:7334

    2. 만약 0으로만 이루어져 있는 그룹이 있을 경우 그 중 한 개 이상 연속된 그룹을 하나 골라 콜론 2개(::)로 바꿀 수 있다.
    2001:db8:85a3::8a2e:370:7334

2번째 규칙은 모호함을 방지하기 위해서 오직 한 번만 사용할 수 있다.
올바른 축약형 IPv6주소가 주어졌을 때, 이를 원래 IPv6 (32자리의 16진수)로 복원하는 프로그램을 작성하시오.
"""

"""
입력
첫째 줄에 올바른 IPv6 주소가 주어진다. 이 주소는 최대 39글자이다. 또한, 주소는 숫자 0-9, 알파벳 소문자 a-f, 콜론 :으로만 이루어져 있다.
"""

"""
출력
첫째 줄에, 입력으로 주어진 IPv6의 축약되지 않은 형태를 출력한다.
"""

# 일단은 :로 구분해서 다 리스트에 넣자!

# 0으로만 이루어진 그룹이 없는 경우 -> 일단 받아서 콜론으로 구분해서 리스트에 넣기 -> 리스트 길이가 8이면 0으로만 이루어진 그룹 없어서 처리 쉬움

# 문제는 0으로만 이루어진 그룹일 때.... 문자열에 공백이 있으면 0으로만 이루어진 그룹임.
# ::도 리스트에 넣어버려서 예를 들어서 3::1 일때 -> ['3', '', '1'] 이렇게 하고, 리스트 개수 세어서 8 - len(list) + 1 개를 복사해서 삽입할 수 없나? -> insert(인덱스, 값)
# EX ['3', '::', '::', '::', '::', '::', '::', '1'] 그러고 문자열 돌면서 regex 써서 앞에 0 채우고, if i == '::' 이면 0000으로 대입

import sys
input = sys.stdin.readline

def main():
  address = input().strip()

  # 1. '::' 있을 때 (0 그룹 있을 때)
  if '::' in address:
    # 1:2:3:4:5:6:7:: -> ['1:2:3:4:5:6:7', '']
    parts = address.split('::')
    # 앞부분과 뒷부분 나누기
    left = parts[0].split(':') if parts[0] else []
    right = parts[1].split(':') if parts[1] else []

    # 2. 0 그룹 개수 계산
    group_0_cnt = 8 - len(left) - len(right)
    group_0 = ['0000'] * group_0_cnt

    full_address = left + group_0 + right
  # :: 없을 때
  else:
    full_address = address.split(':')
  
  result = [group.zfill(4) for group in full_address]

  print(':'.join(result))  

if __name__ == "__main__":
  main()

"""
처음 했던 접근 및 코드

address = input()[:-1].split(':')
  # len(address) == 8: 0그룹 없는 경우
  if len(address) == 8:
    for idx, group in enumerate(address):
      if len(group) != 4:
        address[idx] = group.zfill(4)
    print(':'.join(address))
  # len(address) != 8: 0그룹 있는 경우 (그룹이 공백으로 저장됨)
  else:
    while len(address) != 8:
      space_idx = address.index('')
      address.insert(space_idx, '')
    for idx, group in enumerate(address):
      if len(group) != 4:
        address[idx] = group.zfill(4)
    print(':'.join(address))
      # 공백을 공백 있는 인덱스 자리에 계속 삽입
"""