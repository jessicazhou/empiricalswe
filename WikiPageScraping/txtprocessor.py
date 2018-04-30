"""
created April 25
@author jessicazhou
"""

#for post processing the file
#python3 txtprocessor.py output.txt (the output produced by autoscraping.py)


import os
import io
import sys
from bs4 import BeautifulSoup
import csv
import string
import urllib
import time
import csv
from urllib.parse import urlparse

param_1=sys.argv[1]

#input = open (param_1,"r") # open input file for reading

"""
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
"""

with open(param_1, 'r') as input:
    #output = open('output.csv', 'wb')
     with open('outputcsv.csv', 'w', newline='') as csvfile:
        fieldnames = ['author', 'project name', 'url', '(1) no project', '(2) no wiki/no content', '(3) wiki and content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        next(input) #skip the first line of input sample line: 'https://github.com/0-afflatus/grail_test.git ;3'
        for line in input: 
            #tokenize by space
            data=line.split(' ;',3)  #data[0] = https://github.com/0-afflatus/grail_test.git data[1] = 3
            #first item = url
            #store url
            print(data)
            print(data[0])
            print(data[1])

            url = data[0] #first url
            cat = data[1] #second item = category
        
            #then tokenize url
            token = urlparse(url) #ParseResult(scheme='https', netloc='github.com', path='/0zone/MapApi.git', params='', query='', fragment='')
            urlpath = token.path       # /0-afflatus/grail_test.git   
            print("path of url: {} \n".format(urlpath)) 
            gitinfo = urlpath.split('/')  
            print("split up url: {} \n".format(gitinfo)) 
            #store author
            author =  gitinfo[1]
            #store project
            project = gitinfo[2]
            
            if(cat=='1\n'):
                print("in cat 1")
                writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': 'x', '(2) no wiki/no content':' ', '(3) wiki and content':' '})
            elif(cat=='2\n'):
                print("in cat 2")
                writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': ' ', '(2) no wiki/no content':'x', '(3) wiki and content':' '})
            else:
                print("in cat 3")
                writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': ' ', '(2) no wiki/no content':' ', '(3) wiki and content':'x'})

        
        



