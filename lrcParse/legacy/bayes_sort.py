#!/usr/bin/python3

import sys
import lrc_bayes


if __name__ == '__main__':

    lrc_freq, lrc_count = lrc_bayes.freq_load(sys.argv[1])

    for k, v in sorted(lrc_freq.items(), key=lambda kv: kv[1], reverse=True):
        print("%s\t%f" % (k, v))
