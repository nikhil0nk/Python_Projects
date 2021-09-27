import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


"""
print(soup.prettify())	# to print html in tree structure

for i in soup.find_all("code"):
    print(i.text)
    # We can also do it like this
    # print(i.get_text())

title = soup.title
print(title)

print(soup.find('p')) #first para
print(soup.find('p')[class]) #class of first para

paras = soup.find_all('p') #all paras
print(type(paras))
for i in paras:
    print(i['href'])
#or
for i in paras:
    print(i.get('href'))

print(soup.find_all("p", class_="lead"))
print(soup.find_all(class_="code-toolbar"))
print(soup.find(id='qna')) # no find_all() function since id can be given to only one element

soup.find(‘element’).text # or soup.find(‘element’).get_text()

anchors = soup.find_all('a')
links = set()
for link in anchors:
  if link.get('href') != '#':
    links.add(link.get('href'))

print(links)

ul = soup.find("ul")
print(ul.contents)
#or
ul = soup.find("ul")
for i in ul.children:
	print(i)

ul = soup.find("ul")
print(ul.parent)
print(ul.parent.parent)

ul = soup.find(id="li")
print(ul.next_sibling.next_sibling)
for j in ul.next_siblings:
    print(j)
for i in ul.previous_siblings:
    print(i)

print(ul.previous_sibling.previous_sibling)

ul = soup.find(id="li")
elem = ul.next_sibling.next_sibling
print(elem)
for i in elem.stripped_strings:
    print(i)


"""
