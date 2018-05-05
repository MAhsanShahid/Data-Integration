import csv
import json
import re
from tqdm import tqdm

# realdata = [['A904694','A904696'],['A904697','A904698']]

realdata=[]
reader = csv.reader(open('update.csv', 'r'))

for data in reader:
    realdata.append(data)


def search(a):
    reader = csv.reader(open('inputDB.csv', 'r'))
    for data in reader:
        if data[0] == a:
            return data

dict = {}
i = 0
for each in tqdm(realdata):
    array = []
    for every in each:
        array.append(search(every))
    dict[i] = array
    i= i +1

print dict

for each in dict:

    for idx,every in enumerate(dict[each][0]):

        if(every == "" and dict[each][1][idx] != ""):
            dict[each][0][idx] = dict[each][1][idx]

        if(idx == 7 or idx == 10):
            dict[each][0][idx] = re.sub("\D", "", dict[each][0][idx])

        if (idx == 6 and len(dict[each][0][6]) > len(dict[each][1][6])):
            dict[each][1][idx] = dict[each][0][idx]

    for idx,every in enumerate(dict[each][1]):
        if(every == "" and dict[each][0][idx] != ""):
            dict[each][1][idx] = dict[each][0][idx]

        if (idx == 7 or idx == 10 ):
            dict[each][1][idx] = re.sub("\D", "", dict[each][1][idx])

        if (idx == 6 and len(dict[each][1][6]) > len(dict[each][0][6])):
            dict[each][0][idx] = dict[each][1][idx]

    #
print json.dumps(dict)


