import csv
import math
import output
import mini

def openFile(name):
    fl = open(name, 'r')
    reader = csv.DictReader(fl,  delimiter=';')
    array = {}
    count = 0
    NAs = 0
    for row in reader:
        dic = {}
        for k in row.keys():
            if row[k] != "NA":
                dic[k] = row[k]
            else :
                NAs += 1
        array[count] = dic
        count += 1
    fl.close()
    return array

def test(result):
    global count
    if isinstance(result[0], int):
        calculateProportions(result)
        count += 1
        print("Cluster numero " + str(count) + " sur 466 (" + str(count / 466.0 * 100) + "%)")
    else:
        for node in result:
            test(node)

def calculateProportions(leaves):
    global count
    data = openFile("sequence_table.csv")
    homoCount = 0
    araCount = 0
    drosoCount = 0
    maisCount = 0
    totalWeight = 0
    totalSize = 0
    totalAromaticity = 0
    totalInstability = 0
    totalIsoelectric = 0
    totalSheet = 0
    totalTurn = 0
    totalHelix = 0
    for leave in leaves:
        if data[leave]["organism"] == "Homo":
            homoCount += 1
        elif data[leave]["organism"] == "Arabidopsis":
            araCount += 1
        elif data[leave]["organism"] == "Drosophila":
            drosoCount += 1
        elif data[leave]["organism"] == "Maize":
            maisCount += 1
        totalWeight += float(data[leave]["weight"])
        totalSize += float(data[leave]["size"])
        totalAromaticity += float(data[leave]["aromaticity"])
        totalInstability += float(data[leave]["instability index"])
        totalIsoelectric += float(data[leave]["isoelectric point"])
        totalSheet += float(data[leave]["sheet"])
        totalTurn += float(data[leave]["turn"])
        totalHelix += float(data[leave]["helix"])

    total = homoCount + araCount + drosoCount + maisCount
    print total
    weightVariance = 0
    sizeVariance = 0
    aromaVariance = 0
    instaVariance = 0
    isoVariance = 0
    sheetVariance = 0
    turnVariance = 0
    helixVariance = 0
    for leave in leaves:
        weightVariance += ((totalWeight / float(total) * 100) - float(data[leave]["weight"])) ** 2
        sizeVariance += math.sqrt((totalSize / float(total) * 100) - float(data[leave]["size"]))
        aromaVariance += ((totalAromaticity / float(total) * 100) - float(data[leave]["aromaticity"])) ** 2
        instaVariance += math.sqrt((totalInstability / float(total) * 100) - float(data[leave]["instability index"]))
        isoVariance += ((totalIsoelectric / float(total) * 100) - float(data[leave]["isoelectric point"])) ** 2
        sheetVariance += math.sqrt((totalSheet / float(total) * 100) - float(data[leave]["sheet"]))
        turnVariance += math.sqrt((totalTurn / float(total) * 100) - float(data[leave]["turn"]))
        helixVariance += math.sqrt((totalHelix / float(total) * 100) - float(data[leave]["helix"]))
    tmptotal = total
    if tmptotal <= 1:
        tmptotal = 2
    species = {count : {"number" : total,
    "weight" : weightVariance / (tmptotal - 1), "size" : sizeVariance / (tmptotal - 1), "aromaticity" : aromaVariance / (tmptotal - 1), "instability" : instaVariance / (tmptotal - 1),
    "isoelectric" : isoVariance / (tmptotal - 1), "sheet" : sheetVariance / (tmptotal - 1), "turn" : turnVariance / (tmptotal - 1), "helix" : helixVariance / (tmptotal - 1),
     "Homo" : homoCount / float(total) * 100, "Drosophila" : drosoCount / float(total) * 100, "Arabidopsis" : araCount / float(total) * 100, "Maize" : maisCount / float(total) * 100}}
    speciesFile = open("species.txt", "a")
    speciesFile.write(str(species))

speciesFile = open("species.txt", "w")
speciesFile.close()
count = 0
test(output.clusters)
print count
