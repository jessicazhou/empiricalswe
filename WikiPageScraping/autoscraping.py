"""
created Sat Mar 31, 2018
@author: jessicazhou

"""

#python3 autoscraping.py sampleURLS.txt

import os
import os.path
import io
import sys
import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import string

param_1= sys.argv[1]

global output 


def urlcheck(url):
   
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False


with open(param_1) as f:
 
    start_time = time.time()

    output = open('output.txt','w') 

    noproject=0
    wikitab=0
    linecount=0

    for line in f:
        if(len(line)<18):
            print("end of file processing\n")
            break #safeguard for eof whitespace
        linecount+=1
        output.write(line+"\n")        

        #if project exists
        if(urlcheck(line)):
            line=line.replace(".git\n","/wiki") 
            
            response = urllib.request.urlopen(line)
            the_page = response.read()
            response.close
            soup = BeautifulSoup(the_page, "html5lib")
            #os.chdir(foldername)
            #if the sidebar exists, there is custom content to scrape
            link = soup.find_all("div",class_="has-rightbar")
            if(len(link)>0):
                wikitab+=1
                #print("content in wiki")
                output.write("content in wiki\n")
                os.system("python3 /home/jess/Documents/spring\\ 18/research/this\\ scraping\\ thing/scripts!/WikiPageScraping/scraping.py " + line)
                #or /home/jess/Documents/spring 18/research/this scraping thing/scripts!/WikiPageScraping                                                    
        else:
            #print("project doesn't exist")
            output.write("project doesn't exist\n")
            noproject+=1
        #print("\n________________________\n\n")
        output.write("\n________________________\n\n")

#print("--- %s seconds ---" % (time.time() - start_time))
    output.write("Total projects: "+str(linecount)+"\nwiki tab with content: "+str(wikitab)+" "+str(wikitab/linecount))
    output.write("\nProjects that don't exist anymore: "+str(noproject)+" "+str(noproject/linecount))
    output.write("\nRuntime: %s seconds" %(time.time() - start_time))


  

   