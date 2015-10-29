#!/usr/bin/env python
# -*-coding: utf8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import string
from collections import defaultdict

import jiebav2
import jiebav2.posseg

import docclass

seg_dict = defaultdict(lambda: 0)

# 常用词库
jiebav2.load_userdict("./userdict.dic")
jiebav2.load_userdict("./brands.dic")
jiebav2.load_userdict("./product.dic")

def trans_string(s):
	table = string.maketrans("","")
	return s.strip().translate(table," ~`!@#$%^&*()-_=+[]\{}|;':\",./<>?")


def getCnWords(doc):
	doc = trans_string(doc)
	words = jiebav2.posseg.cut(doc)
	words = [(w.word.encode("utf8"),w.flag) for w in words]
	result =  dict([(w,1) for w in words])
	return result


cl = docclass.fisherclassfier(getCnWords)

xx = '852,"水利水电工程施工质量监控技术杨凌职业技术学院水利水电建筑工程专业课程改革系列教材国家示范性高等职业院"'
xx1= '5385,"椒盐掌中宝"'
xx2= '3374,"色织竹节棉床单四件套（典藏）"'
xx3= '1602,"2015新款韩风童装夏季新款迷你菠萝印花纯棉女童短袖T恤"'

#for line in [xx,xx1,xx2,xx3]:
for line in open("./trainning_data.dat"):
	line = line.strip("\n")
	if len(line) < 2:
		continue
	try:
		parts = line.split(',"')
		cat_id,title = parts
		title = title.strip('"')
		#print title
		#print cat_id
		cl.train(title,cat_id)
	except:
		pass


for x in open("./test_data.dat"):
	x = x.strip("\n")
	goods_id,alias,title = x.split("\t")
	print "\t".join([goods_id,alias,cl.classify(title,"unknow"),str(cl.fisherprob(title,"3374")),title])

#print cl.fisherprob("成人奶粉","852")
#print cl.classify("成人奶粉","unknow")
