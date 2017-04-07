import csv

W1 = -1.10430038
W2 = -0.08929912
W3 = -96.34046936
W4 =164.94706726
W5 = -22.91306877
b = -228.20257568

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
    humidityList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/humidity.2015_result.csv")))
    rainfallList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/rainfall.2015_result.csv")))
    temperatureMaxList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.max.2015_result.csv")))
    temperatureMinList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.min.2015_result.csv")))
    temperatureAvgList = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.avg.2015_result.csv")))

    result = []
    for i in range(len(humidityList)):
        result.append(W1*humidityList[i]+W2*rainfallList[i]+W3*temperatureMaxList[i]+W4*temperatureAvgList[i]+W5*temperatureMinList[i]+b)

    with open('another_mosquito.csv','w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(result)


