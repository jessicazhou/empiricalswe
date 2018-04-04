"""
created Sat Mar 31, 2018
@author: jessicazhou

"""

#python3 autoscraping.py sampleURLS.txt

import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import csvimport time
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

output = open('output.csv','w') 

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

            line=line.replace(".git","/wiki")
            print(line)
            output.print(line)

            #if wiki tab exists
            if(urlcheck(line)):
                print("wiki tab exists")
                output.print("wiki tab exists")

                response = urllib.request.urlopen(line)
                the_page = response.read()
                response.close
                soup = BeautifulSoup(the_page)

                #if the sidebar exists, there is custom content to scrape
                link = soup.find_all("div",class_="has-rightbar")
                if(len(link)>0):
                    print("content in wiki")
                    output.print("content in wiki")

                    os.system("python3 scraping.py " + line)
                    #or /home/jess/Documents/spring 18/research/this scraping thing/scripts!/WikiPageScraping
                else:
                    print("content not in wiki")
                    output.print("content not in wiki")
            else:
                print("wiki page not found")
                output.print("wiki page not found")
            print("________________________")
            output.print("________________________")
print("--- %s seconds ---" % (time.time() - start_time))
output.print("--- %s seconds ---" % (time.time() - start_time))
  

   