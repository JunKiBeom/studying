import time

def hanoi(n,frm,tmp,to):
    global cnt
    cnt+=1
    if(n==1):
        print("Disk 1, %c to %c"%(frm,to))
    else:
        hanoi(n-1,frm,to,tmp)
        print("Disk %d, %c to %c"%(n,frm,to))
        hanoi(n-1,tmp,frm,to)

while(1):
    n=int(input("Input Disk Number: "))
    if(n>1): break
    else: print("Input N>1")
start=time.time()
cnt=0
print("Print result\n")
hanoi(n,'A','B','C')
print("Cnt:",cnt)
print('time:',time.time()-start,'sec')