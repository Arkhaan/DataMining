from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree, cut_tree
from matplotlib import pyplot as plt
import csv
import numpy as np

def clusterisation(data, metric, clustertype, plot = True):
    matrix_distance = pdist(data, metric= metric)
    Z = linkage(matrix_distance, clustertype)
    R = dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    clusters = cut_tree(Z, len(set(R["color_list"]))-1)

    if plot:
        plt.figure(figsize=(25, 10))
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('sample index')
        plt.ylabel('distance')
        plt.show()

    return clusters

def openFile(name):
    fl = open(name, 'r')
    reader = csv.DictReader(fl,  delimiter=';')
    array = {}
    count = 0
    for row in reader:
        dic = {}
        for k in row.keys():
            if row[k] != "NA":
                dic[k] = row[k]
        array[count] = dic
        count += 1
    return array

def testRecursif(data, result = [], parameters = []):
    if len(parameters) == 0:
        return result
    if result == []:
        branches = [data.keys()]
    else:
        branches = [result]
        result = []
    for branch in branches:
        toCluster = []
        listID = []
        for number in data:
            if number in branch:
                try:
                    toCluster.append([data[number][parameters[-1]]])
                    listID.append(number)
                except:
                    pass
        if len(listID) < 3:
            return listID
        resultGlobal = clusterisation(toCluster, 'euclidean', 'ward', False)
        Clusters = {}
        for i in range(0, len(resultGlobal)):
            if resultGlobal[i][0] in Clusters:
                Clusters[resultGlobal[i][0]].append(listID[i])
            else:
                Clusters[resultGlobal[i][0]] = [listID[i]]
        for key in Clusters.keys():
            result.append(Clusters[key])
        newResult = []
        for r in result:
            newResult.append(testRecursif(data, r, parameters[:-1]))
    return newResult


data = openFile("testTable.csv")
result = testRecursif(data, [], ['size', 'weight', 'aromaticity', 'instability index', 'isoelectric point', 'sheet', 'turn', 'helix'])
