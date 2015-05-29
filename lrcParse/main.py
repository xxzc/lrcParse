#!/usr/bin/python3

__author__ = 'zhangcheng'
import json
import sys

import lrc_cmds


if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print('Error: Too few args.')
        sys.exit(-1)
    ppath, cmd, lrc_path, *args = sys.argv

    with open(lrc_path, 'r') as f:
        lrcs = json.load(f)
    print("%d Lyric Loaded." % len(lrcs), file=sys.stderr)
    #top = lrc_title_freq(lrcs, n)
    #top = lrc_lyricist_freq(lrcs, n)
    #top = lrc_lyricist_freq(lrcs, n)
    #top = lrc_lrc_freq(lrcs, 4, n)
    try:
        func = getattr(lrc_cmds, 'lrc_%s_freq' % cmd)
        top = func(lrcs, *map(int, args))
    except None:
        pass

    print("Result:", file=sys.stderr)
    for i in top:
        print('%s\t%d' % i)
