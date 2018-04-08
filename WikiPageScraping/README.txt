Takes an input of a list of github pages to scrape the content of wiki tab with BeautifulSoup for further analysis.

Prerequisite: 
Python 3.6.5
beautifulsoup4-4.6.0
bs4-0.0.1
html5lib-1.0.1

Sample Command:
python3 autoscraping.py sampleURLS.txt

Notes:
Before running the script, please change the file directory in line 73 of autoscraping.py to your file directory.


Learning Python and BS as I go, so here are some references I found helpful:

BeautifulSoup documentation
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Getting all links from a div having a class
https://stackoverflow.com/questions/8616928/python-getting-all-links-from-a-div-having-a-class

Case for when there are many pages (>15 pages, requires expansion)
Parsing a dynamic webpage, need to click on link to see the rest in the table
https://pythonprogramming.net/javascript-dynamic-scraping-parsing-beautiful-soup-tutorial/
https://github.com/snowplow/snowplow/wiki

Searching for link with specific word
https://stackoverflow.com/questions/38252434/beautifulsoup-to-find-a-link-that-contains-a-specific-word

Creating files, looping
https://stackoverflow.com/questions/12560600/creating-a-new-file-filename-contains-loop-variable-python