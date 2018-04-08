"""
created Fri Mar 30, 2018
@author: jessicazhou

"""
import os
import io
import sys
from bs4 import BeautifulSoup
import csv
import string
import urllib
import time

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
#pass in github urls in autoscraper.py
wiki= sys.argv[1]

response = urllib.request.urlopen(wiki)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page, "html5lib")

        #create a folder titled [PROJECTNAME_USERNAME] and save files in it
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

if not os.path.exists(dirname):
    os.makedirs(dirname)
      
os.chdir(dirname)
#create a txt file of this name + write object to the file
f = open(dir1[3]+'_mainwiki.txt','w') 
#f.write('hello world')
f.write(str(soup)) #soup.prettify

#create folder titled with [PROJECTNAME_TABS] 
subdirectory = "wiki_tabs"
os.makedirs(subdirectory)

#loop through all the links/subpage in the wiki navigation
#create text file for each subpage
links = soup.findAll('a',attrs={'class':'wiki-page-link'})
os.chdir(subdirectory)
for a in links:
    print (a['href'])
    git= 'https://github.com'
    url = git + a['href']
    print("this is the url ", url)

        #create text file for each subpage
    with io.open("tab_" + a.string + ".txt", 'w', encoding='utf-8') as f:
        print("this is the url ", url)
        try:
          response = urllib.request.urlopen(url)
          print("this is the url ", url)

          the_page1 = response.read()
          response.close
          soup1 = BeautifulSoup(the_page1, "html5lib")
          f.write(str(soup1))      
        except urllib.error.HTTPError as e: #if too many requests sent to server / too many tabs
          time.sleep(10)
          print("sleeping because 429 status code received")
          time.sleep(50)
          
          response = urllib.request.urlopen(url)
          print("this is the url ", url)
          the_page1 = response.read()
          response.close
          soup1 = BeautifulSoup(the_page1, "html5lib")
          f.write(str(soup1)) 
        
        
    
        #f.close()
        # pathname += 1






