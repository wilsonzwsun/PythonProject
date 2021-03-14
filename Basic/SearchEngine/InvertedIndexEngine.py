from Basic.SearchEngine.SearchEngineBase import SearchEngineBase
from Basic.SearchEngine.SearchEngineBase import main
import re


class InvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(InvertedIndexEngine, self).__init__()
        self.inverted_id = {}

    def add_corpus(self, file_path):
        super().add_corpus(file_path)

    def process_corpus(self, fid, text):
        words = self.parse_words(text)
        for word in words:
            if word not in self.inverted_id:
                self.inverted_id[word] = []
            self.inverted_id[word].append(fid)

    ##########################
    #####hard to understand ###########
    def search(self, query):
        query_words = self.parse_words(query)
        query_words_index = list()
        for query_word in query_words:
            query_words_index.append(0)

        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_id:
                return []

        result = []
        while True:

            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []

            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_id[query_word]

                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])

            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    # resturn word hash set
    @staticmethod
    def parse_words(text):
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        words = text.split(' ')
        words = filter(None, words)

        return set(words)


if __name__ == '__main__':
    IE = InvertedIndexEngine()
    main(IE)
