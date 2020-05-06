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
# driver.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=475875948')

# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
# req = requests.get('https://www.melon.com/mymusic/playlist/mymusicplaylistview_inform.htm?plylstSeq=476017614', headers = header) ## 주간 차트를 크롤링 할 것임
html = driver.page_source
parse = BeautifulSoup(html, 'html.parser')
# print(parse)

parse_titles = parse.find_all("div", {"class": "ellipsis rank01"})
parse_singers = parse.find_all("div", {"class": "ellipsis rank02"})
parse_albums = parse.find_all("div", {"class": "ellipsis rank03"})

# print(parse_albums)
title=[]
singer=[]
album=[]

for t in parse_titles:
    title.append(t.find('a').text)

for s in parse_singers:
    singer.append(s.find('span', {"class": "checkEllipsis"}).text)

for a in parse_albums:
        album.append(a.find('a').text)

# print("T",title)
# print("S",singer)
# print("A",album)

csvfile = open("./csv/Melon_DJ_Playlist.csv", "w", encoding='UTF-8')
csvwriter = csv.writer(csvfile)

for i in range(len(title)):
    print('%3d번: %s [%s] - %s' % (i + 1, title[i], album[i], singer[i]))
    csvwriter.writerow([title[i], singer[i], album[i]])

csvfile.close()
driver.close()