class SearchEngineBase(object):

    def __init__(self):
        pass

    def add_corpus(self, file_path):
        try:
            with open(file_path, 'r') as fin:
                text = fin.read()
        except Exception as err:
            print("file:{}, error:{} ".format("in.txt", err))
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('~ not implemented.')

    def search(self, query):
        raise Exception('search not implemented')


def main(searchengine):
    print("we use {} sever!!".format(type(searchengine).__name__))
    for fp in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        searchengine.add_corpus(fp)

    while True:
        query = input("input txt: ")
        res = searchengine.search(query)
        print('found {} result :'.format(len(res)))
        print(*res, sep=" , ")

        # for re in res:
        #     print("found in {} ".format(re))
