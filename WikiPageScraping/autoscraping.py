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
    nowikiornocontent=0
    linecount=0

    output.write(" 1 = no project 2 = no wiki or no content exist 3 = wiki and content exist\n")

    for line in f:
        if(len(line)<18):
            print("end of file processing\n")
            break #safeguard for eof whitespace
        linecount+=1
        print("project #"+str(linecount)+"\n")
        fline=line.replace("\n","")
        output.write(fline+";")        

        #if project exists
        if(urlcheck(line)):
            line=line.replace(".git\n","/wiki") 
            
            response = urllib.request.urlopen(line)
            the_page = response.read()
            response.close
            soup = BeautifulSoup(the_page, "html5lib")
            #os.chdir(foldername)
           
            link = soup.find_all("div",class_="has-rightbar")  #if the sidebar exists, there is custom content to scrape
            if(len(link)>0):
                wikitab+=1
                #content in wiki
                output.write("3")
                os.system("python3 /home/jess/Documents/spring\\ 18/research/this\\ scraping\\ thing/scripts!/WikiPageScraping/scraping.py " + line) #change this line
            else:
                #either no wiki tab or empty tab
                output.write("2")    
                nowikiornocontent+=1                                  
        else:
            #print("project doesn't exist")
            output.write("1")
            noproject+=1
        output.write("\n")


output.write("\n\nTotal projects: "+str(linecount)+"\nProjects with wiki tab and wiki content: "+str(wikitab)+" / "+str(linecount)+" or {:.2%}".format(wikitab/linecount))
output.write("\nProjects that don't exist anymore: "+str(noproject)+" / "+str(linecount)+" or {:.2%}".format(noproject/linecount))
output.write("\nProjects with no wiki tab or no wiki content: "+str(nowikiornocontent)+" / "+str(linecount)+" or {:.2%}".format(noproject/linecount))
output.write("\nRuntime: %s seconds" %(time.time() - start_time))
output.close()


  

   