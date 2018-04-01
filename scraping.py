"""
created Fri Mar 30, 2018
@author: jessicazhou

"""

import urllib.request
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer 
import nltk
from nltk.collocations import *
import io

"""
current organization

FOLDER: [GITHUB PROJECT NAME]
    TXT: [HOME PAGE]
    FOLDER: WIKI TABS
        TXT: [TAB NAME]
        TXT: [TAB NAME]
        TXT: [TAB NAME]
        TXT: [TAB NAME]
        ETC
"""

#link of the wiki with input
wiki = "https://github.com/jekyll/jekyll/wiki"

#create BeautifulSoup object of html of entirety of webpage
response = urllib.request.urlopen(wiki)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page)

#print object to console (for testing/immediate purposes)
print(soup.get_text())
            
#print (soup.prettify())
#print (soup.title.string)

#TODO create a folder titled with name of Github Project




#create a txt file of this name + write object to the file
f = open('helloworld.txt','w')
#f.write('hello world')
f.write(soup.prettify())

#loop through all the links/subpage in the wiki navigation
#create text file for each subpage
links = soup.findAll('a',attrs={'class':'wiki-page-link'})
for a in links:
    print (a['href'])
    #haha = open('helloworld.txt','w')
    #1f.write(a['href'])
    url = wiki + a['href']
    with io.open("tab_" + a.string + ".txt", 'w', encoding='utf-8') as f:
        response = urllib.request.urlopen(url)
        the_page = response.read()
        response.close
        soup = BeautifulSoup(the_page)
        f.write(soup.prettify())


#f.write(soup.title.string) Home · jekyll/jekyll Wiki · GitHub
f.close()



