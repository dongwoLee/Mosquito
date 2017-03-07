import csv

CONST_W1=0.3566637
CONST_W2=-2.80135822
CONST_W3=-102.51014709
CONST_W4=172.35151672
CONST_W5=-26.701931
CONST_b = -252.6374054

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        mosquito_2015 = list(reader)

    return mosquito_2015

def makeList(fList):

    factor = []
    for i in range(len(fList)):
        factor.append(float(fList[i][0]))

    return (factor)

if __name__ == '__main__':
     data_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/average_mosquito_2015/2015_mosquito_average.csv")))
     predict_list = []
     for i in range(len(data_2015)):
         if(data_2015[i]>=0 and data_2015[i]<=20):
             predict_list.append("1")
         elif(data_2015[i]>=21 and data_2015[i]<=40):
             predict_list.append("2")
         elif(data_2015[i]>=41 and data_2015[i]<=80):
             predict_list.append("3")
         else:
             predict_list.append("4")

     humidity_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/humidity.2015_result.csv")))
     rainfall_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/rainfall.2015_result.csv")))
     temperatureMax_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.max.2015_result.csv")))
     temperatureAvg_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.avg.2015_result.csv")))
     temperatureMin_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.min.2015_result.csv")))

