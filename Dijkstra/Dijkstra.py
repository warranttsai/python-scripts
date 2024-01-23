# the map has tons of vertices with the distance between neighbors.
# set the distance of start vertex to start vertex as 0 
# search from the first vertex to the last, everytime has to search all the vertice.
# record the distances between start vertex and neighbors.
# visit the unvisited vertex with smallest distance.
# calculate the distance through different vertice, if it is shorter, record it in previous_vertex and dist. Or remain still.
# note: the lanes are two-way, consider about the opposite situation
import sys
import operator

Vertice = [1, 2, 3, 4, 5, 6]
map = [[1, 6, 14],  # from, to, distance
		[1, 3, 9],
		[1, 2, 7],
		[2, 3, 10],
		[2, 4, 15],
		[3, 6, 2],
		[3, 4, 11],
		[4, 5, 6],
		[5, 6, 9]
		]
unvisited = {}
dist = [sys.maxsize]*(len(Vertice)+1)  # The table will contain 1 to 1 and 1 to the others. So use Vertice +1.
previous_vertex = [1]*(len(Vertice)+1)

dist[1] = 0
# First step
for i in map:  # search every neighbors
	if i[0] == 1:
		unvisited[i[1]] = i[2]  # {i[1]:i[2]} => {destination:distance}
		dist[i[1]] = i[2]
		
# Show
print("Vertice | Distance | PreviousVertice" )
for i in Vertice:
	print(i, "\t|", dist[i], "\t|", previous_vertex[i])
	
# while loop
while len(unvisited) >= 1:
	s = sorted(unvisited.items(), key=operator.itemgetter(1))	
	for i in s:
		unvisited.pop(i[0])
		for j in map:
			# the lanes are two-way.
			if i[0] == j[0]:
				if (dist[i[0]]+j[2]) < dist[j[1]]:  # if the distance to destination is shorter. 
					dist[j[1]] = dist[i[0]] + j[2]
					unvisited[j[1]] = dist[j[1]]
					previous_vertex[j[1]] = j[0]
				else:
					unvisited[j[1]] = j[2] 
			elif i[0] == j[1]:
				if dist[i[0]]+j[2] < dist[j[0]]:
					dist[j[0]] = dist[i[0]]+j[2]
					unvisited[j[0]] = dist[j[0]]
					previous_vertex[j[0]] = j[1]			
		# Show
		print("Vertice | Distance | PreviousVertice" )
		for i in Vertice:
			print(i, "\t|", dist[i], "\t|", previous_vertex[i])