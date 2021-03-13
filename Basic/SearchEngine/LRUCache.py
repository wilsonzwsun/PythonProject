import pylru

class LRUCache(object):
	def __init__(self,size=32):
		self.cache = pylru.lrucahe(size)

	def has(self,key):
		return key in self.cache

	def get(self,key):
		return self.cache[key]

	def set(self,key,val):
		self.cache[key] = val

