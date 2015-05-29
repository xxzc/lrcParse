#!/usr/bin/python3

import sys


def freq_load(fn):
    with open(fn) as f:
        count = 0
        freq = {}
        for line in f.readlines():
            line = line.rstrip('\n')
            cols = line.split('\t')
            freqn = float(cols[1])
            freq[cols[0]] = freqn
            count += freqn
    return (freq, count)


if __name__ == '__main__':
    lrc_fn, jp_fn = sys.argv[1:3]

    lrc_freq, lrc_count = freq_load(lrc_fn)
    jp_freq, jp_count = freq_load(jp_fn)

    bayes = {}
    for l in lrc_freq:
        if l not in jp_freq: continue
        bayes[l] = (lrc_freq[l] / jp_freq[l]) * (jp_count / lrc_count)

    for k, v in sorted(bayes.items(), key=lambda kv: kv[1], reverse=True):
        print("%s\t%f" % (k, v))
