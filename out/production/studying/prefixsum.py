import time, random

def prefixSum1(X, n):
    global p1_start,p1_end
    p1_start=time.time()
    S=[0]*n
    for i in range (n):
        S[i]=0
        for j in range(i+1):
            S[i]+=X[j]
    # print(S)  #확인
    p1_end=time.time()

# code for prefixSum1

def prefixSum2(X, n):
    global p2_start, p2_end
    p2_start=time.time()
    S=[0]*n
    S[0]=X[0]
    for i in range(n):
        S[i]=S[i-1]+X[i]
    # print(S)  #확인
    p2_end=time.time()

# code for prefixSum2

random.seed()   # random 함수 초기화
# n 입력받음
n=int(input())
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X=[]
for i in range (n):
    X.append(random.randint(-999,999))  # -999 ~ 999의 범위에서 n개의 수를 랜덤 생성, X에 추가
# print(X)  # 출력 확인
# prefixSum1 호출
prefixSum1(X,n)
# prefixSum2 호출
prefixSum2(X,n)
# 두 함수의 수행시간 출력
print("Prefixsum1 : %f"%(p1_end-p1_start))  # 소수점 6자리까지 출
print("Prefixsum2 : %f"%(p2_end-p2_start))
print("Prefixsum1 :",(p1_end-p1_start))  # 그대로 출력
print("Prefixsum2 :",(p2_end-p2_start))