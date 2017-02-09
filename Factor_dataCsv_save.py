import tensorflow as tf
import itertools
import os
import csv

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
            humidityResult.append(float(humidity[j][1]))

    myfile = open("C:/Users/dw/Desktop/urbaneco/result_factor_data/resTemperature.min.csv","w")
    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    wr.writerow(humidityResult)



def folderHumidityRead():
    humidityFile = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/urbaneco/temperature.min/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                humidityFile.append(fileName)

    return humidityFile


if __name__ == '__main__':
    huminityRead(folderHumidityRead())