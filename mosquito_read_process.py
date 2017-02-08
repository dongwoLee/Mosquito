import tensorflow as tf
import csv,os

#This is for training Data so I collected 2011~2014 catch_mosquito data

def folderMosquitoRead():
    MosquitoFile = []
    for (path, dir, files) in os.walk("C:/Users/dw/Desktop/urbaneco/catch_mosquito/AllData/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.csv':
                fileName = (str(path)+str(filename))
                MosquitoFile.append(fileName)

    return MosquitoFile

def readMosquito(mList):
    CntMosquito = []
    resCntMosquito = []
    for i in range(len(mList)):
        yearMosquitoList = open(mList[i],'r')
        csvReader = csv.reader(yearMosquitoList)

        for row in csvReader:
            CntMosquito.append(row)

    return CntMosquito

def groupingMosquito()

if __name__ == '__main__':
    print ((readMosquito(folderMosquitoRead())))


