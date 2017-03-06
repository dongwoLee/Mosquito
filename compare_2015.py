import csv

def readCsvToList(file):
    with open(file,'r') as f:
        reader = csv.reader(f)
        mosquito_2015 = list(reader)

    return mosquito_2015

def makeList(fList):

    factor = []
    for i in range(len(fList)):
        factor.append(float(fList[i][1]))

    return (factor)

if __name__ == '__main__':
     data_2015 = (makeList(readCsvToList("C:/Users/dw/Desktop/Mosquito/Mosquito/2015_mosquito_average.csv")))
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

     print (predict_list)