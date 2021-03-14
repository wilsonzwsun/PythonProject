from Basic.SearchEngine.SearchEngineBase import SearchEngineBase
from Basic.SearchEngine.SearchEngineBase import main
import re


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__text_dict__ = {}

    # add files into dict
    def add_corpus(self, file_path):
        super(BOWEngine, self).add_corpus(file_path)

    ######
    def process_corpus(self, id, text):
        # raise Exception('~ not implemented.')
        self.__text_dict__[id] = self.parse_words(text)

    def search(self, query):
        # raise Exception('search not implemented')
        res = []
        query_set = self.parse_words(query)
        for fid, words_set in self.__text_dict__.items():
            if self.match(query_set, words_set):
                res.append(fid)
        return res

    # resturn word hash set
    @staticmethod
    def parse_words(text):
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        words = text.split(' ')
        words = filter(None, words)

        return set(words)

    @staticmethod
    def match(queryset, wordset):
        # raise Exception()
        for query in queryset:
            if query in wordset:
                return True
            return False


if __name__ == '__main__':
    BE = BOWEngine()
    main(BE)
