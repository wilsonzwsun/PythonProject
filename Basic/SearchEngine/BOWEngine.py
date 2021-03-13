from SearchEngineBase import SearchEngineBase
from SearchEngineBase import main

##TODO
class BOWEngine(SearchEngineBase):
	def __init__(self):
		super(BOWEngine,self).__init__()

	def add_corpus(self,file_path):
		

	def process_corpus(self,id,text):
		raise Exception('~ not implemented.')

	def search(self,query):
		raise Exception('search not implemented')

	def match(queryset,wordset):
		raise()

