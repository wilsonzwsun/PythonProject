
class SearchEngineBase(object):

	def __init__(self):
		pass

	def add_corpus(self,file_path):
		with open(file_path,'r') as fin:
			text = fin.read()
		self.process_corpus(file_path,text)

	def process_corpus(self,id,text):
		raise Exception('~ not implemented.')

	def search(self,query):
		raise Exception('search not implemented')

def main(se):
	for fp in ['1.txt','2.txt','3.txt','4.txt','5.txt']:
		se.add_corpus(fp)

	while True:
		query = input("input txt: ")
		res = se.search(query)
		print('found {} result :'.format(len(res)))
		for re in res:
			print(re)
