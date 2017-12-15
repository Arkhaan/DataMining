from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree
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

    if plot:
        plt.figure(figsize=(25, 10))
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('sample index')
        plt.ylabel('distance')
        dendrogram(
            Z,
            leaf_rotation=90.,  # rotates the x axis labels
            leaf_font_size=8.,  # font size for the x axis labels
        )
        plt.show()
    return Z

def cut(tree):
    root, nodelist = to_tree(tree, rd=True)
    idsleft = root.get_left().pre_order(lambda x: x.id)
    idsright = root.get_right().pre_order(lambda x: x.id)
    return idsleft, idsright

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

def multicluster(data, parameters):
    branches = [data.keys()]
    for parameter in parameters:
        result = []
        for branch in branches:
            toCluster = []
            for number in data:
                if number in branch:
                    try:
                        toCluster.append([data[number][parameter]])
                    except:
                        pass
            resultGlobal = clusterisation(toCluster, 'euclidean', 'ward', False)
            branch1, branch2 = cut(resultGlobal)
            result.append(branch1)
            result.append(branch2)
        branches = result
    return branches

data = openFile("mini_table.csv")
result = multicluster(data, ['weight', 'aromaticity'])
print result
for n in result:
    print len(n)

            # if len(branches) == 0:
            #     for number in data:
            #         try:
            #             toCluster.append([data[number][parameter]])
            #         except:
            #             pass
            # else:
