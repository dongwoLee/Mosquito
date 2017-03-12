import csv

CONST_W1=0.35666299
CONST_W2=-2.80136108
CONST_W3=-102.5102005
CONST_W4=172.35162354
CONST_W5=-26.7019825
CONST_b = -252.63739014

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
     real_list = []
     for i in range(len(data_2015)):
         if(data_2015[i]>=0 and data_2015[i]<=20):
             real_list.append("1")
         elif(data_2015[i]>=21 and data_2015[i]<=40):
             real_list.append("2")
         elif(data_2015[i]>=41 and data_2015[i]<=80):
             real_list.append("3")
         else:
             real_list.append("4")

     print (real_list)


     humidity_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/humidity.2015_result.csv")))
     rainfall_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/rainfall.2015_result.csv")))
     temperatureMax_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.max.2015_result.csv")))
     temperatureAvg_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.avg.2015_result.csv")))
     temperatureMin_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/mosquito_factor_2015/temperature.min.2015_result.csv")))

     test_mosquito=[]

     for j in range(len(data_2015)):
         m=CONST_W1 * humidity_2015[j]+CONST_W2*rainfall_2015[j]+CONST_W3*temperatureMax_2015[j]+CONST_W4*temperatureAvg_2015[j]+CONST_W5*temperatureMin_2015[j]+CONST_b
         if(m>=0 and m<=20):
             test_mosquito.append("1")
         elif(m>=21 and m<=40):
             test_mosquito.append("2")
         elif(m>=41 and m<=80):
             test_mosquito.append("3")
         elif (m < 0):
             test_mosquito.append("1")
         else:
             test_mosquito.append("4")

     print (test_mosquito)


     cnt = 0
     for k in range(len(real_list)):
         if(real_list[k]==test_mosquito[k]):
             cnt +=1

     print (cnt/len(real_list)*100)

