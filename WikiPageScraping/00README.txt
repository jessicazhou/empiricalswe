Prerequisite: 
Python 3.6.5
beautifulsoup4-4.6.0
bs4-0.0.1
html5lib-1.0.1

Notes:
Before running the script, please change the file directory in line 73 of autoscraping.py to your file directory.
Make sure sampleURLS.txt has newline after last URL entry for the script to process it (looking for ".git\n") 

To help better understand the occurence of documentation within wiki pages in open source software projects, the scripts:
    (1) Take an input of a list of Github projects
    (2) Scrapes web pages of Github projects that actually have wiki pages with BeautifulSoup & generates a text report detailing:
        1 - # projects that no longer exist
        2 - # projects with default (empty) / no wiki page
        3 - # projects with wiki pages that have content
    (3) Converts the text report to CSV for further analysis

Inputs of 383 and 87,674 projects as well as their respective outputs, have been provided as well.

---------------------------------------------------
(1 & 2) SCRAPING sample command:
    python3 autoscraping.py sampleURLS.txt

    in repository:
    SAMPLE INPUT FILE: (file of URLs) 1input_sampleURLS.txt

    SAMPLE OUTPUT FILES: (folder) 2Output_383_report_and_scraped_wikis
                                (file report) 2output.txt
                                (folder Github repo Wiki #1)
                                    (html file) tab_1
                                    (html file) tab_2
                                    ....
                                (folder Github repo Wiki #2)
                                (folder Github repo Wiki #3)
                                .....


             
(3) POSTPROCESSING: 
    python3 txtprocessor.py output_from_autoscraping.txt 

    in repository:
    INPUT: text report file:
                2output.txt
    OUTPUT FILE: csv file 
                3output.csv


In the folder "00Run_87674_URLs_and_Wikis" 
the same process is applied to a group of 87,674 Github links, 
split into 9 batches of ~10k projects each.

Each .txt in "1input_txt_1_to_9" folder corresponds to 
one of "2output_downloaded_wiki_and_txt_report"'s output folders (containing output.txt & scraped projects) 
and one of "3output_csv_files"'s csv files.

----------------------------------------------------

OBSERVATIONS:
In a sample of 87,674 Github projects: 
   1) don't exist:        12,891    14.70%
   2) empty or no Wiki:   73,570    83.91%
   3) existing Wiki:      1,213     1.38%
Factoring out the 12,891 no longer existing projects, that leaves 74,783 Github projects, 1,213, or 1.62% of which have Wiki pages.

NOTED ERRORS/TODOS:
If # folders of downloaded projects =/= # projects with wikipages in report
    -there may be project names that begin with "." (saving the project as a dot file under current program)
    -two distinct URLS (changed username,project name, or both) map to the same project 
-Linking postprocessing to scraping   
-Might be better to have output be authorname then projectname
-If URL redirects to another project URL (project/author change), capture new URL
-Run stops at the same place in batches 4 - androrat by naltaleaj, 6 - hgi-reports.git by wtsi-hgi, 7 - coffee-react-rtansform by gusvargas)


----------------------------------------------------

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
