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
	def add_edges(self,weight,vertex1,vertex2):
		if vertex1 not in self.vertices:
			self.vertices.append(vertex1)
		if vertex2 not in self.vertices:
			self.vertices.append(vertex2)
		self.edges.append([weight]+[vertex1]+[vertex2])
		list=[weight]+[vertex1]+[vertex2]
		if list not in self.edges:
			self.edges.append(list)
		vertex1.neighbours[vertex2]=weight
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

 def dijkstra(graph,vertex,queue):
 	while queue != []:
 		min_vert=heap_extract_min(queue)
 		for vert_itr in min_vert.neighbours.keys():
 			if vert_itr in queue:
 				relax(min_vert.neighbours[vert_itr],min_vert,vert_itr)
 				heap_increase_key(queue,queue.index(vert_itr))

 def relax(weight,vertex1,vertex2):
	if vertex2.key > vertex1.key + weight:
		vertex2.key=vertex1.key + weight
		vertex2.parent=vertex1
		print("vertex1 is ",vertex1.name,"vertex2 is " , vertex2.name,"distance of vertex2 is ", vertex2.key)

s=Vertex('s'); t=Vertex('t'); x=Vertex('x'); y=Vertex('y'); z=Vertex('z');
T=Graph('T')
T.add_edges(10,s,t); T.add_edges(5,s,y); T.add_edges(1,t,x); T.add_edges(2,t,y); T.add_edges(4,x,z); T.add_edges(6,z,x);
 T.add_edges(7,z,s); T.add_edges(3,y,t); T.add_edges(9,y,x); T.add_edges(2,y,z); 

>>> s.key=0
>>> queue=[s,t,x,y,z]
>>> build_min_heap(queue)
Calling build_min_heap
Length of Array is  5
Index is  2
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

dijkstra(T,s,queue)

>>> dijkstra(T,s,queue)
Left node is  1
Right is  2
vertex1 is  s vertex2 is  t distance of vertex2 is  10
vertex1 is  s vertex2 is  y distance of vertex2 is  5
Left node is  1
Right is  2
Left node  t  is greater than min  z
Swap  t   z
Calling min_heapify again on min  1
Left node is  3
Right is  4
vertex1 is  y vertex2 is  t distance of vertex2 is  8
vertex1 is  y vertex2 is  x distance of vertex2 is  14
vertex1 is  y vertex2 is  z distance of vertex2 is  7
Left node is  1
Right is  2
Left node  t  is greater than min  x
Swap  t   x
Calling min_heapify again on min  1
Left node is  3
Right is  4
vertex1 is  z vertex2 is  x distance of vertex2 is  13
Left node is  1
Right is  2
vertex1 is  t vertex2 is  x distance of vertex2 is  9
Left node is  1
Right is  2

>>> for i in T.vertices:
	print(i.name,i.key)

	
s 0
t 8
y 5
x 9
z 7
>>> 