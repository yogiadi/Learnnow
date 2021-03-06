class Vertex:
	def __init__(self,name):
		self.name=name
		self.neighbours=[]
		self.color="WHITE"
		self.distance=math.inf
		self.parent=None
	def add_neighbours(self,vertex):
		if vertex not in self.neighbours:
			self.neighbours.append(vertex)
	def change_color(self,color):
		self.color=color
	def change_distance(self,distance):
		self.distance=distance
	def change_parent(self,vertex):
		self.parent=parent
class Graph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
	def add_vertex(self,vertex):
		if vertex not in self.vertices:
			self.vertices.append(vertex)
	def add_edge(self,vertex1,vertex2):
		vertex1.add_neighbours(vertex2)
		vertex2.add_neighbours(vertex1)

class Queue:
	def __init__(self,name):
		self.name=name
		self.items=[];
	def is_empty(self):
		return self.items==[]
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		 return self.items.pop()
	def size(self):
		return len(items)
import math
r = Vertex('r');s=Vertex('s'); t=Vertex('t')
u,v,w,x,y=Vertex('u'),Vertex('v'),Vertex('w'),Vertex('x'),Vertex('y')
graph=Graph('graph')
graph.add_vertex(r);
graph.add_vertex(s);graph.add_vertex(t);
graph.add_vertex(u);graph.add_vertex(v);graph.add_vertex(w);graph.add_vertex(x);graph.add_vertex(y);
graph.add_edge(r,v);graph.add_edge(r,s);graph.add_edge(s,w);graph.add_edge(w,t);graph.add_edge(w,x);
graph.add_edge(t,u);graph.add_edge(t,x);graph.add_edge(u,y)
graph.add_edge(x,y);graph.add_edge(x,u);


def bfs(graph,vertex):
	vertex.color='GREY'
	vertex.distance=0
	print("Vertex is ", vertex.name)
	q=Queue('queue')
	q.enqueue(vertex)
	for elem in q.items:
		print ("Element in queue is ",elem.name)
	while not q.is_empty():
		vertex1=q.dequeue()
		print("Vertex1 is ", vertex1.name)
		for elem in q.items:
			print ("Element in queue is ",elem.name)
		for i in vertex1.neighbours:
			if i.color=='WHITE':
				print("Vi is ", i.name)
				i.color='GREY'
				i.change_distance(vertex1.distance+1)
				i.parent=vertex1
				q.enqueue(i)
				for elem in q.items:
					print ("Element in queue is ",elem.name)
		vertex1.color='BLACK'

Vertex is  s
Element in queue is  s
Vertex1 is  s
Vi is  r
Element in queue is  r
Vi is  w
Element in queue is  w
Element in queue is  r
Vertex1 is  r
Element in queue is  w
Vi is  v
Element in queue is  v
Element in queue is  w
Vertex1 is  w
Element in queue is  v
Vi is  t
Element in queue is  t
Element in queue is  v
Vi is  x
Element in queue is  x
Element in queue is  t
Element in queue is  v
Vertex1 is  v
Element in queue is  x
Element in queue is  t
Vertex1 is  t
Element in queue is  x
Vi is  u
Element in queue is  u
Element in queue is  x
Vertex1 is  x
Element in queue is  u
Vi is  y
Element in queue is  y
Element in queue is  u
Vertex1 is  u
Element in queue is  y
Vertex1 is  y


>>> for i in graph.vertices:
	print("i is ",i.name," distance is " , i.distance)

	
i is  r  distance is  1
i is  s  distance is  0
i is  t  distance is  2
i is  u  distance is  3
i is  v  distance is  2
i is  w  distance is  1
i is  x  distance is  2
i is  y  distance is  3
>>> 