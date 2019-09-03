# Preorder Traversals
# Author: Jonathan Hang
import sys

def main():
	global firstList, strList, intList
	firstList = []
	strList = []
	intList = []
	#Reads in numbers from a text file
	for line in sys.stdin.readlines():
		line.split()
		firstList.append(line)
	#Numbers in file become stringp
	for item in firstList:
		strList = strList + item.split()
	#Turns string into int
	for stringNum in strList:
		intList = intList + [int(stringNum)]
		
	# Uses listMaker to seperate each case into multiple lists
	fullList = listMaker(intList)
	preorderCheck(fullList) #Checks the validity of preorder traversal of a BST 

#Creates lists without negative number
def listMaker(intList):
	newList = []
	finalList = []
	for num in intList:
		if num > 0:
			newList.append(num)
		else:
			finalList.append(newList)
			newList = []
	return finalList

def BST(node):
	minInt = -2**32
	array = [] 
	root = minInt
	for value in node: 
		if value < root: 
			return False
		while(len(array) > 0 and array[-1] < value): 
			root = array.pop() 
		array.append(value) 
	return True

def preorderCheck(fullList):
	caseCounter = 1
	for num in fullList:
		if BST(num) == True:
			print("Case %d: Yes" % (caseCounter))
		else:
			print("Case %d: No" % (caseCounter))
		#Increment the case each time it checks
		caseCounter = caseCounter + 1

if __name__ == '__main__':
    main()
