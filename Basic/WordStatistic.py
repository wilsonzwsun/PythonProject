import re
import os


class WordStatis():
    BUFFER_SIZE = 200

    def __init__(self):
        self.__statis_text__ = {}

    def parse(self, text, sorted_wdict):
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        wlist = text.split(' ')
        wlist = filter(None, wlist)

        for w in wlist:
            if w not in self.__statis_text__:
                self.__statis_text__[w] = 0
            self.__statis_text__[w] += 1

        return self.__statis_text__

    def statis(self, input='in.txt', output='out.txt'):
        path = os.path.dirname(os.path.abspath(__file__))
        file = path + '/' + input
        try:
            with open(file, 'r') as fin:
                # text = fin.readlines()
                while True:
                    text = fin.readline(WordStatis.BUFFER_SIZE)
                    if not text:
                        break
                    # print(len(text))
                    text = ''.join(text)
                    self.__statis_text__ = self.parse(text, self.__statis_text__)
                # print(len(self.__statis_text__))
        except Exception as err:
            print("file:{}, error:{} ".format("in.txt", err))

        self.__statis_text__ = sorted(self.__statis_text__.items(), key=lambda v: v[1], reverse=True)

        try:
            with open(path + '/' + output, 'w') as fout:
                for w, f in self.__statis_text__:
                    fout.write('{}  {}\n'.format(w, f))
        except Exception as err:
            print("file:{}, error:{} ".format("out.txt", err))
        print('done')


myStatis = WordStatis()
myStatis.statis()
print('exit')
