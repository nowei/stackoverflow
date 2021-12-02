from bs4 import BeautifulSoup
from requests_html import HTMLSession 

session = HTMLSession()
url = "https://twitter.com/aProfile/"
page = session.get(url)
print(page.html)
page.html.render(sleep=5)
print(page.html.search('Agregator Profile'))
# html = BeautifulSoup(page.text, "html.parser")
# print(html)
# titles = html.find_all('title')
# print(titles[0].text) 
# session = HTMLSession()
# r = session.get('https://pythonclock.org')
# r.html.render()
# print(r.html.search('Python 2.7 will retire in...{}Enable Guido Mode')[0])
