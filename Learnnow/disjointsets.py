class  dsets:
	"""docstring for  """
	def __init__(self,name):
		self.parent=self
		self.name=name
		self.rank=0

def union(dsets1,dsets2):
	link(find_set(dsets1),find_set(dsets2))

def link(dsets1,dsets2):
	if dsets1.rank > dsets2.rank :
		dsets2.parent=dsets1
	else :
		dsets1.parent=dsets2
		if (dsets1.rank == dsets2.rank):
			dsets2.rank=dsets2.rank +1
def find_set(dsets):
	if dsets != dsets.parent:
		dsets.parent=find_set(dsets.parent)
	return dsets.parent

>>> a=dsets('a')
>>> b=dsets('b')
>>> c=dsets('c')
>>> d=dsets('d')

>>> a=dsets('a')
>>> b=dsets('b')
>>> c=dsets('c')
>>> d=dsets('d')
>>> union(a,b)
>>> union(b,c)
>>> union(c,d)
>>> union(a,c)
>>> a.rank
0
>>> b.rank
2
>>> c.rank
0
>>> d.rank
0



