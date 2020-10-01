
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3+%EC%8"
           + "A%AC%EA%B8%B0")

time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')


thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'img/{i}.jpg')
    i += 1

driver.quit()
