import csv



def makeDict(file):
    occD = {}
    with open(file, 'r') as occ_csv:
        reader = csv.DictReader(occ_csv)
        ## for occ in reader:
        ##     #print(occ)
        ##     print(occ[1])
        ##     occD[occ[0]] = float(occ[1])
        for occ in reader:
            occD.update(occ)
    return occD


print(makeDict("occupations.csv"))
    
