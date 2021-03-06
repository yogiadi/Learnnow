class Vertex:
	def __init__(self,name):
		self.name=name
		self.key=math.inf
		self.parent=None
		self.neighbours={}
class Graph:
	def __init__(self,name):
		self.name=name
		self.vertices=[]
		self.edges=[]
	def add_vertices(self,vertex1):
		if vertex1 not in self.vertices:
			self.vertices.append(vertex1)
	def add_edges(self,weight,vertex1,vertex2):
		if vertex1 not in self.vertices:
			self.vertices.append(vertex1)
		if vertex2 not in self.vertices:
			self.vertices.append(vertex2)
		list=[weight]+[vertex1]+[vertex2]
		if list not in self.edges:
			self.edges.append(list)
		vertex1.neighbours[vertex2]=weight
		vertex2.neighbours[vertex1]=weight
def build_min_heap(arr):
            print("Calling build_min_heap")
            len_arr=len(arr)
            print("Length of Array is ",len_arr)
            index=(len_arr-1)//2
            print("Index is ",index)
            while(index>=0):
              print("In while loop")
              print("Index is ",index)
              min_heapify(arr,index,len_arr)
              index=index-1
def min_heapify(arr,index,len_arr):
            left_node=2*index +1
            print("Left node is ",left_node)
            right_node=2*index+2
            print("Right is ",right_node)
            min=index
            if (left_node<=len_arr-1 and arr[left_node].key< arr[min].key):
              print("Left node ",arr[left_node].name," is greater than min ",arr[min].name)
              min=left_node
            if (right_node<=len_arr-1 and arr[right_node].key< arr[min].key):
              print("Right ",arr[right_node].name," is greater than min ",arr[min].name)
              min=right_node
            if ( min != index):
              print("Swap ",arr[min].name," ",arr[index].name)
              arr[min],arr[index]=arr[index],arr[min]
              print("Calling min_heapify again on min ",min)
              min_heapify(arr,min,len_arr)
def heap_minimum(arr):
  return arr[0]
def heap_extract_min(arr):
  min=arr[0]
  len_arr=len(arr)
  arr[0]=arr[len_arr-1]
  del arr[len_arr-1:]
  min_heapify(arr,0,len_arr-1)
  return min
def min_heap_insert(arr,element):
  arr.append(element)
  print("Array is ",arr)
  len_arr=len(arr)-1
  print("Array of length is ", len_arr)
  heap_increase_key(arr,len_arr)

def heap_increase_key(arr,index):
  while index > 0 and arr[index//2].key>arr[index].key:
    arr[index],arr[index//2]=arr[index//2],arr[index]
    index=index//2

 def mst_prim(Graph,root,Queue):
 	root.key=0
 	heap_increase_key(Queue,Queue.index(root))
 	while Queue != []:
 		vertex_min=heap_extract_min(Queue)
 		print("min name is ",vertex_min.name)
 		for next_vert in vertex_min.neighbours.keys():
 			if next_vert in Queue and vertex_min.neighbours[next_vert] < next_vert.key:
 				next_vert.parent=vertex_min
 				print("next vert" , next_vert.name," parent is " , vertex_min.name)
 				next_vert.key=vertex_min.neighbours[next_vert] 
 				heap_increase_key(Queue,Queue.index(next_vert))
 
 a=Vertex('a'); b=Vertex('b'); c=Vertex('c'); d=Vertex('d'); e=Vertex('e'); f=Vertex('f'); g=Vertex('g'); h=Vertex('h'); i=Vertex('i')

 Queue=[a,b,c,d,e,f,g,h,i]

 >>> build_min_heap(Queue)
Calling build_min_heap
Length of Array is  9
Index is  4
In while loop
Index is  4
Left node is  9
Right is  10
In while loop
Index is  3
Left node is  7
Right is  8
In while loop
Index is  2
Left node is  5
Right is  6
In while loop
Index is  1
Left node is  3
Right is  4
In while loop
Index is  0
Left node is  1
Right is  2
>>> for i in Queue:
	print(i.name)

	
a
b
c
d
e
f
g
h
i

T=Graph('T')
T.add_vertices(a); T.add_vertices(b); T.add_vertices(c); T.add_vertices(d); T.add_vertices(e); T.add_vertices(f)
 T.add_vertices(g); T.add_vertices(h); T.add_vertices(i)
 T.add_edges(4,a,b); T.add_edges(8,a,h); T.add_edges(11,b,h); T.add_edges(8,b,c); T.add_edges(2,i,c); T.add_edges(7,h,i); T.add_edges(1,h,g); T.add_edges(6,i,g)
 T.add_edges(2,g,f); T.add_edges(4,c,f); T.add_edges(7,c,d); T.add_edges(14,d,f); T.add_edges(9,d,e); T.add_edges(10,f,e)



 Left node is  1
Right is  2
min name is  a
next vert b  parent is  a
next vert h  parent is  a
Left node is  1
Right is  2
Left node  h  is greater than min  d
Swap  h   d
Calling min_heapify again on min  1
Left node is  3
Right is  4
min name is  b
next vert c  parent is  b
Left node is  1
Right is  2
Left node  c  is greater than min  g
Swap  c   g
Calling min_heapify again on min  1
Left node is  3
Right is  4
min name is  h
next vert i  parent is  h
next vert g  parent is  h
Left node is  1
Right is  2
Left node  i  is greater than min  f
Swap  i   f
Calling min_heapify again on min  1
Left node is  3
Right is  4
Left node  c  is greater than min  f
Swap  c   f
Calling min_heapify again on min  3
Left node is  7
Right is  8
min name is  g
next vert i  parent is  g
next vert f  parent is  g
Left node is  1
Right is  2
Left node  i  is greater than min  e
Swap  i   e
Calling min_heapify again on min  1
Left node is  3
Right is  4
Left node  c  is greater than min  e
Swap  c   e
Calling min_heapify again on min  3
Left node is  7
Right is  8
min name is  f
next vert c  parent is  f
next vert d  parent is  f
next vert e  parent is  f
Left node is  1
Right is  2
Left node  i  is greater than min  e
Swap  i   e
Calling min_heapify again on min  1
Left node is  3
Right is  4
min name is  c
next vert i  parent is  c
next vert d  parent is  c
Left node is  1
Right is  2
Left node  d  is greater than min  e
Swap  d   e
Calling min_heapify again on min  1
Left node is  3
Right is  4
min name is  i
Left node is  1
Right is  2
min name is  d
next vert e  parent is  d
Left node is  1
Right is  2
min name is  e



