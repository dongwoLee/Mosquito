import tensorflow as tf
import itertools
import os
import csv

def folderHumidityRead():
    humidityFile = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/urbaneco/humidity/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                humidityFile.append(fileName)

    return humidityFile

def huminityRead(huminityList):
    humidity=[]
    humidityResult=[]
    for i in range(len(huminityList)):
        yearHumidityList = open(huminityList[i],'r') #read huminity.2011~2015.csv
        csvReader = csv.reader(yearHumidityList)

        for row in csvReader:
            humidity.append(row)

    for j in range(0,len(humidity)):
        if(int(humidity[j][0][6]) >= 1 and int(humidity[j][0][6]) <= 4):
            continue
        else:
            humidityResult.append(humidity[j])

    return (humidityResult)

def folderRainFallRead():
    rainFallFile = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/urbaneco/rainfall/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                rainFallFile.append(fileName)

    return rainFallFile

def rainFallRead(rainFallList):
    rainFall=[]
    rainFallResult=[]
    for i in range(len(rainFallList)):
        yearRainFallList = open(rainFallList[i],'r') #read huminity.2011~2015.csv
        csvReader = csv.reader(yearRainFallList)

        for row in csvReader:
            rainFall.append(row)

    for j in range(0,len(rainFall)):
        if(int(rainFall[j][0][6]) >= 1 and int(rainFall[j][0][6]) <= 4):
            continue
        else:
            rainFallResult.append(rainFall[j])

    return (rainFallResult)

def fillZeroRainFall(hList,rList):
    lastRainFall = [0.0]*len(hList)

    for i in range(len(hList)):
        for j in range(len(rList)):
            if (hList[i][0] == rList[j][0]):
                lastRainFall[i] = float(rList[j][1])
            else:
                continue

    return lastRainFall

def saveCsv(list):
    myfile = open("C:/Users/dw/Desktop/urbaneco/result/resRainFall.csv", "w")
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(list)

if __name__ == '__main__':
    saveCsv(fillZeroRainFall(huminityRead(folderHumidityRead()),rainFallRead(folderRainFallRead())))