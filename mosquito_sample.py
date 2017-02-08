import tensorflow as tf
import itertools
import os
import csv

def huminityRead(huminityList):
    hResult=[]
    for i in range(len(huminityList)):
        yearHumidityList = open(huminityList[i],'r') #read huminity.2011~2015.csv
        csvReader = csv.reader(yearHumidityList)

        for row in csvReader:
            hResult.append(row)

    """for j in range(0,len(hResult)):
        if(int(hResult[j][0][6]) >= 1 and int(hResult[j][0][6]) <= 4):
            hResult.pop(j)"""

    #print (hResult[1825])


def folderHumidityRead():
    humidityFile = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/urbaneco/humidity/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                humidityFile.append(fileName)

    return humidityFile



if __name__ == '__main__':
    huminityRead(folderHumidityRead())