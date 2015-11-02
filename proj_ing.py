#/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import time
import re
import os

#funcao para descobrir o numero de paginas do topico
def num_pages(page):
    c = 0
    for line in page:
        if line.find("page-") != -1:
            c+= 1
            if (c == 8):
                temp = line.split("page-", 1)[1]
                temp = temp.split('"', 1)[0]
                temp = int(temp)
                return temp

#adiciona posts aos users
def add_post(line, dic_users):
    user = line.split("data-author=")[1]
    user = user.split('"')[1]
    if user in dic_users:
        dic_users[user] = dic_users[user] + 1
    else:
        dic_users[user] = 1

#inicio
url_base = raw_input("URL do tópico: ")
titulo = raw_input("Título do tópico: ")

#pega o numero de paginas
page = urllib.urlopen(url_base)
num = num_pages(page)

dic_users = {}
#le todas as paginas do topico
for index in range(1, num+1):
    url_now = url_base + "/page-" + str(index)
    page = urllib.urlopen(url_now)
    for line in page:
        if line.find('"message   " data-author=') != -1:
            add_post(line, dic_users)

for w in sorted(dic_users, key=dic_users.get, reverse=True):
    print w, dic_users[w]

page.close()
