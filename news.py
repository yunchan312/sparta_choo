from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98&oquer" \
      + "y=%EC%B6%94%EC%84%9D&tqi=U3lozsp0Yidssfgl85lssssssM4-211996"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.section._prs_nws_all > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')

    ws1.append([title, url, company])
    print(title, url, company)




driver.quit()
wb.save(filename='articles.xlsx')