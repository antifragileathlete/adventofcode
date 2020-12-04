f = open('third.txt')  # Open file on read mode


lines = f.read().split("\n")  # Create a list containing all lines
array = list(lines)

arrayBlank = []

def func():
    for line in array:
        mulitply = line*10000
        arrayBlank.append(mulitply)
    return arrayBlank



def checkSlope(rightCount):
    grid = func()
    goingRight = 0
    counter = 0
    lineCounter = 1
    for line in grid:
        if len(line) > goingRight + 1:
            position = line[goingRight]
            goingRight += rightCount
            print("Position", position)
            if position == "#":
                counter += 1
                print("Counter", counter)
            lineCounter += 1
            # print("Line:", lineCounter)
        
    return counter




def checkSlopeDown2(rightCount):
    grid = func()
    goingRight = 0
    lineCounter = 1
    counter = 0
    for index, line in enumerate(grid):
        if len(line) > goingRight + 1:
            # print("Line:", lineCounter)
            if index % 2 == 0:
                position = line[goingRight]
                goingRight += rightCount
                # print(position)
                if position == "#":
                    counter += 1
                    # print("Counter:", counter)
            lineCounter += 1
    return counter


first = checkSlope(3)
second = checkSlope(1)
third = checkSlope(7)
fourth = checkSlope(5)
fifth = checkSlopeDown2(1)


print(first)
print(second)
print(third)
print(fourth)
print(fifth)
sum = 47 * 61 * 257 * 64 * 37
print(sum)



# sum = checkSlope(3) * checkSlope(1) * checkSlope(5) * checkSlope(7) * checkSlopeDown2(1)
# print(sum)
