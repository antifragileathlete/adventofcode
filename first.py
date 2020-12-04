def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

array = readFile("first.txt")
array.pop(0)
array.pop(-1)

print(array)

numbers = list(map(int, array))

numbers = [1, 2, 3, 124, 765, 34, 1233, 54, 776, 344, 545, 123, 675]

sum = 2020

for num in numbers:
  for num2 in numbers:
    for num3 in numbers:
      print(num * num2 * num3)


