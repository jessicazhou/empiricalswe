"""
created Fri Mar 30, 2018
@author: jessicazhou

"""

import urllib.request
from bs4 import BeautifulSoup
import io
import os
import string

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
#TODO, pass in github urls in autoscraper.py
wiki = "https://github.com/jekyll/jekyll/wiki"

#create BeautifulSoup object of html of entirety of webpage
response = urllib.request.urlopen(wiki)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page)

#print object to console (for testing/immediate purposes)
#print(soup.get_text())
            
#print (soup.prettify())
#print (soup.title.string)

#create a folder titled [PROJECTNAME_USERNAME] and save files in it
#TODO, naming
pathname = 1
#directory = "project_name/" 
directory = soup.title.string
    #sample string:
    #Home · jekyll/jekyll Wiki · GitHub
    #follows format
        #Home · [user or organization]/[project] Wiki · GitHub

directory = directory.replace("/",' ')
dir1 = directory.split()
dirname = dir1[3]+"_by_"+dir1[2]+"/"

#dir1 =[Home, . ,]

input()

#while pathname < 4:
if not os.path.exists(dirname):
    os.makedirs(dirname)
   
#create a txt file of this name + write object to the file
os.chdir(dirname)
f = open(dir1[2]+'_mainwiki.txt','w') #TODO naming
#f.write('hello world')
f.write(soup.prettify())

#create folder titled with [PROJECTNAME_TABS] #TODO naming
subdirectory = "wiki_tabs"
os.makedirs(subdirectory)

#loop through all the links/subpage in the wiki navigation
#create text file for each subpage
links = soup.findAll('a',attrs={'class':'wiki-page-link'})

os.chdir(subdirectory)
for a in links:
    print (a['href'])
    url = wiki + a['href']

    #loop through all the links/subpage in the wiki navigation
    #create text file for each subpage
    links = soup.findAll('a',attrs={'class':'wiki-page-link'})
       
    with io.open("tab_" + a.string + ".txt", 'w', encoding='utf-8') as f:
        response = urllib.request.urlopen(url)
        the_page = response.read()
        response.close
        soup = BeautifulSoup(the_page)
        f.write(soup.prettify())              
            

   # pathname += 1

f.close()



