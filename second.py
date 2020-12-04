f = open('second.txt') # Open file on read mode
lines = f.read().split("\n") # Create a list containing all lines
array = list(lines)




counter = 0

for line in array:
    splitArray = line.split(' ')
    letterCountHigher = int(splitArray[0].split('-')[1])
    letterCountLower = int(splitArray[0].split('-')[0])
    letter = splitArray[1][0]
    string = splitArray[2]
        # if string.count(letter) >= letterCountLower and string.count(letter) <= letterCountHigher:
        #     counter += 1
        #     print(string, letter, string.count(letter), letterCountLower, "-", letterCountHigher,  "True", counter)
    

    if string[letterCountLower -1] == letter and not string[letterCountHigher -1] == letter:
        counter += 1
    elif not string[letterCountLower - 1] == letter and string[letterCountHigher -1] == letter:
        counter += 1
    else:
        print("whaddup")
    # else:
    #     if string[letterCountLower + 1] == letter:
    #         counter += 1

print("counter:", counter)
f.close()  # Close file


