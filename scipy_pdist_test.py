from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree
from matplotlib import pyplot as plt
import csv
import numpy as np
paramarray= [[1,5,6],[2,4,4],[9,1,8]]

csv_name = "mini_table1000.csv"
# csv_name = "sequence_table.csv"
fl = open(csv_name, 'r')
reader = csv.DictReader(fl,  delimiter=';')
array = []
for row in reader:
    # array.append([len(row['seq'])])

    if row["weight"] != "NA" and str(row["isoelectric point"]) != 'NA':
        array.append([row["weight"], row["isoelectric point"]])


# print array

matrix_distance = pdist(array, metric= 'braycurtis')
Z = linkage(matrix_distance, 'ward')
# calculate full dendrogram
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


print type(Z)
print len(Z.tolist())

print dir(to_tree(Z))
print to_tree(Z).count
