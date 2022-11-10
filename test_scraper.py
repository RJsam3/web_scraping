import requests
from bs4 import BeautifulSoup

webpage =  requests.get('')
prefix = ''
pages = []

page = BeautifulSoup(webpage.content, 'html.parser')
pages.append(page)

As = page.findAll('a')
links = []
#print(As)
for a in As:
    links.append(prefix+a['href'])


for link in links:
    webpage = requests.get(link)
    page = BeautifulSoup(webpage.content, 'html.parser')
    pages.append(page)
    if len(pages) > 5:
        pages.pop()

file_names = []
for i in range(len(links)):
    links[i] = links[i].replace('/', '_')
    links[i] = links[i].replace('.', '_')
    links[i] = links[i].replace('_aspx', '.html')
    links[i] = links[i].replace(':', '_')
    file_names.append(links[i])

print(file_names)
page_strings =  []
for page in pages:
    page_strings.append(str(page))
loopbreak =  False
for page_string in page_strings:
    if loopbreak == True:
         break
    for file_name in file_names:
        if file_names.index(file_name) > len(page_strings):
            loopbreak = True
            break
        else:
            with open(f'{file_name}','w') as file:
                file.write(page_string)


#print(pages)