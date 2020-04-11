def find_median_five(L):
    l = len(L)  # 배열 길이
    if (l==0): return None
    median = int(l / 2)
    if (l % 2 == 1):
        return L[median]
    else:
        return int((L[median - 1] + L[median]) / 2)


def MoM(L, k):  # L의 값 중에서 k번째로 작은 수 리턴
    if len(L) == 1:  # no more recursion
        return L[0]
    i = 0
    A, B, M, medians = [], [], [], []
    while i + 4 < len(L):
        medians.append(find_median_five(L[i: i + 5]))
        i+=5

    if i < len(L) and i + 4 >= len(L):
        medians.append(find_median_five(L[i:]))

    mom = MoM(medians, len(medians) // 2)
    for v in L:
        if v < mom:
            A.append(v)
        elif v > mom:
            B.append(v)
        else:
            M.append(v)
            

    if len(A) >= k:
        return MoM(A, k)
    elif (len(A) + len(M))< k:
        return MoM(B, k - len(A) - len(M))
    else:
        return mom


# n과 k를 입력의 첫 줄에서 읽어들인다
n, k = [int(i) for i in input().split()]
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
L = [int(i) for i in input().split()]
print(MoM(L, k))
