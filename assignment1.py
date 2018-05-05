import mysql.connector
import jellyfish



def formatString (list):
    formatList=[]
    list = [tuple(map(str, eachTuple)) for eachTuple in list]
    for each in list:
        each = str(each).strip("(),',""")
        each = each.lower()
        formatList.append(each)
    return formatList




cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='data_integration')
cur = cnx.cursor()

cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'imdb';")
imdb = cur.fetchall()

cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'rotten_tomatoes';")
rotten_tomatoes = cur.fetchall()

cur.execute("SELECT * FROM imdb limit 20;")
imdb_data = cur.fetchall()

cur.execute("SELECT * FROM rotten_tomatoes limit 20;")
rotten_data=cur.fetchall()

cnx.close()


imdb = formatString(imdb)
rotten_tomatoes = formatString(rotten_tomatoes)

h=0
for k in imdb:
    for l in rotten_tomatoes:
        if (jellyfish.jaro_distance(unicode(k, "utf-8"), unicode(l, "utf-8")) > 0.80 and k!= 'id' and l!='id'):
            print k,l
            h=h+1
            break
print h


print imdb_data
print rotten_data


# print "dadadad"
#
#
#
# i=0
# for x in imdbList:
#     for y in rotten_tomatoesList:
#         if(x==y):
#             i=i+1
#
# print  i
#
# similarityDict={}
# for each in imdbList:
#     similarityDict[each]= 1
#
# for item in rotten_tomatoesList:
#     if(similarityDict.has_key(item)):
#         similarityDict[item]=similarityDict[item]+1;
#
# m=0
# for each in similarityDict:
#     if(similarityDict[each]==2 and each != 'id'):
#         print each
#         m = m + 1
# print m
#
#
# stt =jellyfish.match_rating_codex(u'actor name')
# pt =jellyfish.match_rating_codex(u'family name')
#
#
# print stt,pt
#
# print jellyfish.nysiis(u'name')
# print jellyfish.nysiis(u'family name')
#
# print jellyfish.jaro_distance(u'gender', u'sex')






