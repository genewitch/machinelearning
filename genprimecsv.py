import math

#set False for data.csv, eval.csv, testcompare.csv; set True for test.csv
istest = False
minnumber=3         #these have to be hand edited. sorry.
maxnumber=99998     #this too

#this is if your test data is less digits than the eval data.
# if you train/eval on 7 digit numbers and then try to predict on 4 digit numbers sklean doesn't like
# set the first thing to +3 in that specific circumstance
if istest:
    fill=len(str(maxnumber))
else:
    fill=len(str(maxnumber))

# going to have to work IDs in at some point?
id=0

# just to make the CSV Headers
pos=fill

#this doesn't need to be quoted but i did it anyhow, CSV headers:
for digit in range(1,fill+1):
    pos = pos - 1
    if pos != 0:
        print('"' + str(10**pos) + '"',end=',')
        #pos = pos - 1
    else:
        print('"' + str(10**pos) + '"',end='') # otherwise the test csv has dangling commas
    

if not istest:    
    print(",prime") # add the comma back in for the CSV Headers
else:
    print()
    
for leftcolumn in range(minnumber,maxnumber+1):
    #print(str(id), end=',')
    #print(str(leftcolumn), end=',')
    unpadded = str(leftcolumn)
    padded = unpadded.zfill(fill)
    
    for q in range(0,len(padded)-len(unpadded)):
        print("-1", end=',')
    
    
    
    #for digit in str(leftcolumn):
        #print(str(digit), end=',')
    # ^ this sucks because there's no way to know if you're on the last digit
    # so let's use the iterable part of strings, separate with a comma and end blank,
    # in case we need to print the prime test 1 or 0
    print(*str(leftcolumn), sep=',', end='')
        
        
    if not istest:
        print(",", end='')
        
    boo = False #should be called isprime but /shrug
    
    #stupid naive and slow primality test, but 100% accurate so who cares
    sqr = math.floor(math.sqrt(leftcolumn))
    for loope in range(2,sqr+1):
       if leftcolumn % loope == 0:
          #if it's not prime and we're not testing, "0\n", otherwise "\n"
          if not istest:
            print("0")
          else:
            print()
          boo = True
          break
    if not boo:
       if not istest:
        print("1")
       else:
        print()
    id = id + 1



