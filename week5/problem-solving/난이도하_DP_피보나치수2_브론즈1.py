# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys

def main():
  # input
  n = int(sys.stdin.readline())

  # 피보나치 수열의 n번째 값을 출력해야 하고 n <= 90
  # 90까지는 배열에 저장이 되어 있어야 바로 출력이 되겠지?
  # 배열 안 쓰고 풀 수 있지 않나? 같은 바보같은 생각이 드는데, 그러면 전전값이랑 전값 어떻게 찾아올건데?

  # 배열 생성
  dp = [0] * 91
  dp[1] = 1

  for i in range(2, 91):
    dp[i] = dp[i-1] + dp[i-2]
  
  print(dp[n])

if __name__ == "__main__":
  main()