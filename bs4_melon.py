from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import csv

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver: WebDriver = webdriver.Chrome('./chromedriver',chrome_options=options)
# driver.implicitly_wait(2)
link=input()
driver.get(link)
# driver.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=476017614')

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
# req = requests.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=476017614', headers = header) ## 주간 차트를 크롤링 할 것임
html = driver.page_source
parse = BeautifulSoup(html, 'html.parser')
# print(parse)

parse_titles = parse.find_all("a", {"class": "fc_gray"})        # 제목
parse_singers = parse.find_all("div", {"id": "artistName"})     # 가수
parse_albums = parse.find_all("a", {"class": "fc_mgray"})       # 앨범

# print(parse_albums)
title=[]    # 제목
singer=[]   # 가수
album=[]    # 앨범

acnt=0      # 앨범 이름 저장용

for t in parse_titles:
    title.append(t.text)

for s in parse_singers:
    singer.append(s.find('a', {"class": "fc_mgray"}).text)

for a in parse_albums:
    acnt+=1
    if acnt%2==0:   # div.ellipsis > a.fc_mgray가 가수와 앨범이 동일, 앨범만 나오도록 처리
        album.append(a.text)

# print("T",title)
# print("S",singer)
# print("A",album)

csvfile = open("./csv/Melon_My_Playlist.csv", "w", encoding='UTF-8')    # 한글 인코딩 깨질경우 CP494로 바꿀 것
csvwriter = csv.writer(csvfile)

for i in range(len(title)):
    print('%3d번: %s [%s] - %s' % (i + 1, title[i], album[i], singer[i]))    # 곡, 가수, 앨범 순으로 저장
    csvwriter.writerow([title[i], singer[i], album[i]])

csvfile.close()
driver.close()