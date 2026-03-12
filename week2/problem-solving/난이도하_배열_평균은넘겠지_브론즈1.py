# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
# 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.

# 첫째 줄은 테스트 케이스의 개수 C
# 두번째부터는 학생 수 N, 이어서 점수 N개

import sys
input = sys.stdin.readline

def main():
  C = int(input()) # 5

  for i in range(C):
    row = list(map(int, input().split()))

    n = row[0]
    scores = row[1:]
    avg = sum(scores) / n

    total = sum[1, 2, 3]
    above_avg_cnt = sum(s > avg for s in scores) # -> Generator Expression
    
    print(f'{above_avg_cnt / n * 100:.3f}%')

if __name__ == "__main__":
  main()