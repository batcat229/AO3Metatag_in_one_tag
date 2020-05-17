from get_request import simple_get
from bs4 import BeautifulSoup

url='https://archiveofourown.org/tags/Genderfluid%20Sh%C4%AB%20Q%C4%ABngxu%C3%A1n/works'
raw_html=simple_get(url)
html=BeautifulSoup(raw_html, 'html.parser')
count=html.find('h2')
print(count)