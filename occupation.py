import csv
import random


def make_dict(file):
    occD = {}
    input_file = open(file)
    reader = csv.DictReader(input_file)
    for occ in reader:
        #print occ['Job Class']
        #print occ['Percentage']
        occD[occ['Job Class']] = float(occ['Percentage'])
    occD.pop('Total')
    return occD

def pick_random(occD, total):
    chosen = random.uniform(0, total)
    for key in occD:
        chosen -= occD[key]
        if chosen <= 0.1:
            return key + ", " + str(occD[key])
    return "That's not right"


#print(make_dict("occupations.csv"))
occs = make_dict("occupations.csv")
print pick_random(occs, 99.8)

testerD = {}
top = 100000.0

for i in range (1, int(top)):
    this = pick_random(occs, 99.8)
   # print this
    try:
        testerD[this] += 1
    except:
        testerD[this] = 1
    #print testerD
for key in testerD:
    testerD[key] = testerD[key] / top * 100
print testerD
    
