W = int(input())
words = input().split()
# code below
empty = 0  # 왼쪽맞춤 카운트(W전까지)
cnt = 0  # 12까지 카운트
p = []  # 왼쪽맞춤 값 저장
sum=0
#print(words)

#for i in range(0, len(words)):
#    print(len(words[i]), end=' ')


i=0
while (i < len(words)):
    if len(words[i]) < (W-cnt): #단어길이가 남은 cnt보다 작으면
        cnt += len(words[i])
        if i== (len(words)-1): # 근데 얘가 마지막 단어면
            if cnt==W: #근데 마지막 단어이면서 cnt==W라면
                empty=0
                p.append(empty)
                break
            else: # 마지막 단어이긴 한데 cnt가 아직 부족하다면
                empty += (W-cnt)
                p.append(empty)
                break
        else: # 마지막 단어가 아니면
            cnt+=1
            i+=1
            if cnt==W: # cnt를 W만큼 다 채웠다면
                empty+=1
                p.append(empty)
                cnt,empty=0,0

    elif len(words[i]) == (W-cnt):
        if i==(len(words)-1):
            empty=0
            p.append(empty)
            break
        else:
            empty=0
            cnt=0
            p.append(empty)
            cnt,empty=0,0
            i+=1
    else:
        empty=(W-cnt)+1
        cnt+=(W-cnt)
        p.append(empty)
        cnt,empty=0,0

# print(p)
for i in range(len(p)):
    sum+=(p[i])**3

print(sum)