import random, timeit


def quick_sort(A, first, last):
    if first >= last: return
    global Qc, Qs
    left, right = first + 1, last
    pivot = A[first]

    while left <= right:
        Qc += 1
        while left <= last and A[left] < pivot:
            left += 1
            Qc += 2

        while right > first and A[right] > pivot:
            right -= 1
            Qc += 2

        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            Qs += 3

    A[first], A[right] = A[right], A[first]
    Qs += 3

    quick_sort(A, first, right - 1)
    quick_sort(A, right + 1, last)


def merge_sort(A, first, last):
    if first >= last: return
    global Mc, Ms
    m = (first + last) // 2
    merge_sort(A, first, m)
    merge_sort(A, m + 1, last)
    i, j = first, m + 1
    B = []

    while i <= m and j <= last:
        Mc += 2
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
            Mc += 1
        else:
            B.append(A[j])
            j += 1
            Mc += 1

    for k in range(i, m + 1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])
    for i in range(first, last + 1):
        A[i] = B[i - first]
        Ms += 1


def heap_sort(A):
    global Hc,Hs
    n = len(A)
    for k in range(n - 1, -1, -1):
        heapify_down(A,k,n)

    n = len(A)
    for k in range(n - 1, -1, -1):
        A[0], A[k] = A[k], A[0]
        Hs+=2
        n = n - 1
        heapify_down(A,0,n)

def heapify_down(A,s,n):
    global Hc, Hs
    while 2 * s + 1 < n:
        L = 2 * s + 1
        R = 2 * s + 2
        if L < n and A[L] > A[s]:
            m = L
            Hc += 1
        else:
            m = s
            Hc += 1
        if R < n and A[m] < A[R]:
            m = R
            Hc += 1
        if m != s:
            A[s], A[m] = A[m], A[s]
            s = m
            Hc += 1
            Hs += 2
        else:
            break


## 여기에 세 가지 정렬함수를 위한 코드를...
##


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]: return False
    return True


#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
print(A)
assert (check_sorted(B))
print(B)
print(C)
assert (check_sorted(C))
