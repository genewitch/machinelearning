import csv
floflag = True  #is prime column float/double?
passing = 0.92  # threshold that this 'fitness test' denotes the predictor labelling a number as prime
lowest = 0.99       # lowest score seen
highest = 0.001     #highest score seen

wcl = 99997 #wc -l of the file, or whatever you set in the other python.
comparefile = open(r'C:\pythonvenvs\igel\testcompare.csv', newline='')
compreader = csv.reader(comparefile)
predictionfile = open(r'C:\pythonvenvs\igel\model_results\predictions.csv', newline='') 
predreader = csv.reader(predictionfile)

predict = []
compare = []
total = 0
correct = 0
falsepos = 0
falseneg = 0
pcount = 0
ccount = 0 
for row in predreader:
    if row[-1] == "prime":
        continue
    #print(row[0],row[-1])
    if not floflag:
        predict.append(row[-1])
        if row[-1] == "1":
            pcount = pcount + 1
    else:
        predict.append(float(row[-1]))
        if float(row[-1]) > passing:
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

if not floflag:
    for itr8 in range(0,len(compare)):
        total = total + 1
        if predict[itr8] == compare[itr8]:
            correct = correct + 1
        elif predict[itr8] == "1" and compare[itr8] == "0":
            falsepos = falsepos + 1
        elif predict[itr8] == "0" and compare[itr8] == "1":
            falseneg = falseneg + 1
else:
    for itr8 in range(0,len(compare)):
        total = total + 1
        if predict[itr8] <= lowest:
            lowest = predict[itr8]
        elif predict[itr8] > highest:
            highest = predict[itr8]
        if predict[itr8] <= passing and compare[itr8] == "0" or predict[itr8] > passing and compare[itr8] == "1":
            correct = correct + 1
        elif predict[itr8] > passing and compare[itr8] == "0":
            falsepos = falsepos + 1
        elif predict[itr8] <= passing and compare[itr8] == "1":
            falseneg = falseneg +1 
            
assert( falsepos + falseneg == total-correct )
            
print("Total:\t" + str(total) + "\t\tCorrect:" + str(correct))
print("Incorrect:\t" + str(total-correct) + "\t\tBut count shows:" + str(falsepos+falseneg) + " incorrect")
print("Ratio incorrect/correct:\t" + str((total-correct)/correct))
print("False Positives:\t" + str(falsepos) + "\t\tFalse Negatives:\t" + str(falseneg))
if floflag:
    print("Highest score:\t" + str(highest) + "\t\tLowest:" + str(lowest))
    
