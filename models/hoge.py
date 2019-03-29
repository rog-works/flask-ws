from flask import g
from werkzeug.local import LocalProxy

class Hoge():
	def _init__(self):
		self.v = 0

def __get_hoge():
	if not hasattr(g, 'hoge'):
		g.hoge = Hoge()
	return g.hoge

hoge = LocalProxy(__get_hoge)
