import gmplot
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from pyvis.network import Network

############################################################## 1.1 Get Locations and Plot Map #################################################################
geolocator = Nominatim(user_agent="geoapi")

kl = geolocator.geocode("Kuala Lumpur")
jakarta = geolocator.geocode("Jakarta")
bangkok = geolocator.geocode("Bangkok")
taipei = geolocator.geocode("Taipei")
hk = geolocator.geocode("Hong Kong")
tokyo = geolocator.geocode("Tokyo")
beijing = geolocator.geocode("Beijing")
seoul = geolocator.geocode("Seoul")

kl_coordinates = (kl.latitude, kl.longitude)
jakarta_coordinates = (jakarta.latitude, jakarta.longitude)
bangkok_coordinates = (bangkok.latitude, bangkok.longitude)
taipei_coordinates = (taipei.latitude, taipei.longitude)
hk_coordinates = (hk.latitude, hk.longitude)
tokyo_coordinates = (tokyo.latitude, tokyo.longitude)
beijing_coordinates = (beijing.latitude, beijing.longitude)
seoul_coordinates = (seoul.latitude, seoul.longitude)


apikey=''
gmap = gmplot.GoogleMapPlotter(kl.latitude, kl.longitude, 4, apikey=apikey)

latitude = [kl.latitude, jakarta.latitude, bangkok.latitude, taipei.latitude, hk.latitude, tokyo.latitude, beijing.latitude, seoul.latitude]
longitude= [kl.longitude, jakarta.longitude, bangkok.longitude, taipei.longitude, hk.longitude, tokyo.longitude, beijing.longitude, seoul.longitude]
gmap.scatter(latitude, longitude, color='red', size=40, marker=True)
gmap.marker(kl.latitude,kl.longitude, color='white')
gmap.plot(latitude, longitude, 'blue', edge_width=3)
gmap.draw("map.html")

######################################################################## 1.2 Get Distances ######################################################################

distances = [[0 for i in range(8)] for j in range(8)]
city_coordinates = [kl_coordinates, jakarta_coordinates, bangkok_coordinates, taipei_coordinates, hk_coordinates, tokyo_coordinates, beijing_coordinates, seoul_coordinates]

for i in range(8):
    for j in range(8):
        distances[i][j] = great_circle(city_coordinates[i], city_coordinates[j]).kilometers

net=Network("700px", "1000px")

net.add_node(0, label="Kuala Lumpur", size=10)
net.add_node(1, label="Jakarta", size=10)
net.add_node(2, label="Bangkok", size=10)
net.add_node(3, label="Taipei", size=10)
net.add_node(4, label="Hong Kong", size=10)
net.add_node(5, label="Tokyo", size=10)
net.add_node(6, label="Beijing", size=10)
net.add_node(7, label="Seoul", size=10)

for i in range(8):
    for j in range(8):
        if i is not j:
            value = str(round(great_circle(city_coordinates[i], city_coordinates[j]).kilometers, 2)) + " km"
            net.add_edge(i, j, label=value, font_color="white")

net.toggle_physics(True)
net.barnes_hut(spring_length=200)
net.show_buttons()
net.show("graph.html")

################################################################### Journey Planner ############################################################################


class Graph:
    # Constructor
    def __init__(self, edges, N):
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

count= 0 #count for number of hamiltonian paths discovered
pathstring = [] #array to store all hamiltonian paths
distance_array = [] #array to store path distances

#############################################################
#     Backtracking algorithm to find hamiltonian paths      #
#############################################################

def hamiltonian_path(g, v, visited, path, N, pathstring):
    if len(path) == N:
        # print hamiltonian path
        global count
        count+=1

        pathstring.append(path[:]) #append to global array
        print(path)

        return

    # Check if every edge starting from vertex v leads to a solution or not
    for w in g.adjList[v]:

        # process only unvisited vertices as hamiltonian
        # path visits each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)

            # check next vertex (w) to see if path is a valid hamiltonian
            hamiltonian_path(g, w, visited, path, N, pathstring)

            # Backtracking function
            visited[w] = False
            path.pop()


if __name__ == '__main__':
    #edgelist assignment
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
             (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
             (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
             (3, 4), (3, 5), (3, 6), (3, 7),
             (4, 5), (4, 6), (4, 7),
             (5, 6), (5, 7),
             (6, 7)]

    N = 8 #number of nodes

    g = Graph(edges, N) #create graph

    start = 0 #fixed starting node

    path = [start] #assigned a starting path

    # mark start node as visited
    visited = [False] * N
    visited[start] = True

    hamiltonian_path(g, start, visited, path, N, pathstring)
    print("\ntotal hamiltonian paths: ", count)

#############################################################
# bubble-calc algorithm to calculate distances of all paths #
#############################################################

def pathdistance(pathstring, city_coordinates, distance_array):

    temp_distance = 0

    for i in range(len(pathstring)):
        current_path = pathstring[i]
        for j in range(7):
            temp_distance = great_circle(city_coordinates[current_path[j]], city_coordinates[current_path[j+1]]).kilometers + temp_distance

        distance_array.append(temp_distance)
        temp_distance = 0

pathdistance(pathstring, city_coordinates, distance_array)

print(distance_array)

# sortedpaths = sorted(distance_array)
#
#
# for i in distance_array:
#     if distance_array[i] == sortedpaths[1]:
#         print("hi", distance_array[i])

######################################################################################################## TIM SORT FROM HERE ###########################################################################

minrun = 32

def InsSort(arr, start, end):
    for i in range(start + 1, end + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    # The `first` array should go from `start` to
    # `mid + 1`, while the `right` array should
    # go from `mid + 1` to `end + 1`
    first = arr[start:mid + 1]
    last = arr[mid + 1:end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    ind1 = 0
    ind2 = 0
    ind = start

    while ind1 < len1 and ind2 < len2:
        if first[ind1] < last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1 < len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2 < len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr


def TimSort(arr):
    n = len(arr)
    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `minrun` size.
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = InsSort(arr, start, end)

    curr_size = minrun
    while curr_size < n:
        # Compute the `mid` (where the first array ends
        # and the second starts) and the `end` (where
        # the second array ends)
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr
    # utility function to print the Array


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()


# Driver program to test above function
if __name__ == "__main__":
    arr = distance_array #DISTANCE ARRAY IS THE ARRAY I WANT SORTED
    n = len(arr)
    print("Given Array is")
    printArray(arr, n)

    TimSort(arr)

    print("After Sorting Array is")
    printArray(arr, n)


