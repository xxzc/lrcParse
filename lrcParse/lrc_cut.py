#!/usr/bin/python3
__author__ = 'zhangcheng'

import json
import sys
import time
import juman_cut


def text2words(t):
    segs = juman.cut(t);
    ignore_seg = ['\u00A0', '\u0020', '\u3000'] #spaces
    segs = list(filter(lambda s: s not in ignore_seg, segs))
    return segs


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Error: Too few args.')
        sys.exit(-1)
    ppath, infile, outfile = sys.argv

    with open(infile, 'r') as f:
        data = json.load(f)

    juman = juman_cut.Juman()

    stime = time.time()
    for i in range(len(data)):
        data[i]['lrc_words'] = text2words(data[i]['lyric'])
        print('%d. %s' % (i, data[i]['title']))
        #print(data[i]['lrc_words'])
    etime = time.time()

    with open(outfile, 'w') as f:
        json.dump(data, f)

    print('Done. Average process time %.3fs' % ((etime-stime)/len(data)))
