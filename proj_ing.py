#/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import time
import re
import os

def num_pages(page):
    c = 0
    for line in page:
        if line.find("page-") != -1:
            c+= 1
            if (c == 8):
                print line
                temp = line.split("page-", 1)[1]
                temp = temp.split('"', 1)[0]
                temp = int(temp)
                return temp

url_base = raw_input("URL do topico: ")
titulo = raw_input("Titulo do topico: ")

page = urllib.urlopen(url_base)
num = num_pages(page)


page.close()
