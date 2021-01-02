# 일반적인 재귀 함수
def factorial(n):
    if n==1: return n
    else: return n * factorial(n-1)

a=factorial(4)
print(a)
''' 
factorial(4) = 4 * factorial(3)
             = 4 * (3 * factorial(2))
             = 4 * (3 * (2 * factorial(1)))
             = 4 * (3 * (2 * 1))
             = 4 * (3 * 2)
             = 4 * 6
             = 24
'''
# factorial 재귀 함수는  factorial(n)-> ... -> factorial(1) 로 재귀 호출 된 후,
# factorial(1)이 계산이 된 후에 return 되면서 전체 계산이 완성 된다.
# 즉, 바닥 경우에 도달 할 때까지 재귀 호출이 계속하게 된다.

# Tail Recursion 방식
def factorial2(n, value = 1):
    if n==1: return value
    else: return factorial2(n-1, value*n)

b=factorial2(4)
print(b)
'''
factorial2(4)
factorial2(3, 1*4)  # value = 1
factorial2(2, 4*3)  # value = 4
factorial2(1, 12*2) # value = 12
factorial2(1)       # value = 24, return value
24 -> 24 -> 24 -> 24 # return four times with a same 24
'''

# 재귀 함수의 매개변수로 현재의 중간 계산된 factorial 값을 직접 전달해주기 때문에
# 바닥 경우인 n=1인 경우에 이미 최종 값 24가 계산되었고, 이후엔 그 값을 return만 해서 전달 됨.
# 이 성질을 이용하면 하나의 recursion stack의 내용을 overwrite하는 식으로 메로리 사용을 크게 줄일 수 있음
# TRO (Tail Recursion Optimization) 언어에 따라 지원 여부가 결정 된다.