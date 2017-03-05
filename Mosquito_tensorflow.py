
import csv

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        factor_list = list(reader)

    return factor_list

def makeList(fList):

    factor = []
    for i in range(len(fList)):
        factor.append(fList[i][1])

    return factor

if __name__ == '__main__':
    print (len(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_result.csv")))
