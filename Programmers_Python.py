# 강의 주소 : https://school.programmers.co.kr/learn/courses/4008

#0. 수강 전에 이 문제를 풀어보세요.
'''
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

예시
input	                output
[[1], [2]]	            [1,1]
[[1, 2], [3, 4], [5]]	[2,2,1]
'''

# 내 코드
def solution(mylist):
    answer=[]
    for i in range(len(mylist)):
        answer.append(len(mylist[i]))
    # print(answer)
    return answer

# 추천 코드
def solution(mylist):
    return list(map(len,mylist))

#1. 몫과 나머지
'''문제 설명
숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

출력 설명
a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

제한 조건
a와 b는 자연수입니다.

입력 예
5 3
출력 예
1 2
'''

# 내 코드 : 연산자 이용
a, b = map(int, input().strip().split(' '))
print(a//b, a%b)

# 추천 코드 : divmod와 unpacking 이용
a, b = map(int, input().strip().split(' '))
print(*divmod(a, b))
'''
⨳ divmod를 사용할 때 주의할 점
무조건 divmod를 사용하는 게 좋은 방법은 아닙니다.
가독성이나, 팀의 코드 스타일에 따라서, a//b, a%b와 같이 쓸 때가 더 좋을 수도 있습니다.
또한, divmod는 작은 숫자를 다룰 때는 a//b, a%b 보다 느립니다. 대신, 큰 숫자를 다룰 때는 전자가 후자보다 더 빠르지요.
'''

#2. n진법으로 표기된 string을 10진법 숫자로 변환하기
'''
문제 설명
base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

출력 설명
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

제한 조건
base는 10 이하인 자연수입니다.
num은 3000 이하인 자연수입니다.

예시
input	output
12 3	5
444 5	124
'''

# 내 코드
num, base = map(int, input().strip().split(' '))
print(int(str(num), base))

# 타 언어 및 일반 코드
num, base = map(int, input().strip().split(' '))
num=str(num)

answer = 0
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base ** idx)
print(answer)

# 추천 코드 : int(x, base=10) 함수 사용
num, base = map(int, input().strip().split(' '))
print(int(str(num), base))

#3. 문자열 정렬하기
'''
문제 설명
문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

제한조건
s의 길이는 n보다 작습니다.
(n - s의 길이)는 짝수입니다.
s는 알파벳과 숫자로만 이루어져 있으며, 공백 문자가 포함되어있지 않습니다.

입력 예
abc 7
출력 예
abc      
   abc   
      abc
'''

# 내 코드
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

# 일반 코드
### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
print(answer)


# 추천 코드
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