__author__ = 'zhangcheng'
import json

if __name__ == '__main__':
    files = ['../lrc2w.json', '../lrc2w-5w.json', '../lrc999.json']
    lrcs = []
    for fn in files:
        with open(fn) as f:
            lrcs.extend(json.load(f))
            print('Done %s' % fn)

    with open('../lrc.json','w') as wf:
        json.dump(lrcs, wf)

    print("Done %d" % len(lrcs))