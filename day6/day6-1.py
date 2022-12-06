input = open("day6/input.txt").read()

lenCode = 4

for i in range(0,len(input)):
    noPattern = False
    pattern = input[i:i+lenCode]
    for j in pattern:
        counter = 0
        for k in pattern:
            if j == k:
                counter += 1
        if counter > 1:
            noPattern = True
        #print(input[i:i+lenCode])
        #print(counter)
    if not noPattern:
        print(i+lenCode)
        break


