# -*- coding: utf-8 -*-
import Document as Dc
import re
import Stemmer
from io import open

themes = ["science\t", "style\t", "culture\t", "life\t", "economics\t", "business\t", "travel\t", "forces\t",
          "media\t", "sport\t"]
infile = "news_train.txt"
outfile = "news_wo_themes.txt"
docsize = 60000

TrainTxt = open(infile, 'r', encoding='utf-8')
OutTxt = open(outfile, "w+", encoding='utf-8')

DocList = TrainTxt.read()
YO = "Ё".decode('utf8')
YE = "Е".decode('utf8')
yo = "ё".decode('utf8')
ye = "е".decode('utf8')
DocList = DocList.replace(YO, YE)
DocList = DocList.replace(yo, ye)
DocList = DocList.replace('.', '. ')
DocList = DocList.replace(';', '; ')
DocList = DocList.replace(',', ', ')

DocumentsList = []

dclist = DocList.split("\n")
dclist.pop(60000)

for doc in dclist:
    splitted = doc.split("\t")
    NewDoc = Dc.Document(splitted[0], splitted[1], splitted[2])
    DocumentsList.append(NewDoc)

dictionary = '[^абвгдежзийклмнопрстуфхцчшщъыьэюя АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-]'.decode('utf8')
regex = re.compile(dictionary)
stemmer = Stemmer.Stemmer('russian')
stemmer.maxCacheSize = 0

for doc in DocumentsList:
    doc.body = regex.sub('', doc.body.lower())
    body = ''
    for word in doc.body.split(' '):
        word = stemmer.stemWord(word)
        body = body + word + ' '
    doc.body = ' '.join(body.split())
print(DocumentsList[0].body)
