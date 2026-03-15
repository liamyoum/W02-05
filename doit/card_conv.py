# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하는 함수

def card_conv(x: int, r: int) -> str:
  """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

  d = [] # 변환 후 문자열
  dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  while x > 0:
    d += dchar[x % r]
    x //= r
  
  return "".join(reversed(d))

print(card_conv(59, 16))