"""
created Sat Mar 31, 2018
@author: jessicazhou

"""

import os
import sys

param_1= sys.argv[1]
with open(param_1) as f:
    for line in f:
        line=line.replace(".git","/wiki")
        os.system("python3 scraping.py " + line)
        #or /home/jess/Documents/spring 18/research/this scraping thing/scripts!/WikiPageScraping
        system("pause")