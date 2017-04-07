import numpy as np

xy = np.loadtxt('2015_original_predict.csv',delimiter=',',dtype='float32')

x_data = xy[:,0:1]

original = []
result = []

for i in range(len(x_data)):
    if(x_data[i] >= 0 and x_data[i] <=20):
        original.append("1")
    elif(x_data[i] > 21 and x_data[i]<=40):
        original.append("2")
    elif (x_data[i] > 41 and x_data[i] <= 80):
        original.append("3")
    elif (x_data[i] > 81 and x_data[i] <= 160):
        original.append("4")
    elif (x_data[i] > 161 and x_data[i] <= 320):
        original.append("5")
    elif (x_data[i] > 321 and x_data[i] <= 640):
        original.append("6")
    elif (x_data[i] > 641 and x_data[i] <= 1280):
        original.append("7")
    else:
        original.append("8")

print (original)

result_data = xy[:,[-1]]

for j in range(len(result_data)):
    if (result_data[j] >= 0 and result_data[j] <= 20):
        result.append("1")
    elif (result_data[j] > 21 and result_data[j] <= 40):
        result.append("2")
    elif (result_data[j] > 41 and result_data[j] <= 80):
        result.append("3")
    elif (result_data[j] > 81 and result_data[j] <= 160):
        result.append("4")
    elif (result_data[j] > 161 and result_data[j] <= 320):
        result.append("5")
    elif (result_data[j] > 321 and result_data[j] <= 640):
        result.append("6")
    elif (result_data[j] > 641 and result_data[j] <= 1280):
        result.append("7")
    elif (result_data[i]<0):
        result.append("1")
    else:
        result.append("8")

gene_cnt = 0
one_cnt = 0

for k in range(len(x_data)):
    if((float(original[k])-float(result[k])==0)):
        gene_cnt+=1

for k in range(len(x_data)):
    if((abs(float(original[k])-float(result[k]))<=1)):
        one_cnt+=1

print (gene_cnt/len(x_data)*100)
print (one_cnt/len(x_data)*100)