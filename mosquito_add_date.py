import csv
import os
import datetime, time

def folderMosquitoRead():
    mosquitoFile = []
    AllMosquitoData = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/Mosquito/Mosquito/result_mosquito_data/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                mosquitoFile.append(fileName)

    for i in range(len(mosquitoFile)):
        f = open(mosquitoFile[i],'r')
        csvReader = csv.reader(f)

        for row in csvReader:
            AllMosquitoData.append(row)

    return AllMosquitoData

def collectAllData(mData):
    collectMosqutioData = []

    for i in range(len(mData)):
        if(i%2==0):
            for j in range(len(mData[i])):
                if(int(mData[i][j][8])>=1 and int(mData[i][j][8])<=4):
                    continue
                else:
                    collectMosqutioData.append(mData[i][j])

    return (collectMosqutioData)

def classifyByData(yearData):

    #All the years consist of 184 dates from May 1 to October 31
    #dictionary

    MayToOctober = [0]*184
    May = [0]*31
    June = [0]*30
    July = [0]*31
    August = [0]*31
    September = [0]*30
    October = [0]*31

    date_list = []
    mosquito_list = []

    m_dict = {}
    for i in range(len(yearData)):
        l = yearData[i].split()
        date = l[0][2:]
        mosquito = (l[-1][:-2])
        if(mosquito[0] == "'"):
            mosquito = mosquito[1:]
        date_list.append(date)
        mosquito_list.append(mosquito)
        print (date+" "+mosquito)

    for i in range(len(date_list)):
        mCnt=0.0
        for j in range(len(date_list)):
            if(date_list[i]==date_list[j]):
                mCnt += float(mosquito_list[i])

    """m_dict=dict(zip(date_list,mosquito_list))
    print (len(m_dict))"""


if __name__ == '__main__':
    data_2011 = []
    data_2012 = []
    data_2013 = []
    data_2014 = []

    rawData = (collectAllData(folderMosquitoRead()))

    for i in range(len(rawData)):
        if(rawData[i][5]=='1'):
            data_2011.append(rawData[i])
        elif(rawData[i][5]=='2'):
            data_2012.append(rawData[i])
        elif (rawData[i][5] == '3'):
            data_2013.append(rawData[i])
        elif (rawData[i][5] == '4'):
            data_2014.append(rawData[i])

    classifyByData(data_2011)

    """l = data_2011[248].split()
    print (l) # date
    print (float(l[3][0:len(l[3])-3])) #rainfall"""

