class Vertex:
	def __init__(self,name):
		self.name=name
		self.parent=self
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

class Graph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
		self.edges=[]
	def add_vertices(self,vertex):
		if vertex not in self.vertices:
			self.vertices.append(vertex)
	def add_edges(self,weight,point1,point2):
		edge=[weight]+[point1]+[point2]
		if edge not in self.edges:
			self.edges.append(edge)

def mst_kruskal(supertree,A):
	sorted_edge=sorted(supertree.edges,key=lambda l:l[0])
	for weight , point1 , point2 in sorted_edge:
		print("weight is ",weight , "point1 is ",point1.name,"point2 is ",point2.name)
		print(find_set(point1).name)
		if find_set(point1) != find_set(point2):
			print("Add vetices")
			A.add_vertices(point1)
			A.add_vertices(point2)
			A.add_edges(weight,point1,point2)
			union(point1,point2)

 a=Vertex('a'); b=Vertex('b'); c=Vertex('c'); d=Vertex('d'); e=Vertex('e'); f=Vertex('f'); g=Vertex('g'); h=Vertex('h'); i=Vertex('i')

 T=Graph('T')
T.add_vertices(a); T.add_vertices(b); T.add_vertices(c); T.add_vertices(d); T.add_vertices(e); T.add_vertices(f)
 T.add_vertices(g); T.add_vertices(h); T.add_vertices(i)
 T.add_edges(4,a,b); T.add_edges(8,a,h); T.add_edges(11,b,h); T.add_edges(8,b,c); T.add_edges(2,i,c); T.add_edges(7,h,i); T.add_edges(1,h,g); T.add_edges(6,i,g)
 T.add_edges(2,g,f); T.add_edges(4,c,f); T.add_edges(7,c,d); T.add_edges(14,d,f); T.add_edges(9,d,e); T.add_edges(10,f,e)

weight is  1 point1 is  h point2 is  g
h
Add vetices
weight is  2 point1 is  i point2 is  c
i
Add vetices
weight is  2 point1 is  g point2 is  f
g
Add vetices
weight is  4 point1 is  a point2 is  b
a
Add vetices
weight is  4 point1 is  c point2 is  f
c
Add vetices
weight is  6 point1 is  i point2 is  g
g
weight is  7 point1 is  h point2 is  i
g
weight is  7 point1 is  c point2 is  d
g
Add vetices
weight is  8 point1 is  a point2 is  h
b
Add vetices
weight is  8 point1 is  b point2 is  c
g
weight is  9 point1 is  d point2 is  e
g
Add vetices
weight is  10 point1 is  f point2 is  e
g
weight is  11 point1 is  b point2 is  h
g
weight is  14 point1 is  d point2 is  f
g

>>> for i in A.vertices:
	print(i.name)

	
h
g
i
c
f
a
b
d
e
>>> for weight , point1 , point2 in A.edges:
		print("weight is ",weight , "point1 is ",point1.name,"point2 is ",point2.name)

		
weight is  1 point1 is  h point2 is  g
weight is  2 point1 is  i point2 is  c
weight is  2 point1 is  g point2 is  f
weight is  4 point1 is  a point2 is  b
weight is  4 point1 is  c point2 is  f
weight is  7 point1 is  c point2 is  d
weight is  8 point1 is  a point2 is  h
weight is  9 point1 is  d point2 is  e

