
#import urllib.request import Request, urlopen
#from bs4 import BeautifulSoup
import http.cookiejar
import urllib.parse
import urllib.request
import sys
import os
import io
from bs4 import BeautifulSoup

wiki = "https://github.com/snowplow/snowplow/wiki"


response = urllib.request.urlopen(wiki)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page, "lxml")


links = soup.findAll('a',attrs={'class':'wiki-page-link'})


for a in links:
    print (a['href'])
    url = https://github.com + a['href']
    print("this is the url ", url)
        
        #create text file for each subpage
    with io.open("tab_" + a.string + ".txt", 'w', encoding='utf-8') as f:
        try:
          print("this is the url ", url)

          response = urllib.request.urlopen(url)
          the_page1 = response.read()
          response.close
          soup1 = BeautifulSoup(the_page1, "lxml")
          f.write(str(soup1))      
        except urllib.error.HTTPError as e: #if too many requests sent to server / too many tabs
          time.sleep(10)
          print("sleeping because 429 status code received")
          time.sleep(50)
          

          reponse = urllib.request.urlopen(url)
          the_page1 = response.read()
          response.close
          soup1 = BeautifulSoup(the_page1, "lxml")
          f.write(str(soup1)) 
        
        

"""

response = urllib.urlopen(url)
print(reponse.getcode())

try:
    conn = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    # ...
    print('HTTPError: {}'.format(e.code))
"""
"""
#line = "https://github.com/bwidawsk/hobos/wiki"
#line = "https://github.com/jekyll/jekyll/wiki"
line = "https://github.com/login"

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

payload = urllib.parse.urlencode({"username or email address": "USERNAME HERE",
                                  "password": "PASSWORD HERE",
                                  "redirect": "index.php",
                                  "sid": "",
                                  "login": "Login"}).encode("utf-8")
response = opener.open(line, payload)
"""

"""
#REFhttps://stackoverflow.com/questions/45023861/login-to-website-using-urllib-instead-of-http-client

#with urllib.request.urlopen(line) as response:
html = response.geturl()
print("response ", html)
print(len(html))

print("request ", line)
print(len(line))


if(line==html):
    print("same\n")
else:
    print("not\n")
"""

"""
req = Request(line)
response=urlopen(req).geturl()
print(response)
"""

"""
line = "https://github.com/bwidawsk/hobos/wiki"
#line = "https://github.com/jessicazhou/empiricalswe/wiki"

response = urllib.request.urlopen(line)
the_page = response.read()
response.close
soup = BeautifulSoup(the_page)


pls=requests.get(line)


a=urllib.urlopen(line)
a.getcode()
"""

#pls=requests.get(line)


#if(str(pls) == '<Response [302]>') :
 #   print('hi')

#line = "https://github.com/bwidawsk/hobos/wiki"
#line = "https://github.com/jessicazhou/empiricalswe/wiki"#links = soup.findAll('a',attrs={'class':'wiki-page-link'})

#line = "https://github.com/bwidawsk/hobos/wiki"
#line = "https://github.com/jessicazhou/empiricalswe/wiki"




#output = open('out1.txt','w') 

#if the sidebar exists, there is custom content to scrape
"""
link = soup.find_all("nav", attrs={"data-selected-links":'repo_projects'}) 
print(link)
output.write("js-selected-navigation-item\n")
output.write(str(link))

#x = urllib.request.urlopen('https://www.google.com/')
#print(x.read())
"""

"""



# soup.find_all("p", "title")
# <p class="title"><b>The Dormouse's story</b></p>

#<a class="btn btn-sm btn-primary" href=/hessicazhou/empiricalswe/wiki/_new" 



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


    
#

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