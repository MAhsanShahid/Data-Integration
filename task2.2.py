from itertools import product
import jellyfish
from tqdm import tqdm



# with open("inputDB.csv") as inputFile:
#     aList = inputFile.read().split("\n")
#     aProduct = product(aList,aList)
# # with open('update.csv', 'w') as outFile:
#     for aElem,bElem in tqdm(aProduct):
#         if ( aElem != bElem and jellyfish.jaro_distance(unicode(aElem, "utf-8"), unicode(bElem, "utf-8")) > 0.90):
#             list1 = aElem.split(",")
#             list2 = bElem.split(",")
#             output = list1[0]+ "," +list2[0]+"\n"
#             # outFile.write(output)


import csv
data= []
with open('inputDB.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)


first=[]
second=[]
third=[]
fourth=[]
fifth=[]
sixth=[]

for idx,each in tqdm(enumerate(data)):

    if(idx < len(data)/5):
        first.append(each)

    elif (idx >= len(data) / 5 and idx < (2 * len(data) / 5 )):
        second.append(each)

    elif (idx >= (2 * len(data) / 5 ) and idx < (3 * len(data) / 5)):
        third.append(each)

    elif (idx >= (3 * len(data) / 5) and idx < (4 * len(data) / 5)):
        fourth.append(each)

    else:
        fifth.append(each)



print len(first)
print len(second)
print len(third)
print len(fourth)
print len(fifth)


def generate(list):
    newlist= []
    for idx,each in tqdm(enumerate(list)):
        for ilm, every in enumerate(list):
            if(list[idx] != list[ilm] and jellyfish.jaro_distance(unicode(str(list[idx]), "utf-8"), unicode(str(list[ilm]), "utf-8")) > 0.80):
                newlist.append(each[0]+","+every[0])

    return newlist


final= []
final.append(generate(first))
final.append(generate(second))
final.append(generate(third))
final.append(generate(fourth))
final.append(generate(fifth))

print(final)

with open('next.csv', 'w') as outFile:
    for each in final:
        for every in each:
            outFile.write(every+"\n")