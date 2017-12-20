class Vertex:
	def __init__(self,name):
		self.name=name
		self.distance=math.inf
		self.parent=None

class Graph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
		self.edges=[]
	def add_edges(self,weight,vertex1,vertex2):
		if vertex1 not in self.vertices:
			self.vertices.append(vertex1)
		if vertex2 not in self.vertices:
			self.vertices.append(vertex2)
		self.edges.append([weight]+[vertex1]+[vertex2])
def relax(weight,vertex1,vertex2):
	if vertex2.distance > vertex1.distance + weight:
		vertex2.distance=vertex1.distance + weight
		vertex2.parent=vertex1
		print("vertex1 is ",vertex1.name,"vertex2 is " , vertex2.name,"distance of vertex2 is ", vertex2.distance)

def bellman_ford(graph,source):
	source.distance=0
	for j in range(0,len(graph.vertices)):
		for  weight,vertex1,vertex2 in graph.edges:
			relax(weight,vertex1,vertex2)
	for weight,vertex1,vertex2 in graph.edges:
		if vertex2.distance > vertex1.distance + weight:
			return False
	return True

s=Vertex('s'); t=Vertex('t'); x=Vertex('x'); y=Vertex('y'); z=Vertex('z');
T=Graph('T')
T.add_edges(5,t,x); T.add_edges(8,t,y); T.add_edges(-4,t,z); T.add_edges(-2,x,t); T.add_edges(-3,y,x); T.add_edges(9,y,z);
 T.add_edges(7,z,x); T.add_edges(2,z,s); T.add_edges(6,s,t); T.add_edges(7,s,y); 

 >>> bellman_ford(T,s)
vertex1 is  s vertex2 is  t distance of vertex2 is  6
vertex1 is  s vertex2 is  y distance of vertex2 is  7
vertex1 is  t vertex2 is  x distance of vertex2 is  11
vertex1 is  t vertex2 is  z distance of vertex2 is  2
vertex1 is  y vertex2 is  x distance of vertex2 is  4
vertex1 is  x vertex2 is  t distance of vertex2 is  2
vertex1 is  t vertex2 is  z distance of vertex2 is  -2
True
>>> s.distance
0
>>> t.distance
2
>>> x.distance
4
>>> y.distance
7
>>> z.distance
-2
>>> 




