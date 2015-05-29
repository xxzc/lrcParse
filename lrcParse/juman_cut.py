__author__ = 'zhangcheng'

from subprocess import Popen, PIPE


class Juman:
    p = Popen(['juman', '-b'], stdin=PIPE, stdout=PIPE)
    def __init__(self):
        self.stdin = Juman.p.stdin
        self.stdout = Juman.p.stdout
    def cut(self, text):
        res = []
        for line in text.splitlines():
            self.stdin.write(bytes(line+'\n', 'UTF-8'))
            self.stdin.flush()

            res.append('<S>')
            while True:
                code = self.stdout.readline()
                #print(code)
                line = code.decode()
                if line.startswith('EOS\n'): break
                res.append(line[0:line.find(' ')])
            res.append('</S>')
        return res


if __name__ == '__main__':
    juman = Juman()

    while True:
        t = input('STR:')
        print(juman.cut(t))

