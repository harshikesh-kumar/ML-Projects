import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("http://www.codeheroku.com/blog.html")
print(page)
contents = page.content

#print(contents)
soup = BeautifulSoup(contents,'html.parser')#or lxml.parser

#print(soup)
#print(soup.head)
#print(soup.body)

data = []
blog = {}

section = soup.find('section', attrs={'class':'card-group-2'})
#print(section)

all_cards = section.find_all('div', attrs={'class':'card'})

for card in all_cards:
    blog = {}
    title = card.find('h2',class_='card-title')
    title = title.text.strip()
    blog['title']= title
    blog['date_posted'] = card.select('.card-date')[0].text.strip()
    #print(blog)
    
    data.append(blog)

print(data)
'''
csv_columns = ['title','date_posted']
#print(data)
with open ('webcsv1.csv','w') as file:
    writer = csv.DictWriter(file,fieldnames=csv_columns)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

    file.close()
'''

'''
f = open('webcsv','wb')
csv_writer = csv.writer(f)
for i in data:
    csv_writer.writerow(i)

f.close()
'''

#for i in data:
df = pd.DataFrame(data)

#print(df)

df.to_csv('webcsv2.csv')

#print(data[0])


