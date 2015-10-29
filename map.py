#!/usr/bin/env python
#coding=utf-8

import os
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

# 常用词库
jiebav2.load_userdict("./userdict.dic")

# 品牌库
jiebav2.load_userdict("./brands.dic")

# 
list_dirs =  os.walk("./product_dict")
for root,dirs,files in list_dirs:
	for f in files:
		if ".dic" in f:
			print os.path.join(root,f)
			jiebav2.load_userdict(os.path.join(root,f))


def trans_string(s):
	table = string.maketrans("","")
	return line.strip().translate(table," ~`!@#$%^&*()-_=+[]\{}|;':\",./<>?")


#for line in sys.stdin:
#	line = trans_string(line)
#	parts = line.strip().split("\t")
#	if len(parts) <= 1:
#		continue
#	
#	seg_list = jiebav2.posseg.cut(parts[0])
#
#	for x in seg_list:
#		print x.word + "\t" + x.flag
i = 1
for line in sys.stdin:
	i += 1
	line = trans_string(line.strip("\n"))
	seg_list = jiebav2.posseg.cut(line)

	for x in seg_list:
		#print x.word + "\t" + x.flag
		print "\t".join([str(i),x.word,x.flag])
