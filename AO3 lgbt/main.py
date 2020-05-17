from get_request import simple_get
from bs4 import BeautifulSoup
import xlsxwriter
import time


def find_between(r,first,last):
    try:
        start=r.index(first)+len(first)
        end = r.index(last,start)
        true_r=r[start:end]
        return true_r
    except ValueError:
        return
    
def count(url):
    try:
        raw_html=simple_get(url)
        html=BeautifulSoup(raw_html, 'html.parser')
        raw_count=html.find('h2')
        count=find_between(str(raw_count),'>','W')[3:-1]
        if(count.find('of')!=-1):
            count=count[11:]
        return count
    except ValueError:
        count=0
        return count
        

workbook = xlsxwriter.Workbook('raw_result.xlsx')
worksheet=workbook.add_worksheet()
row=2
column=2


url='https://archiveofourown.org/tags/LGBTQ%20Themes'
raw_html=simple_get(url)
html=BeautifulSoup(raw_html, 'html.parser')
sub_tags=html.find_all(attrs={"class":"sub listbox group"})
list=sub_tags[0].find_all(attrs={"class":"tags tree index"})


#Must begin from 1
for i in list[1:]:
    try:
        a=i.previous_sibling
        raw_tag_name=a.contents
        tag_name=str(raw_tag_name)[2:-2]
        print(tag_name)
        u=a.get('href')
        tag_url='https://archiveofourown.org'+u+'/works'
        tag_count=count(tag_url)   
        worksheet.write(row, column, tag_name)
        column=column+1
        worksheet.write(row, column, tag_count)
        row=row+1
        column=2
        time.sleep(3)
    except:
        break
    
workbook.close()

print("finish")