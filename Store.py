# -*- coding: utf-8 -*-
import Document as Dc
import re
import Stemmer
from io import open


def initial_replacements(file_path):
    train_txt = open(file_path, 'r', encoding='utf-8')
    doc_list = train_txt.read()
    yo_caps = "Ё".decode('utf8')
    ye_caps = "Е".decode('utf8')
    yo = "ё".decode('utf8')
    ye = "е".decode('utf8')
    doc_list = doc_list.replace(yo_caps, ye_caps)
    doc_list = doc_list.replace(yo, ye)
    doc_list = doc_list.replace('.', '. ')
    doc_list = doc_list.replace(';', '; ')
    doc_list = doc_list.replace(',', ', ')
    # string
    return doc_list


def fill_doc_list(docs):
    documents_list = []
    docs_splitted = docs.split("\n")
    docs_splitted.pop(len(docs_splitted)-1)

    for doc in docs_splitted:
        single_doc = doc.split("\t")
        new_doc = Dc.Document(single_doc[0], single_doc[1], single_doc[2])
        documents_list.append(new_doc)
    # list of Document class objects
    return documents_list


def stem_doc_list(doc_list):
    dictionary = '[^абвгдежзийклмнопрстуфхцчшщъыьэюя АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-]'.decode('utf8')
    regex = re.compile(dictionary)
    stemmer = Stemmer.Stemmer('russian')
    stemmer.maxCacheSize = 0

    for doc in doc_list:
        doc.body = regex.sub('', doc.body.lower())
        body = ''
        for word in doc.body.split(' '):
            word = stemmer.stemWord(word)
            body = body + word + ' '
        doc.body = ' '.join(body.split())
    return doc_list

file_path="news_train.txt"
docs_ready = stem_doc_list(fill_doc_list(initial_replacements(file_path)))
print(docs_ready[567].body)