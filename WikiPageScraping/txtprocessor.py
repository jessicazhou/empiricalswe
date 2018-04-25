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

    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['author', 'project name', 'url', '(1) no project', '(2) no wiki/no content', '(3) wiki and content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
    next(input) #skip the first line of input
    for line in input #sample line: https://github.com/0-afflatus/grail_test.git ;3
        #tokenize by space
        data=line.split(' ;',2)  #data[0] = https://github.com/0-afflatus/grail_test.git data[1] = 3
        #first item = url
        #store url
        url = data[0] 
            #then tokenize url
            token = urlparse(url)  
            token = token.path       # /0-afflatus/grail_test.git       
            token = token.split('/')  
                #store author
                author =  token[0]
                #store project
                project = token[1]
        #second item = category
        cat = data[1]
        if(cat==1):
            writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': 'x', '(2) no wiki/no content':' ', '(3) wiki and content':' '})
        else if(cat==2):
            writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': ' ', '(2) no wiki/no content':'x', '(3) wiki and content':' '})
        else:
            writer.writerow({'author': author, 'project name': project, 'url': url, '(1) no project': ' ', '(2) no wiki/no content':' ', '(3) wiki and content':'x'})

        
        



