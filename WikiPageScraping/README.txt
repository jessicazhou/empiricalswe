Takes an input of a list of github pages to scrape the content of wiki tab with BeautifulSoup for further analysis.
Creates report of 1) projects that have content in wiki or 2) projects that don't exist or 3) don't have a wiki tab, or have an empty wikitab.



Prerequisite: 
Python 3.6.5
beautifulsoup4-4.6.0
bs4-0.0.1
html5lib-1.0.1

Notes:
Before running the script, please change the file directory in line 73 of autoscraping.py to your file directory.
Make sure sampleURLS.txt has newline after last URL entry for the script to process it (looking for ".git\n") 

Sample Command:
python3 autoscraping.py sampleURLS.txt

Sample line of URL in sampleURLs.txt as input:
https://github.com/jekyll/jekyll.git


Sample output: [git url];[project code, either 1, 2, or 3]
   at quick glance, this means:
   1 = no project
   2 = no wiki or no content exist
   3 = wiki and content exist
               





Python & BeautifulSoup references:

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