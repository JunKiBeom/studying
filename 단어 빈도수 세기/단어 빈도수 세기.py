# 실습 14-2: 단어 빈도수 세기
print('*** 단어 빈도수 세기 ***')


# 텍스트 파일 fname 읽기 함수
def readTextFile(fname):
    txt = ''
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        txt += line
        line = f.readline()
    f.close()
    return txt


# 텍스트 파일 읽기
fname = input('파일 이름? ')
text = readTextFile(fname)

# 단어 빈도수 세기
word_dic = {}
word_str = ''

t = text.lower()+'\n'
# print(t)
for i in range(len(t)):

    if (not('A' <= t[i] <= 'Z' or 'a' <= t[i] <= 'z')):

        if word_str in word_dic:
            word_dic[word_str] += 1
            w_str = ''
            word_str = ''

        if (word_str==''):
            continue
        word_dic[word_str] = 1
        w_str = ''
        word_str = ''

    else:
        w_str = t[i]
        word_str += w_str

print(word_dic)