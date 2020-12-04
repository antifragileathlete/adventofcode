f = open('fourth.txt')  # Open file on read mode


array = f.read().split("\n\n") # Create a list containing all lines
# something = re.split(r'[\n\n]', lines)
# array = list(lines)
# lines = f.read() # Create a list containing all lines
first = str(array[3])
print(first)
# splitFirst = first.split(' ')
# print(splitFirst)

if (('ecl' in first) and ('hcl' in first) and ('byr' in first) and ('hgt' in first) and ('cid' in first) and ('eyr' in first) and ('pid' in first) and ('iyr' in first)):
  print("LOL")
else:
  print("Expected")

if 'iyr' in first:
  print('HOW')
else:
  print("WHY")

counter = 0











# newArray = []c


# def func():
#   emptyString = []
#   for passport in array:
#     splitArray = passport.split(',', ' ')
#     print(splitArray)

#   # print(emptyString)


#     # print(splitArray)

# func()


# newArray = array.split(',')

# print(newArray)

# for line in array:
#     splitArray = line.split(' ')
#     letterCountHigher = int(splitArray[0].split('-')[1])
#     letterCountLower = int(splitArray[0].split('-')[0])
#     letter = splitArray[1][0]
#     string = splitArray[2]

# newArray = iterutils.cunked(array, 1)
# print(newArray)

# def func():
#   for passport in array:
#     print(passport)

# func()


