import csv
import os

def folderMosquitoRead():
    mosquitoFile = []
    AllMosquitoData = []
    for (path, dir, files) in os.walk("C:/Users/dw/mosquito_predict/result_mosquito_data/"):
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


if __name__ == '__main__':
    print (folderMosquitoRead())