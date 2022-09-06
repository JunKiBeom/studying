# 강의 주소 : https://school.programmers.co.kr/learn/courses/4008

# Part1-1. 수강 전에 이 문제를 풀어보세요.
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


# Part2-1. 몫과 나머지
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


# Part2-2. n진법으로 표기된 string을 10진법 숫자로 변환하기
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


# Part3-1. 문자열 정렬하기
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

# 내 코드 & # 추천 코드
s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))   # 좌측 정렬
print(s.center(n))  # 가운데 정렬
print(s.rjust(n))   # 우측 정렬

# 일반 코드
### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s
print(answer)


# Part3-2. 알파벳 출력하기
'''
문제 설명

입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

예시1
입력        출력
0          abcd...(중간생갹)...xyz

예시2
입력        출력
1          ABCD...(중간생략)...XYZ
'''

# 내 코드
num = int(input().strip())
for i in range(0,26):
    if (num==0):
        A='a'
    else:
        A='A'
    print(chr(ord(A)+i), end="")

# 추천 코드 : string 모듈 사용
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters   # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits          # 숫자 0123456789


# Part4-1. 2차원 리스트 뒤집기
'''
문제 설명
다음을 만족하는 함수, solution을 완성해주세요.
solution 함수는 이차원 리스트, mylist를 인자로 받습니다
solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, 
solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

제한 조건
mylist의 원소의 길이는 모두 같습니다.
mylist의 길이는 mylist[0]의 길이와 같습니다.
각 리스트의 길이는 100 이하인 자연수입니다.
'''

# 내 코드
def solution(mylist):
    answer = [[] for _ in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i].append(mylist[j][i])
    return answer

# 추천 코드 : zip 사용
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))


# Part4-2. i번째 원소와 i+1번째 원소
'''
문제 설명
숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. 
solution 함수가 mylist의 i번째 원소와 i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.
단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.

제한 조건
mylist의 길이는 1 이상 100 이하인 자연수입니다.
mylist의 원소는 1 이상 100 이하인 자연수입니다.

예시
mylist	                    output
[83, 48, 13, 4, 71, 11]     [35, 35, 9, 67, 60]

설명:
83과 48의 차는 35입니다.
48과 13의 차는 35입니다.
13과 4의 차는 9입니다.
4와 71의 차는 67입니다.
71과 11의 차는 60입니다.
따라서 [35, 35, 9, 67, 60]를 리턴합니다.
'''

# 내 코드
def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i]-mylist[i+1]))
    return answer

# 추천 코드 : zip 이용
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer


# Part4-3. 모든 멤버의 type 변환하기
'''
문제 설명
문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.

제한조건
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.

예시
input	output
['1', '100', '33']	[1, 100, 33]
'''

# 내 코드 : list comprehension 사용 
def solution(mylist):
    return [int(i) for i in mylist]

# 일반 코드
list1 = ['1', '100', '33']
list2 = []
for value in list1:
    list2.append(int(value))

# 추천 코드 : map 이용
list1 = ['1', '100', '33']
list2 = list(map(int, list1))


# Part4-4. map 함수 응용하기
'''
문제 설명
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.
hint) 이전 강의에서 배운 map 함수를 활용해보세요

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

예시
input	                output
[[1], [2]]	            [1, 1]
[[1, 2], [3, 4], [5]]	[2, 2, 1]
'''

# 코드
def solution(mylist):
    answer = list(map(len, mylist))
    return answer


# Part5-1. sequence 멤버를 하나로 이어붙이기
'''
문제 설명
문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.

제한 조건
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소의 길이는 100 이하인 자연수입니다.
'''

# 내 코드 & 추천 코드
def solution(mylist):
    return ''.join(mylist)

# 일반 코드 : for 문을 이용해 원소를 하나씩 이어 붙이기
my_list = ['1', '100', '33']
answer = ''
for value in my_list:
    answer += value


# Part5-2. 삼각형 별찍기
'''
문제 설명
이 문제에는 표준 입력으로 정수 n이 주어집니다.
별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.

제한 조건
n은 100 이하인 자연수입니다.

예시
입력     출력
3       *
        **
        ***
'''

# 내 코드 & 추천 코드
n = int(input().strip())
for _ in range(1,n+1):
    print('*'*_)


# Part6-0. 곱집합(Cartesian product)구하기 - product
'''
예시) 두 스트링'ABCD', 'xy'의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.

보통 사람들은 for 문을 이용해 두 iterable의 원소를 하나씩 곱해갑니다.

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for value1 in iterable1:
    for value2 in iterable2:
        for value3 in iterable3:
            print(value1, value2, value3)

파이썬에서는
itertools.product를 이용하면, for 문을 사용하지 않고도 곱집합을 구할 수 있습니다.

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
'''


