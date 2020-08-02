import requests
from bs4 import BeautifulSoup

# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

count = 0

for music in music:
    a_tag = music.select_one('td.info > a.title.ellipsis')

    if a_tag is not None:
        count = count+1
        title = a_tag
        artist = music.select_one('td.info > a.artist.ellipsis')
        print(count,a_tag.text.lstrip(),artist.text)

        # doc = {
        #     'count': count,
        #     'title': title,
        #     'artist': artist
        # }
        # db.music.insert_one(doc)
