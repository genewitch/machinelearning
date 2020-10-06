#this is just for primality guessings

import csv

wcl = 99997 #wc -l
comparefile = open(r'C:\pythonvenvs\igel\testcompare.csv', newline='')
compreader = csv.reader(comparefile)
predictionfile = open(r'C:\pythonvenvs\igel\model_results\predictions.csv', newline='') 
predreader = csv.reader(predictionfile)

predict = []
compare = []
total = -1
correct = 0
falsepos = 0
falseneg = 0
pcount = 0
ccount = 0 
for row in predreader:
    if row[0] == "id":
        continue
    #print(row[0],row[-1])
    predict.append(row[-1])
    if row[-1] == "1":
        pcount = pcount + 1
#print(str(pcount))
predictionfile.close()

    
for row in compreader:
    if row[-1] == "prime":
        continue
    #print(row[0],row[-1])
    compare.append(row[-1])
    if row[-1] == "1":
        ccount = ccount + 1
#print(str(ccount))
comparefile.close()

for itr8 in range(0,len(compare)):
    total = total + 1
    if predict[itr8] == compare[itr8]:
        correct = correct + 1
    elif predict[itr8] == "1" and compare[itr8] == "0":
        falsepos = falsepos + 1
    elif predict[itr8] == "0" and compare[itr8] == "1":
        falseneg = falseneg + 1
    
    
print("Total:\t" + str(total) + "\t\tCorrect:" + str(correct))
print("Incorrect:\t" + str(total-correct) + "\t\tBut count shows:" + str(falsepos+falseneg) + " incorrect")
print("Ratio incorrect/correct:\t" + str((total-correct)/correct))
print("False Positives:\t" + str(falsepos) + "\t\tFalse Negatives:\t" + str(falseneg))
assert( falsepos + falseneg == total-correct )
    
