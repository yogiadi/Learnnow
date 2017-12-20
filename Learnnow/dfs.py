--Undirected graph

class Vertex:
	def __init__(self,name):
		self.name=name
		self.neighbours=[]
		self.color="WHITE"
		self.dis=math.inf
		self.fin=math.inf
		self.parent=None
class Graph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
	def add_vertex(self,vertex):
		if vertex not in self.vertices:
			self.vertices.append(vertex)
	def add_edge(self,vertex1,vertex2):
		vertex1.neighbours.append(vertex2)
		vertex2.neighbours.append(vertex1)

def dfs(graph):
	for i in graph.vertices:
		i.color="WHITE"
		i.parent=None
		print("i is ",i.name," i.color is " , i.color)
	graph.time=0
	for i in graph.vertices:
		if i.color=="WHITE":
			print("i is ",i.name," i.color is " , i.color," time is ",graph.time)
			dfs_visit(graph,i)
def dfs_visit(graph,i):
	graph.time=graph.time+1
	print("i is ",i.name," i.color is " , i.color," time is ",graph.time)
	i.dis=graph.time
	i.color="GREY"
	print("i is ",i.name," i.color is " , i.color," time is ",graph.time, "discovery time is ",i.dis)
	for j in i.neighbours:
		if j.color=="WHITE":
			print("i is ",i.name," i.color is " , i.color," time is ",graph.time, "discovery time is ",i.dis)
			print("j is ",j.name," j.color is " , j.color," time is ",graph.time, "discovery time is ",j.dis)
			j.parent=i
			dfs_visit(graph,j)
	i.color="BLACK"
	print("i is ",i.name," i.color is " , i.color," time is ",graph.time, "discovery time is ",i.dis)
	graph.time=graph.time+1
	i.fin=graph.time
	print("i is ",i.name," i.color is " , i.color," time is ",graph.time, "discovery time is ",i.dis," finish time is ",i.fin)

import math
u,v,w,x,y,z=Vertex('u'),Vertex('v'),Vertex('w'),Vertex('x'),Vertex('y'),Vertex('z')
graph=Graph('graph')
graph.add_vertex(u);graph.add_vertex(v);graph.add_vertex(w);graph.add_vertex(x);graph.add_vertex(y);graph.add_vertex(z);
graph.add_edge(u,v);graph.add_edge(u,x);graph.add_edge(x,v);graph.add_edge(x,y);graph.add_edge(v,y);
graph.add_edge(w,y);graph.add_edge(w,z);graph.add_edge(z,z);

class DirGraph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
		self.time=0
	def add_vertex(self,vertex):
		if vertex not in self.vertices:
			self.vertices.append(vertex)
	def add_edge(self,vertex1,vertex2):
		vertex1.neighbours.append(vertex2)
u,v,w,x,y,z=Vertex('u'),Vertex('v'),Vertex('w'),Vertex('x'),Vertex('y'),Vertex('z')
graph=DirGraph('dirgraph')
graph.add_vertex(u);graph.add_vertex(v);graph.add_vertex(w);graph.add_vertex(x);graph.add_vertex(y);graph.add_vertex(z);
graph.add_edge(u,v);graph.add_edge(u,x);graph.add_edge(x,v);graph.add_edge(y,x);graph.add_edge(v,y);
graph.add_edge(w,y);graph.add_edge(w,z);graph.add_edge(z,z);


dfs(graph)

for i in graph.vertices:
	print ("i is ",i.name , " color is ",i.color,"discovery time is ", i.dis , " finish time is ",i.fin)


>>> for i in graph.vertices:
	print ("i is ",i.name , " color is ",i.color,"discovery time is ", i.dis , " finish time is ",i.fin)

	
i is  u  color is  BLACK discovery time is  1  finish time is  2
i is  v  color is  BLACK discovery time is  2  finish time is  3
i is  w  color is  BLACK discovery time is  5  finish time is  6
i is  x  color is  BLACK discovery time is  3  finish time is  4
i is  y  color is  BLACK discovery time is  4  finish time is  5
i is  z  color is  BLACK discovery time is  6  finish time is  7

for i in graph.vertices:
	for j in i.neighbours:
		print("i is ",i.name," j is ",j.name)

>>> dfs(graph)
i is  u  i.color is  WHITE
i is  v  i.color is  WHITE
i is  w  i.color is  WHITE
i is  x  i.color is  WHITE
i is  y  i.color is  WHITE
i is  z  i.color is  WHITE
i is  u  i.color is  WHITE  time is  0
i is  u  i.color is  WHITE  time is  1
i is  u  i.color is  GREY  time is  1 discovery time is  1
i is  u  i.color is  GREY  time is  1 discovery time is  1
j is  v  j.color is  WHITE  time is  1 discovery time is  inf
i is  v  i.color is  WHITE  time is  2
i is  v  i.color is  GREY  time is  2 discovery time is  2
i is  v  i.color is  GREY  time is  2 discovery time is  2
j is  y  j.color is  WHITE  time is  2 discovery time is  inf
i is  y  i.color is  WHITE  time is  3
i is  y  i.color is  GREY  time is  3 discovery time is  3
i is  y  i.color is  GREY  time is  3 discovery time is  3
j is  x  j.color is  WHITE  time is  3 discovery time is  inf
i is  x  i.color is  WHITE  time is  4
i is  x  i.color is  GREY  time is  4 discovery time is  4
i is  x  i.color is  BLACK  time is  4 discovery time is  4
i is  x  i.color is  BLACK  time is  5 discovery time is  4  finish time is  5
i is  y  i.color is  BLACK  time is  5 discovery time is  3
i is  y  i.color is  BLACK  time is  6 discovery time is  3  finish time is  6
i is  v  i.color is  BLACK  time is  6 discovery time is  2
i is  v  i.color is  BLACK  time is  7 discovery time is  2  finish time is  7
i is  u  i.color is  BLACK  time is  7 discovery time is  1
i is  u  i.color is  BLACK  time is  8 discovery time is  1  finish time is  8
i is  w  i.color is  WHITE  time is  8
i is  w  i.color is  WHITE  time is  9
i is  w  i.color is  GREY  time is  9 discovery time is  9
i is  w  i.color is  GREY  time is  9 discovery time is  9
j is  z  j.color is  WHITE  time is  9 discovery time is  inf
i is  z  i.color is  WHITE  time is  10
i is  z  i.color is  GREY  time is  10 discovery time is  10
i is  z  i.color is  BLACK  time is  10 discovery time is  10
i is  z  i.color is  BLACK  time is  11 discovery time is  10  finish time is  11
i is  w  i.color is  BLACK  time is  11 discovery time is  9
i is  w  i.color is  BLACK  time is  12 discovery time is  9  finish time is  12
>>> for i in graph.vertices:
	print("i is ",i.name," i.color is " , i.color," time is ",graph.time, "discovery time is ",i.dis," finish time is ",i.fin)

	
i is  u  i.color is  BLACK  time is  12 discovery time is  1  finish time is  8
i is  v  i.color is  BLACK  time is  12 discovery time is  2  finish time is  7
i is  w  i.color is  BLACK  time is  12 discovery time is  9  finish time is  12
i is  x  i.color is  BLACK  time is  12 discovery time is  4  finish time is  5
i is  y  i.color is  BLACK  time is  12 discovery time is  3  finish time is  6
i is  z  i.color is  BLACK  time is  12 discovery time is  10  finish time is  11
>>> 