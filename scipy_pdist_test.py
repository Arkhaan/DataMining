from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree, cut_tree
from matplotlib import pyplot as plt
import csv
import numpy as np
paramarray= [[1,5,6],[2,4,4],[9,1,8]]

# csv_name = "mini_table.csv"
# #csv_name = "sequence_table.csv"
# fl = open(csv_name, 'r')
# reader = csv.DictReader(fl,  delimiter=';')
# array = []
# for row in reader:
#     # array.append([len(row['seq'])])
#     #
#     # if row["weight"] != "NA" and str(row["isoelectric point"]) != 'NA':
#     #     array.append([row["weight"], row["isoelectric point"]])
#     if row["weight"] != "NA":
#         array.append([row["weight"]])
#
#
# matrix_distance = pdist(array, metric= 'euclidean')
# Z = linkage(matrix_distance, 'ward')
# #calculate full dendrogram
# plt.figure(figsize=(25, 10))
# plt.title('Hierarchical Clustering Dendrogram')
# plt.xlabel('sample index')
# plt.ylabel('distance')
# dendrogram(
#     Z,
#     leaf_rotation=90.,  # rotates the x axis labels
#     leaf_font_size=8.,  # font size for the x axis labels
# )
# plt.show()


# print type(Z)
# print len(Z.tolist())
#
# print dir(to_tree(Z))
# print to_tree(Z).count

def clusterisation(data, metric, clustertype, plot = True):
    matrix_distance = pdist(data, metric= metric)
    Z = linkage(matrix_distance, clustertype)
    R = dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )

    if plot:
        plt.figure(figsize=(25, 10))
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('sample index')
        plt.ylabel('distance')
        plt.show()
    clusters = cut_tree(Z, len(set(R["color_list"]))-1)

    return clusters

def cut(tree, distance):
    root, nodelist = to_tree(tree, rd=True)

    branches = []
    findBranches(root, distance, branches)
    return branches

def findBranches(root, distance, nodes):
    if root.dist < distance:
        nodes.append(root.pre_order(lambda x: x.id))
    else:
        leftSide = root.get_left()
        rightSide = root.get_right()
        findBranches(leftSide, distance, nodes)
        findBranches(rightSide, distance, nodes)

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

# def multicluster(data, parameters):
#     branches = [data.keys()]
#     count = 0
#     for parameter in parameters:
#         result = []
#         for branch in branches:
#             toCluster = []
#             for number in data:
#                 if number in branch:
#                     try:
#                         toCluster.append([data[number][parameter]])
#                     except:
#                         pass
#             resultGlobal = clusterisation(toCluster, 'euclidean', 'ward', True)
#
#
#             branch1, branch2 = cut(resultGlobal)
#             result.append(branch1)
#             result.append(branch2)
#         branches = result
#     return branches

def testRecursif(data, result = [], parameters = []):
    if len(parameters) == 0:
        return result
    if result == []:
        branches = [data.keys()]
    else:
        branches = [result]
        result = []
    #print branches
    for branch in branches:
        #print branch
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
        # print("Quelle distance vous semble optimale?")
        # distance = float(raw_input())
        # newBranches = cut(resultGlobal, distance)
        # for newBranch in newBranches:
        #     tmp = []
        #     for element in newBranch:
        #         tmp.append(listID[element])
        #     result.append(tmp)
        # print result
        # print "1 tour de recursive"
        # print parameters
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
            #result [1] = testRecursif(data, result[1], parameters[:-1])
    return newResult


data = openFile("testTable.csv")
#result = testRecursif(data, [], ['weight', 'aromaticity', 'isoelectric point'])
result = testRecursif(data, [], ['size', 'weight', 'aromaticity', 'instability index', 'isoelectric point', 'sheet', 'turn', 'helix'])
print result
