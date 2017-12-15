# needed imports
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np



# # generate two clusters: a with 100 points, b with 50:
# np.random.seed(4711)  # for repeatability of this tutorial
# a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
# b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
# X = np.concatenate((a, b),)
csv_name = 'mini_table10000_alignment_upper_right.csv'
fl = open(csv_name, 'r')
flat_line = ""
for l in fl:
    flat_line += l[:-1]+';'

flat_list = flat_line[:-1].split(";")

print len(flat_list)

# flat_list = [1,0.5,0.9,1,0.4,1]
Z = linkage(flat_list, 'ward')
# calculate full dendrogram
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
