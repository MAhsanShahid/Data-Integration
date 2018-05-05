
import csv
import jellyfish
import re
import requests
import pandas as pd


from tqdm import tqdm


url = 'https://www.50states.com/abbreviations.htm'
html = requests.get(url).content

df_list = pd.read_html(html)
df = df_list[-1]


globalList=[]
def to_upper(oldList):
    newList = []
    for each in oldList:
        newList.append(each.upper())
    globalList.append(newList)
    return newList



def checkStates(oldList):
    i = 1

    while(i != len(df)):

        if(oldList[6] == df[0][i].upper()):
            oldList[6]= df[1][i]
        i=i+1

    return oldList


def checkCity(oldList):
    a = 0
    for each in cityList:
        if( oldList[5] == each[1].upper() or jellyfish.jaro_distance(unicode(oldList[5], "utf-8"), unicode(each[1].upper(), "utf-8")) > 0.80 ):
            oldList[5] = each[1].upper()
            a=1
            break
    if(a != 1):
        oldList[5]=""

    for each in cityList:
        if( oldList[5] == each[1].upper() or jellyfish.jaro_distance(unicode(oldList[5], "utf-8"), unicode(each[1].upper(), "utf-8")) > 0.80 ):
            oldList[5] = each[1].upper()
            a=1
            break
    return oldList

def checkZip(oldList):
    # print int(filter(str.isdigit, oldList[7]))
    oldList[7] = re.findall('\d+', oldList[7])
    oldList[7]= [''.join(map(str, oldList[7][0:1]))]
    if (len(oldList[7][0]) < 5):
        while (len(oldList[7][0]) != 5):
            oldList[7][0]= oldList[7][0] + '0'
    if (len(oldList[7][0]) > 5):
        while (len(oldList[7][0]) == 5):
            oldList[7][0] = oldList[7][0][:-1]
    oldList[7] = oldList[7][0]
    return oldList



def checkSSN(oldList):
    cleanString = oldList[10].replace("-","")
    if(len(cleanString) < 10):
        while(len(cleanString) != 8):
            cleanString = cleanString + '0'
            # print cleanString
    oldList[10]= cleanString
    return oldList[10]

cityReader = csv.reader(open('list-cities-us-30j.csv','rb'))
cityList=[]
for row in cityReader:
    cityList.append(row)



reader = csv.reader(open('inputDB.csv', 'rb'))
writer = csv.writer(open('outfile.csv','wb'))





for row in tqdm(reader):
    print "hello"
    row = to_upper(row)
    row = checkStates(row)
    row = checkCity(row)
    row = checkZip(row)
    row = checkSSN(row)
    writer.writerow(row)
    # row
    # print(', '.join(row))


