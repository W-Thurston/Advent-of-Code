iString = "3113322113"
output = "132123222113"
#         132123222113

## Takes over an hour to run
# # Part 1 - 40 times
# # Part 2 - 50 times
# for j in range(0,50):
#     inputList = list(iString)
#     myList = []
#     count = 1
#     for i in range(0,len(inputList)):
#
#         if len(inputList) > 1:
#             if inputList[0] == inputList[1]:
#                 count +=1
#                 del inputList[0]
#                 continue
#             else:
#                 myList.append((count, inputList[0]))
#                 # for x in range(0,count):
#                 del inputList[0]
#                 count = 1
#         else:
#             myList.append((count, inputList[0]))
#
#
#
#     outputList = []
#     for i in myList:
#         outputList.append(str(i[0]))
#         outputList.append(str(i[1]))
#
#     iString = ''.join(outputList)
#
#     print("Run "+str(j)+": "+str(len(iString)))
#     print()



# takes under a minute to run
from itertools import groupby

def look_and_say(input):
    return ''.join(str(len(list(v))) + k for k, v in groupby(input))

p1 = "3113322113"
for _ in range(40):
    p1 = look_and_say(p1)
print(len(p1))

p2 = "3113322113"
for _ in range(50):
    p2 = look_and_say(p2)
print(len(p2))