# Part6-1. 2차원 리스트를 1차원 리스트로 만들기
'''
문제 설명
문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

제한 조건
arr의 길이는 1 이상 100 이하인 자연수입니다.
arr 원소의 길이는 5를 넘지 않습니다.

예시
input	                            output
[[1], [2]]	                        [1, 2]
[['A', 'B'], ['X', 'Y'], ['1']]	    ['A', 'B', 'X' ,'Y', '1']
'''

# 내 코드 : sum함수 사용
def solution(mylist):
    return sum(mylist, [])

# 일반 코드 : 반복문을 이용해 붙이기
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for element in my_list:
    answer += element

# 추천 코드
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

#제한적으로 사용 가능한 방법 - 각 원소의 길이가 동일한 경우에만 사용 가능합니다.
# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()

'''
예를 들어 다음과 같은 리스트는 편평하게 만들 수 있고
[[1], [2]]
[[1, 2], [2, 3], [4, 5]]
다음과 같이 같이 각 원소의 길이가 다른 리스트는 편평하게 만들 수 없습니다.
[['A', 'B'], ['X', 'Y'], ['1']]
'''

# Part6-2. 순열과 조합
'''
문제 설명
숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.

제한 조건
mylist 의 길이는 1 이상 100 이하인 자연수입니다.

예시
mylist	    output
[2, 1]	    [[1, 2], [2, 1]]
[1, 2, 3]	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
'''

# 내 코드 & 추천 코드
from itertools import permutations

def solution(mylist):
    answer = list(permutations(mylist))
    answer.sort()
    return answer

# 일반 코드 : 보통 사람들은 for 문을 이용해 permutation 함수를 구현합니다.
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


# Part6-3. 가장 많이 등장하는 알파벳 찾기
'''
문제 설명
이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

제한 조건
mystr의 원소는 알파벳 소문자로만 주어집니다.
mystr의 길이는 1 이상 100 이하입니다.

예시
input	    output
'aab'	    'a'
'dfdefdgf'	'df'
'bbaa'	    'ab'
'''

# 내 코드 & 추천 코드 : collections.Counter 사용
import collections

my_str = input().strip()
dic = collections.Counter(my_str)
m = max(dic.values())
tmp = filter(lambda x:x[1]==m, dic.items())
print(''.join(sorted(key for key,value in tmp)))

# 일반 코드 : 반복문을 이용해 수를 셉니다.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError


# Part7-1. for 문과 if문을 한번에
'''
문제 설명
정수를 담은 리스트 mylist를 입력받아, 이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요. 예를 들어, [3, 2, 6, 7]이 주어진 경우
3은 홀수이므로 무시합니다.
2는 짝수이므로 제곱합니다.
6은 짝수이므로 제곱합니다.
7은 홀수이므로 무시합니다.
따라서 2의 제곱과 6의 제곱을 담은 리스트인 [4, 36]을 리턴해야합니다.

제한 조건
mylist는 길이가 100이하인 배열입니다.
mylist의 원소는 1이상 100 이하인 정수입니다.
'''

# 내 코드 : filter와 lambda 이용
def solution(mylist):
    answer = list(map(lambda x:x**2 ,list(filter(lambda x : x % 2 == 0, mylist))))
    #answer = [_**2 for _ in mylist if _ % 2 == 0] <- 아마 원하는 답은 이것
    return answer

# 일반 코드 : for 문 안에서 조건문을 사용해 2-depth 블록을 만듭니다.
mylist = [3, 2, 6, 7]
answer = []
for number in mylist:
    if number % 2 == 0:
        answer.append(number**2) # 들여쓰기를 두 번 함

# 추천 코드 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]


# Part7-2. flag OR else
'''
문제 설명
본 문제에서는 자연수 5개가 주어집니다.
숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
코드를 작성해주세요.

예시 1
입력    출력
2      found
4
2
5
1

설명
수를 곱해나가면 2, 8, 16, 80, 80 이 나옵니다. 
16은 4를 제곱해 나온 수이므로 이 수는 제곱수입니다. 따라서 found를 출력합니다.

예시 2
입력    출력
5      not found
1
2
3
1

설명
수를 곱해나가면 5, 5, 10, 30, 30 이 나옵니다. 이중 어떤 수도 제곱 수가 아니므로 not found를 출력합니다.
제곱수란 어떤 자연수를 제곱한 수입니다. 예를 들어 1, 4, 9, 16, 25, .. 등은 제곱수입니다. ↩
'''