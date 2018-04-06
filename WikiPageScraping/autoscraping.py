"""
created Sat Mar 31, 2018
@author: jessicazhou

"""

#python3 autoscraping.py sampleURLS.txt

import os
import io
import sys
import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
import time

start_time = time.time()

"""
with open('results.csv','w') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow(['project name','url','present of wiki tab','content in tab'])
 
  f = open('mylist.csv', 'r')
    reader = csv.reader(f)
    mylist = list(reader)
    f.close()
    mylist[1][3] = 'X'

    my_new_list = open('mylist.csv', 'w', newline = '')
    csv_writer = csv.writer(my_new_list)
    csv_writer.writerows(mylist)
    my_new_list.close()

"""

param_1= sys.argv[1]

output = open('output.txt','w') 

def urlcheck(url):
   
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False


with open(param_1) as f:
     
        for line in f:

            print(line)
            output.write(line+"\n")

            #if project exists
            if(urlcheck(line)):
                print("project exists")
                output.write("project exists\n")

                line=line.replace(".git\n","/wiki") 

                #if the /wiki url doesn't redirect
                r = requests.get(line, allow_redirects=False)
                if(str(r) != '<Response [302]>'):
                    print("wiki exists")
                    output.write("wiki exists\n")

                    response = urllib.request.urlopen(line)
                    the_page = response.read()
                    response.close
                    soup = BeautifulSoup(the_page)

                    #if the sidebar exists, there is custom content to scrape
                    link = soup.find_all("div",class_="has-rightbar")
                    if(len(link)>0):
                        print("content in wiki")
                        output.write("content in wiki\n")

                        os.system("python3 scraping.py " + line)
                        #or /home/jess/Documents/spring 18/research/this scraping thing/scripts!/WikiPageScraping
                    else:
                        print("content not in wiki")
                        output.write("content not in wiki\n")
                else:
                    print("wiki tab doesn't exist")
                    output.write("wiki tab doesn't exist\n")
            else:
                print("project doesn't exist")
                output.write("project doesn't exist\n")
            print("\n________________________\n\n")
            output.write("\n________________________\n\n")

print("--- %s seconds ---" % (time.time() - start_time))
output.write("--- %s seconds ---" % (time.time() - start_time))
  

   