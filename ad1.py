
bigList = []

with open('input.txt') as f:
    lines = f.readlines()
    
    for line in lines:

        bigList.append(line.strip())

firstPlace = 0
secondPlace = 0
thirdPlace = 0

runningTotal = 0


for item in bigList:
    if item != "":
        runningTotal = int(item) + runningTotal
    if item == "":
        
        #print(runningTotal)

        if runningTotal >= firstPlace:
            thirdPlace = secondPlace
            secondPlace = firstPlace
            firstPlace = runningTotal
            runningTotal = 0
        if runningTotal >= secondPlace and runningTotal < firstPlace:
            thirdPlace = secondPlace
            secondPlace = runningTotal
            runningTotal = 0
        if runningTotal >= thirdPlace and runningTotal < secondPlace:
            thirdPlace = runningTotal
            runningTotal = 0
        if runningTotal < thirdPlace:
            runningTotal = 0



print(firstPlace)
print(secondPlace)
print(thirdPlace)

print(firstPlace+secondPlace+thirdPlace)