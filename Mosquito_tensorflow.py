
import csv

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        factor_list = list(reader)

    return factor_list

def makeList(fList):

    factor = []
    for i in range(len(fList)):
        factor.append(float(fList[i][0]))

    return (factor)

if __name__ == '__main__':
    humidityList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/humidity_result.csv")))
    temperatureMaxList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/temperature.max_result.csv")))
    temperatureMinList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/temperature.min_result.csv")))
    temperatureAvgList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/temperature.avg_result.csv")))
    mosquitoList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_result.csv")))

    print (humidityList)
    print (temperatureMaxList)
    print (temperatureAvgList)
    print (temperatureMinList)
    print (mosquitoList)