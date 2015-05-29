#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import lrc_bayes
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math
import re
def normalize(n, p):
    return math.log(n)/math.log(p)

def show(arr):
    for p in arr:
        print '%s\t%r' % p

if __name__ == '__main__':
    
    lrc_list = []
    max_n = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            cols = line.split('\t')
            lrc_list.append((cols[0], float(cols[1])))
    save_path = sys.argv[3]
    p = 10
    lrc_list = [(k.replace(' ', '').replace('<S>', '').replace('</S>','').decode('utf-8'), normalize(v, p))
                for k, v in lrc_list if v>p]
    #lrc_list = [(k, normalize(v)) for k, v in lrc_list if v>1]
    lrc_list = [p for p in lrc_list if not re.search('[a-zA-Z]', p[0])]
    
    print 'Done with %s phrase.' % len(lrc_list)
    show(lrc_list[:300])
    #wordcloud = WordCloud(width=400, height=int(400*0.618),max_words=40, font_path='/home/zhangcheng/.fonts/noto/NotoSansCJKjp-Bold.otf')
    size = 12000
    wordcloud = WordCloud(width=size, height=int(size/4),max_words=min(max_n, len(lrc_list)), font_path='/home/zhangcheng/.fonts/noto/NotoSansCJKjp-Bold.otf')
    wordcloud.fit_words(lrc_list[:max_n])
    wordcloud.to_file(save_path) 
