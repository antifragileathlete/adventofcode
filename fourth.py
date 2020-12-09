f = open('fourth.txt')  # Open file on read mode


array = f.read().split("\n\n") # Create a list containing all lines
# something = re.split(r'[\n\n]', lines)
# array = list(lines)
# lines = f.read() # Create a list containing all lines
# print(array)

def func():
  blank_array = []
  for item in array:
    new_item = item.replace('\n', ' ')
    blank_array.append(new_item)
  return blank_array

good_array = func()
# print(good_array)

# first = good_array[0]
# print(first)

# sub_array = first.split(' ')
# print(sub_array)

# first_item = sub_array[4]
# print(first_item[:4])

byr_range = range(1920, 2003)
iyr_range = range(2010, 2021)


# print(sub_array)
print(good_array)
super_array = []

def newFunc():
  for array in good_array:
      sub_array = array.split(' ')
      super_array.append(sub_array)
  return super_array

great_array = newFunc()
print(great_array)

    # letters = sub_array[:4]
for subsub_array in great_array:
    for string in subsub_array:
      letters = string[:4]
      nums = string[4:]
      print(letters, nums)
    # byr_date = (array[4:])
    # print(byr_date)
    # if array[:4] == 'byr:':
    #   print(array[:4])
      # if int(array[4:]) in byr_range:
      #   print("YYYEEESS BYR CORRECT")
    # elif array[:4] == 'iyr:' and int(array[4:]) in iyr_range:
    #     print("YYYEEESS IYR CORRECTY")

# byr_range = range(1920, 2003)
# iyr_range = range(2010, 2021)
# ecl_range = ['amb','blu','brn','gry','grn','hzl','oth']
# # # print(ecl_range)
# print(good_array)


# if f'iyr:{custom_range}' in test:
#   print("worked")

# for n in byr_range:
#   print(n)
# def func():
#   counter = 0
#   for substring in array:
#     if (('ecl:' in substring) and ('hcl:' in substring) and ('byr:' in substring) and ('hgt:' in substring) and ('cid' in substring) and ('eyr:' in substring) and ('pid:' in substring) and ('iyr:' in substring)):
#       counter += 1
#       print(f'Counter: {counter}, ALL FIELS VALID')
#     elif (('ecl:' in substring) and ('hcl:' in substring) and ('byr:' in substring) and ('hgt:' in substring) and ('eyr' in substring) and ('pid:' in substring) and ('iyr:' in substring)):
#        counter += 1
#        print(f'Counter: {counter}, MATCH, ONLY CID Missing')
#     else:
#       print('NO MATCH')
#   return counter

# print(func())












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


