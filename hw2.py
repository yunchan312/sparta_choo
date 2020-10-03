from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "hw_articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])
ws1.append([' ', ' ', ' ', ' '])

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EA%B0%95%EC%95%84%EC%A7%80"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.section._prs_nws_all > ul > li')
for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    comp = article.select_one('dl > dd > span').text
    thumb = article.select_one('img')['src']
    print(title, url, comp, thumb)

    ws1.append([title, url, comp, thumb])


wb.save(filename='articles.xlsx')
driver.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "yunchan0339@gmail.com"
my_password = "itsmykorea1100!!"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "phenomenal312@naver.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "잘하고 있니.."
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "과거의 내가 현재의 너에게..."
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 파일 첨부하기
part = MIMEBase('application', "octet-stream")
with open('articles.xlsx', 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="articles.xlsx")
msg.attach(part)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()