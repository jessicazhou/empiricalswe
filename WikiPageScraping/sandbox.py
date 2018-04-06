import requests
import os
import sys
import urllib.request
from bs4 import BeautifulSoup

line = "https://github.com/jessicazhou/empiricalswe/wiki"

"""3
response = urllib.request.urlopen(line)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page)
"""

pls=requests.get(line, allow_redirects=False)

print(pls)

if(str(pls) == '<Response [302]>') :
    print('hi')

#links = soup.findAll('a',attrs={'class':'wiki-page-link'})


# soup.find_all("p", "title")
# <p class="title"><b>The Dormouse's story</b></p>

#<a class="btn btn-sm btn-primary" href=/hessicazhou/empiricalswe/wiki/_new" 


"""3
link = soup.find_all("div",class_="has-rightbar")
print(link)
print(len(link))


link = soup.find_all("div", {"class": "btn btn-sm btn-primary"})
print(link) #this is an empty set
"""

#<div class="has-rightbar">


"""
for a in links:
    print (a['href'])
    print(a[])

""
    
print(a)

#pls = soup.findAll('a',attrs={'class':'btn btn-sm btn-primary'})
#print(pls)
"""


#uh = soup.find(text="Wikis provide a place in your repository to lay out the roadmap of your project,")
#print("hahahaha"+uh.contents)

#hm = soup.findAll('a',attrs={'class':'btn btn-sm btn-primary'})
#print(hm)

"""
##if len(soup.findAll('a',attrs={'class':'btn btn-sm btn-primary'})) > 0:

btn btn-sm btn-primary    
    print("ya!")
links = soup.findAll('a',attrs={'class':'wiki-page-link'})
"""

"""
if not uh:
    print("real! content in wiki")
else:
    print("issa default message")

    """