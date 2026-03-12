# Function Call Evaluation Strategy: 함수 호출에서의 평가 전략
# 함수에 전달된 인자를 "언제" 계산하느냐

# 1) Applicative Order Evaluation (적용 순서 평가)
# 함수 호출 시 argument(인자)를 먼저 계산 후 함수에 전달
# 즉, 인자 먼저 계산하고 그 인자로 함수를 실행
# 대부분의 프로그래밍 언어가 이 방식 사용(C, Java, Python, JS, etc.)

# 2) Normal Order Evaluation (정상 순서 평가)
# 함수를 먼저 실행하면서 필요할 때 인자를 가져와서 계산

# Sum Iteration Version

def nsum(n):
  sum = 0
  for i in range(n + 1):
    sum += i

  return sum

def nsum2(n):
  return sum([i for i in range(n + 1)])

def nsum3(n):
  return sum(list(range(n + 1)))

# 위 세 함수는 내부적으로는 모두 동일하게 작동함. keyword: iterator

# =================================

# Recursive version 1

def nsum_r(n):
  # Base Case
  if n == 0:
    return 0
  return n + nsum_r(n - 1) # -> + n 이라는 추가 연산있으므로 Tail Recursion은 아님

# =================================

# Sum - Tail Recursion - 특정 언어는 이걸 쓰면 for문으로 바꿔주는 등, 이 방법을 쓰라고 하기도 함. 파이썬은 이거 쓰지 말고 for문 쓰도록 강조?
# Tail Recursion(꼬리 재귀)의 핵심: 재귀 호출이 함수의 "Last Operation"이어야 한다. 재귀 호출 결과에 대해 추가 계산 X
# factorial의 경우 TR이 아님. factorial(4) = 4 * factorial(3) = 4 * (3 * factorial(2)) ... 이니까.
# 그래서 그냥 Recursion을 Tail Recursion으로 바꾸면 기존에 나중에 해야할 계산을 미리 인자로 전달해주어야 함.
# 아래에선 total
# 그렇기 때문에 인자가 늘어나는 것
# 그냥 재귀에서 스택 구조만 변경한 것, 일반 재귀: 호출 깊이만큼 스택 필요, TR + Tail Call Optimization: 스택 안 늘리고 실행 가능
# 그래서 사실 재귀처럼 보이지만 본질적으로는 iterative process. 파이썬에서는 TCO 지원 안해서 반복문이 나음
# 일반 재귀: 내려가면서 할 일을 쌓고, 올라오면서 계산 / TR: 내려가면서 계산을 끝내고, 상태만 넘긴다
# 일반 재귀: base case는 계산을 시작하는 지점 / TR: base case는 이미 계산된 결과를 맨 위까지 반환하는 지점
def sum_iter(n, total):
  if n == 0:
    return total
  else:
    return sum_iter(n-1, total + n) # -> 꼬리에 달려있는데 추가 연산 없이 순수하게 자기만 호출하는 Tail Recursion
  
def nsum_tr(n):
  return sum_iter(n, 0)

# =================================

# Exponential을 recursion으로 구현!
def expt(b, n):
  # base case
  if n == 0:
    return 1
  else:
    return b * expt(b, n-1)

# Tail Recursion Exponential
def expt_tr(b, exponent, product = 1):
  if exponent == 0:
    return product
  else:
    return expt_tr(b, exponent - 1, b * product)
  
# Iteration version
def expt_iter(b, n):
  result = 1
  
  for _ in range(n):
    result *= b
  return result

# =================================

# 위까지는 다 time complexity = O(n) 인데, 바로 아래의 함수는 O(log n)으로 더 효율적.
# 홀수든 짝수든 짝수 되는 순간 함수 호출하는, 즉 재귀의 깊이가 exponential decreasing
def fast_expt(b, n):
  # 짝수
  if n == 0:
    return 1
  else:
    if n % 2 == 0:
      return fast_expt(b, n//2) ** 2
  # 홀수
    else:
      return b * fast_expt(b, n-1)
    
# =================================

# 피보나치 수열의 인덱스 n번째 숫자를 가져오는 함수 O(2^n) 
# Tree Recursion
def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)
  
# Fibonacci - Tail Recursion(Iterative Process) O(n)
# 중복 계산 없음 (memoization 기법도 가능)
def fib2(n):
  def fib_iter(a, b, cnt):
    if cnt == 0:
      return a
    else:
      return fib_iter(b, a+b, cnt - 1)
  return fib_iter(0, 1, n)

# Fibonacci - Iteration
def fib_iter(n):
  a, b = 0 ,1
  for _ in range(n):
    a, b = b, a+b
    return a
  
# =================================

# Counting change problem
# Problem: 주어진 금액을, 사용 가능한 동전 단위를 이용해 얼마나 많은 방법으로 거슬러 줄 수 있는가?
# EX) 금액 4, 동전 종류 [1, 2, 3] -> 가능한 경우의 수 4가지 (1+1+1+1) (1+1+2) (1+3) (2+2)
# 알고리즘:
#   1. 주어진 금액(4)에 대해서 첫번째 동전(1)를 제외하고 거슬러줄 수 있는 경우의 수 -> 주어진 금액: 4, 사용가능한 동전: [2,3] -> coins[1:]
#   2. 주어진 금액(4)에 대해서 첫번째 동전(1)를 사용하고 거슬러줄 수 있는 경우의 수 -> 주어진 금액: (4-1) = 3, 사용 가능한 동전: [1,2,3]
#   3. 위 1과 2의 합

# Base case 찾기 -> Smaller problem으로 쪼갤 방법 찾기 -> 결과를 어떻게 합칠지 고민
# 이거 Backtracking이랑은 다른거임. 실행 흐름 자체는 DFS가 맞는데, 아이디어 자체가 다름.
# 백트래킹은 포인터 하나로 갔다가 실패하면 이전 단계로 돌리는거고, 밑에 문제는 큰 문제를 작은 문제들로 잘게 쪼개는거(베이스 케이스까지)
# 목적 자체가 그래프 방문이 아니라, 경우의 수 계산하는거니까 다름

# 시간 복잡도는 O(2^n), 더 줄이고 싶으면 꼬리 재귀 혹은 Memoization 사용
def count_change(amount, coins):
  # Base case
  if amount == 0: # 주어진 금액이 0이면 거스름돈 방법은 1가지
    return 1
  if amount < 0 or len(coins) == 0: # 주어진 금액이 음수고 줄 수 있는 코인이 없을 때
    return 0
  
  return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)

print(count_change(4, [1, 2, 3]))



# Hanoi Tower (대표적 Recursion)

# =============================================================================

print(nsum(10))
print(nsum_r(10))
print(nsum_tr(5))
print(expt(2, 3))
print(expt_iter(2, 3))
print(fast_expt(2, 3))
print(fib(3))