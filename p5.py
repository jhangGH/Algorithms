# D. Hill Climbing Bikers
# Author: Jonathan Hang
import sys

class Vertex:
    def __init__(self,coordinate,table):
        def difCalc(table,coordinate1,coordinate2):
            t1 = table[coordinate1[0]][coordinate1[1]]
            if coordinate2 == None:
                t2 = 0
            else:
                t2 = table[coordinate2[0]][coordinate2[1]]
            return t2 - t1
        self.name = coordinate
        self.x = coordinate[0]
        self.y = coordinate[1]
        if self.x > 0:
            self.up = (self.x - 1, self.y)
        else:
            self.up = None
        if self.y < len(table) - 1:
            self.right = (self.x, self.y + 1)
        else:
            self.right = None
        if self.x < len(table)- 1:
            self.down = (self.x + 1, self.y)
        else:
            self.down = None
        if self.y > 0:
            self.left = (self.x, self.y - 1)
        else:
            self.left = None
        self.upDif = difCalc(table,coordinate,self.up)
        self.downDif = difCalc(table,coordinate,self.down)
        self.leftDif = difCalc(table,coordinate,self.left)
        self.rightDif = difCalc(table,coordinate,self.right)
        self.edges = [self.right,self.left,self.down,self.up]
     
        self.neighbor = {}
        if self.up != None:
            self.neighbor.update({self.up:self.upDif})
        if self.down != None:
            self.neighbor.update({self.down:self.downDif})
        if self.left != None:
            self.neighbor.update({self.left:self.leftDif})
        if self.right != None:
            self.neighbor.update({self.right:self.rightDif})
        
    def getName(self):
        return self.name

    def getNeighbor(self):
        return self.neighbor

def graph(table):
    coordinate = {}
    for row in range(len(table)):
        for column in range(len(table)):
            coordinate[(row,column)] = Vertex((row, column), table)
    return coordinate

def length(slopes):
    minValue = min(slopes)
    maxValue = max(slopes)
    if abs(maxValue) < abs(minValue):
        return minValue
    if abs(maxValue) > abs(minValue):
        return maxValue

def checkSlope():
    global dist
    slopeList = []
    while len(dist) > 1:
        pred = dist[0]
        check = dist[1]
        slopeList.append(check - pred)
        dist.remove(pred)
    return slopeList

def caseMaker():
    caseList = []
    size = 0
    table = []
    for line in sys.stdin.readlines():
        lineList = [int(col) for col in line.split()]
        if size == 0:
            info = lineList
            size = info[0]
        elif [0]*5 == lineList:
            break
        elif size == 1:
            table.append(lineList)
            size = 0
            start = (info[1]-1, info[2]-1)
            end = (info[3]-1, info[4]-1)
            case = [start, end, table]
            table = []
            caseList.append(case)
        else:
            table.append(lineList)
            size = size - 1
    return caseList

def setCases(cases):
    global dist, table
    caseAnswers = []
    for item in cases:
        start = item[0]
        end = item[1]
        table = item[2]
        g = graph(table)
        dist = []
        dijkstra(g,start,end,[],{},{})
        slope = checkSlope()
        l = length(slope)
        caseAnswers.append(l)
    return caseAnswers

def dijkstra(graph, source, destination, visited, distances, predecessors):
    global dist
    if source == destination:
        path=[]
        dist=[]
        pred = destination
        while pred != None:
            row = pred[0]
            column = pred[1]
            cost = table[row][column]
            dist.append(cost)
            path.append(pred)
            pred=predecessors.get(pred, None)
        dist = dist[::-1]
    else :     
        if not visited: 
            distances[source]=0
        for neighbor in graph[source].getNeighbor(): # Visit the neighbors
            if neighbor not in visited:
                new_distance = distances[source] + abs(graph[source].getNeighbor()[neighbor])
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = source
        visited.append(source)
        unvisited = {}
        for i in graph:
            if i not in visited:
                unvisited[i] = distances.get(i, float('inf'))        
        x = min(unvisited, key = unvisited.get)
        dijkstra(graph, x, destination, visited, distances, predecessors)

""" Prints out the cases """
def printCases(cases):
    counter = 1
    for case in range(len(cases)):
        print("Case %d: %s" % (counter, str(cases[len(cases) - case-1])))
        counter = counter + 1

def main():
    global table
    cases = caseMaker()
    printCases(setCases(cases)[::-1])

if __name__ == "__main__":
    main()
