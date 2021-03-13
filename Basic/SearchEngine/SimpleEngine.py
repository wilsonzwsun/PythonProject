from SearchEngineBase import SearchEngineBase
from SearchEngineBase import main

class SimpleEngine(SearchEngineBase):
	def __init__(self):
		super(SimpleEngine,self).__init__()
		self.__id_to_texts = {}

	def process_corpus(self,id,text):
		self.__id_to_texts[id] = text

	def search(self,query):
		res = []
		for id,text in self.__id_to_texts.items():
			if query in text:
				res.append(id)
		return res

if __name__ == '__main__':
	SE = SimpleEngine()
	main(SE)
