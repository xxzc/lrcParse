from collections import Counter
import string
import gc
import sys
__author__ = 'zhangcheng'


def top_n(tok_list, n):
    c = Counter(tok_list)
    return c.most_common(n)


def lrc_lyricist_freq(lrcs, n):
    lyricists = []
    for lrc in lrcs:
        lyricists.extend(filter(None, lrc.get('lyricists', [])))
    return top_n(lyricists, n)


def lrc_composer_freq(lrcs, n):
    composers = []
    for lrc in lrcs:
        composers.extend(filter(None, lrc.get('composers', [])))
    return top_n(composers, n)


def lrc_title_freq(lrcs, n):
    titles = filter(None, [k.get('title', '') for k in lrcs])
    return top_n(titles, n)

def lrc_show_freq(lrcs, n):
    for k,v in lrcs[n].items():
        print("%s:" %k)
        print(v)
        print()
    return []

def cut_str_block_l(s, l):
    res = []
    ignore_char = string.ascii_letters+'\u00A0'+'\u0020'+'\u3000'
    # NO-BREAK SPACE ; SPACE ; IDEOGRAPHIC SPACE
    s = s.translate(str.maketrans(ignore_char, ignore_char, ignore_char))
    for line in s.split('\n'):
        sl = len(line)
        res.extend([line[p:p+l] for p in range(0, sl-l)])
    return res


def lrc_ngram_freq(lrcs, b_n, n):
    words = []
    for l in lrcs:
        words.extend(l.get('lrc_words', []))
    del lrcs
    gc.collect()

    ngram = {}

    for p in range(0, len(words)-b_n):
        kw = ' '.join(words[p:p+b_n])
        ngram[kw] = ngram.get(kw, 0)+1

    print("%d %d_gram Generated." % (len(ngram), b_n), file=sys.stderr)
    return sorted(list(ngram.items()),
                  key=lambda kv: kv[1], reverse=True)[0:n]

