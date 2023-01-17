from io import StringIO
import math
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    for x in graph:
        for y in x:
            y = int(y)
    array1 = []
    for x in graph:
        array1.append(x[0])
    array2 = []
    for x in graph:
        array2.append(x[1])
    f = graph
    g = graph
    array3 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] == g[j][0]:
                array3.append(f[i][0])
    array4 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][1]:
                array4.append(f[i][1])
    array5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][0]:
                array5.append(f[i][1])

    res_array = [] 
    vertices = [] 
    for x in graph:
        for y in x:
            if y not in vertices:
                vertices.append(y)
    vertices.sort()

    for v in vertices:
        res_array.append([])
    
    for v in vertices:
        res_array[int(v)-1].append(array1.count(v))
        res_array[int(v)-1].append(array2.count(v))
        res_array[int(v)-1].append(array3.count(v))
        res_array[int(v)-1].append(array4.count(v))
        res_array[int(v)-1].append(array5.count(v))

    s = 0
    for j in range(len(vertices)):
        for i in range(5):
            if res_array[j][i] != 0:
                s += (res_array[j][i] / (len(vertices) - 1)) * math.log(res_array[j][i] / (len(vertices) - 1), 2)

    return -s