def print_IS(seq, x):
    for i in range(len(seq)):
        if x[i]:
            print(seq[i], end="")
        else:
            print("_", end="")
    print()

def LIS_DP(seq):
    x = [0] * len(seq)
    DP = [1] * (len(seq))
    # code here
    for i in range(len(seq)):
        x[i]=seq[i]

    for i in range(0,len(seq)):
        for j in range(0,i):
            if x[i] > x[j]:
                DP[i] = max(DP[i],DP[j]+1)

    return max(DP), x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)

# abcabc
# abbcbbdbbe
# edabc