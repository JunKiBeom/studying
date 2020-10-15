def max2(A):

    if len(A) == 1: return A[0]
    else:
        m=max2(A[1:])
        return m if m>A[0] else A[0]

# n개의 정수를 읽어 A에 저장
A=[int(i) for i in input().split()]
print(max2(A))