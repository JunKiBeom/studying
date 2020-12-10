'''
함수를 다른 변수에 항당 가능 하며
함수가 할당된 변수는 동일한 함수처럼 활용이 가능하다.
'''

def calc_square(digit):
    return digit**2 # digit * digit

def calc_plus(digit):
    return digit*2 # digit + digit

def calc_quad(digit):
    return digit**4 # digit * digit * digit * digit

def list_square(function, digit_list):
    result = list()
    for digit in digit_list:
        result.append(function(digit))
    print (result)

num_list = [1,2,3,4,5]

list_square(calc_square, num_list)
list_square(calc_plus, num_list)
list_square(calc_quad,num_list)
print()
# 이와 같이 함수를 다른 함수에 인자로 넣을 수도 있다.

def logger(msg):
    message = msg
    def msg_creator():
        print('[HIGH LEVEL]: ',message)
    return msg_creator

log1 = logger('Fisrt')
log1()
print()

def html_creator(tag):
    def text_wrapper(msg):
        print('<{0}> {1} <{0}>'.format(tag,msg))
    return text_wrapper

h1_html_creator = html_creator('h1')
h1_html_creator("h1 태그는 타이틀을 표시하는 태그")

p_html_creator = html_creator('p')
p_html_creator("p태그는 문단을 표시하는 태그")
# 함수의 결과값으로 함수를 리턴할 수도 있다.