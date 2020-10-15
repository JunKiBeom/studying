def max2(A, left, right):
    if len(A)==1 : return A[0]
    if A[left]>=A[right]:
        del A[right]
    elif A[left]<=A[right]:
        del A[left]
    return max2(A,0,len(A)-1)

# n개의 정수를 읽어 A에 저장
A=[int(i) for i in input().split()]
print(max2(A, 0, len(A) - 1))