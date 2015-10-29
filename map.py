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
jiebav2.load_userdict("./product.dic")

# 
#list_dirs =  os.walk("./product_dict")
#for root,dirs,files in list_dirs:
#	for f in files:
#		if ".dic" in f:
#			print os.path.join(root,f)
#			jiebav2.load_userdict(os.path.join(root,f))
#

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
xx = "现代休闲沙发椅"
xx = "现代休闲沙发椅	名师设计	特莱维"
xx = "鹰岩男女款冲锋裤1310202"
xx = "鹰岩男女款冲锋衣1310101"
xx = "美孚/Mobil 1号全合成机油 5W-40 SN级10L+曼牌HU718/5X"
xx= "张小盒加薪英雄旅行箱20寸"
xx = "幸运叶子包邮正品阿迪三叶草2013新冬女裤运动裤长裤G84410"
xx = "【圣诞季】拼毛羽绒服"
xx = "贝嘉琦	儿童滑板车	/二轮三轮踏板	高度可调伸缩带闪光轮多省包邮"

i = 0
#for line in sys.stdin:
for line in [xx]:
	i += 1
	#line = trans_string(line.strip("\n"))
	line = line.strip("\n").replace("\t","").replace(" ","")
	seg_list = jiebav2.posseg.cut(line)

	for x in seg_list:
		#print x.word + "\t" + x.flag
		print "\t".join([str(i),x.word,x.flag])
