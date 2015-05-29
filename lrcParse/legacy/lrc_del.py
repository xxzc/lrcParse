#!/usr/bin/python3
__author__ = 'zhangcheng'

import json
import sys
import time
import lrc_cmds


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Error: Too few args.')
        sys.exit(-1)
    ppath, infile, outfile = sys.argv

    with open(infile, 'r') as f:
        data = json.load(f)

    stime = time.time()
    for i in range(len(data)):
        del data[i]['lyric']
    etime = time.time()

    with open(outfile, 'w') as f:
        json.dump(data, f)

    print('Done. Average process time %.3fs' % ((etime-stime)/len(data)))
