#!/usr/bin/env python
#coding=utf-8

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

sys.path.append("./")

import string
from collections import defaultdict

import jiebav2
import jiebav2.posseg

seg_dict = defaultdict(lambda: 0)
threshold = 1

jiebav2.load_userdict("./userdict.dic")
jiebav2.load_userdict("./brands.dic")

def trans_string(s):
	table = string.maketrans("","")
	return line.strip().translate(table," ~`!@#$%^&*()-_=+[]\{}|;':\",./<>?")


for line in sys.stdin:
	line = trans_string(line)
	parts = line.strip().split("\t")
	if len(parts) <= 1:
		continue
	
	seg_list = jiebav2.posseg.cut(parts[0])

	for x in seg_list:
		print x.word + "\t" + x.flag
