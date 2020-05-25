def max_sum(A, left, right):
    if left == right:
        return A[left]

    m = (left + right) // 2

    # 걸쳐져 있는 경우(왼쪽 최대구간 오른쪽 최대 구간 합)
    sum = 0
    i = m
    max_L = -10000000
    while (i >= left):
        sum += A[i]
        max_L = max(sum, max_L, A[i])
        # if max_L==A[i]:
        #     sum=A[i]
        #     max_L =sum
        i-=1

    sum1 = 0
    j = m + 1
    max_R = -10000000
    while (j <= right):
        sum1 += A[j]
        max_R = max(sum1, max_R, A[j])
        # if max_R==A[j]:
        #     sum=A[j]
        #     max_R=sum
        j+=1
    M = max_L + max_R

    # left에 최대구간
    R = max_sum(A, left, m)

    # right에 최대구간
    L = max_sum(A, m + 1, right)

    return max(M, max(R, L))


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A) - 1)
print(sol)

# -10 -7 5 -7 10 5 -2 17 -25 1