# Problem E
# Author: Jonathan Hang
import sys

isA = {}
hasA = {}

""" Adds is-a relations isA dictionary """
def addIsA(k, v): # key, value
    if k not in isA:
        isA.setdefault(k, [k])
        isA[k].append(v)
    else:
        isA[k].append(v)

""" Adds has-a relations to hasA dictionary """
def addHasA(k,v): # key, value
    if k not in hasA:
        hasA.setdefault(k, [])
        hasA[k].append(v)
    else:
        hasA[k].append(v)

""" is-a check """
def isADFS(v, t): # Start, end/target
    global isDis, tf
    if v == t: # Stop if start is the target
        tf = True
        return True
    if v not in isA: # Stop if start is not in isA
        tf = False
        return False 
    isDis.append(v)
    for w in isA[v]:
        if w == t:
            tf = True
            return True
        if w not in isDis:
            isADFS(w,t)

""" has-a check"""
def hasADFS(v, t):
    global isDis, hasDis, tf
    if tf == True or v == t: 
        tf = True
        return True
    if v in hasA:
        hasDis.append(v)
        for w in hasA[v]:
            if w not in hasDis:
                hasADFS(w,t)
    if v in isA:
        isDis.append(v)
        for w in isA[v]:
            if w not in isDis and w != v:
                hasADFS(w,t)

""" Gets the number of relationships from the text file """
def getRelationships():
    global textFile
    inputOne = textFile[0].split()
    num = int(inputOne[0])
    return num

""" Gets the number of queries from the text file """
def getQueries():
    global textFile
    inputTwo = textFile[0].split()
    num = int(inputTwo[1])
    return (num)

""" Makes the relationships """
def makeRelationships(relationships):
    for items in relationships:
        item = items.split()
        k = item[0] 
        op = item[1]
        v = item[2]
        if op == "is-a":
            addIsA(k,v) # Adds to the isA dictionary 
        elif op == "has-a":
            addHasA(k,v) # Adds to the hasA dictionary 

""" Prints out the answers to each query """
def queryTest(queries):
    global isDis, hasDis, tf
    counter = 1
    for items in queries:
        isDis = []
        hasDis = []
        tf = False
        item = items.split()
        k = item[0] 
        op = item[1]
        v = item[2]
        if op == "is-a":
            if k == v:
                tf = True
            else:
                isADFS(k,v)
            print("Query %d: %s " % (counter, str(tf).lower()))
        elif op == "has-a":
            isADFS(k,v)
            if tf == True:
                tf = False
            else:
                isDis = []
                hasDis = []
                hasADFS(k,v)
            print("Query %d: %s " % (counter, str(tf).lower()))
        counter = counter + 1

def main():
    global textFile, relationships, queries
    textFile = [] # List that holds all the elements from a text file
    relationships = [] # List with the relationships
    queries = [] # List with the queries
    for lines in sys.stdin.readlines(): # Reads in a text file
        lines.split()
        textFile.append(lines.strip()) # Adds all the items in a text file to a list
    numRelationships = getRelationships() # Number of relationships
    numQueries = getQueries() # Number of queries
    relationships = textFile[1:numRelationships+1] # Adds all the relationships into a list
    queries = textFile[numRelationships + 1:numRelationships + numQueries + 1] # Adds all the queries into a list
    makeRelationships(relationships)
    queryTest(queries)

    """ #TEST 
    print(isA)
    print(hasA)
    """

if __name__ == '__main__':
    main()