# Cookie Balancing Act
# Author: Jonathan Hang

""" Input may consist of multiple cases. Each case is described on a single line that begins with the number
of cookies (no more than 100) followed by the weight of each (in integer grams, no more than 1000
grams). Following the last case is a line containing just the number ‘0’. Arbitrary white space may
delimit the input. """

import sys

def main():
    finalList = []
    for lines in sys.stdin.readlines():
        lines.split()
        if lines == "0":
            break
        numList = []
        for num in lines[:-1].split(): # Removes whitespaces in the text file
            numList.append(int(num))
        finalList.append(numList[1:]) # Adds only the weight of the cookies to the finalList
    caseSolver(finalList)

def findMinDiff(arr,arrLength):
    sum = 0
    for i in range(arrLength):
        sum = sum + arr[i]
    
    dp=([[False for i in range(sum+1)]  
            for i in range(arrLength+1)])

    for i in range(arrLength+1):
        dp[i][0] = True

    for i in range(1,sum+1):
        dp[0][i] = False

    for i in range(1,arrLength+1):
        for j in range(1,sum+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <=j:
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    for j in range(round(sum/2),-1,-1):
        if dp[arrLength][j] == True:
            diff = sum-2*j
            break
    return abs(diff)

"""" Prints out minimum total weight difference for each case """
def caseSolver(fullList):
    caseCounter = 1
    for case in fullList:
        arrayLength = len(case)
        print("Case %d: %d" % (caseCounter, findMinDiff(case,arrayLength))) 
        caseCounter = caseCounter + 1

if __name__ == '__main__':
    main()