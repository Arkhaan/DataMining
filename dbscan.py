import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

import csv

import seaborn as sns


# #############################################################################

def build_matrix_line(dico_weight, csv_name):
    liste_score = []
    csvfile = open('sequence_table.csv', 'r')
    reader = csv.DictReader(csvfile,  delimiter=';')

    for dico_cible in reader:
        # if dico_cible['weight'] == None or dico_cible['isoelectric point'] == None:
        #     print dico_cible['weight']
        #     print dico_cible['isoelectric point']
        # else :
        #     dico_weight.append([float(dico_cible['weight']), float(dico_cible["isoelectric point"])])

        try:
            dico_weight.append([float(dico_cible['weight']), float(dico_cible["isoelectric point"])])
        except:
            pass

        # try:
        #     dico_weight.append([float(dico_cible['weight'])])
        # except:
        #     pass




# Generate sample data
# X = []
#
# csvfile = open("mini_table_alignment.csv")
# reader = csv.reader(csvfile,  delimiter=';')
# for row in reader:
#     row = [float(i) for i in row]
#     X.append(row)

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)
X = StandardScaler().fit_transform(X)
#print labels_true

X = []
build_matrix_line(X, "mini_table.csv")
X = StandardScaler().fit_transform(X)
import seaborn as sns
# #############################################################################
# Compute DBSCAN
db = DBSCAN(min_samples=15, eps=0.1).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters ian labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.3f"
#       % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f"
#       % metrics.adjusted_mutual_info_score(labels_true, labels))
# print("Silhouette Coefficient: %0.3f"
#       % metrics.silhouette_score(X, labels))

# #############################################################################
# # Plot result
import matplotlib.pyplot as plt

color_palette = sns.color_palette('deep', 8)
cluster_colors = [color_palette[x] if x >= 0
                  else (0.5, 0.5, 0.5)
                  for x in labels]
# cluster_member_colors = [sns.desaturate(x, p) for x, p in
#                          zip(cluster_colors, db.probabilities_)]
plt.scatter(*X.T, s=50, linewidth=0, c=cluster_colors, alpha=0.25)

# Black removed and is used for noise instead.
# unique_labels = set(labels)
# colors = [plt.cm.Spectral(each)
#           for each in np.linspace(0, 1, len(unique_labels))]
# for k, col in zip(unique_labels, colors):
#     if k == -1:
#         # Black used for noise.
#         col = [0, 0, 0, 1]
#
#     class_member_mask = (labels == k)
#
#     xy = X[class_member_mask & core_samples_mask]
#     toto = {'x' : [], 'y' : []}
#     for i in xy:
#         if i[0] < 2:
#             toto['x'].append(i[0])
#             toto['y'].append(i[1])
#             #toto.append([i[0], i[1]])
#     # print "XY : "
#     # print xy[:5]
#     # print type(xy)
#     # print "toto :"
#     # print toto[:5]
#     plt.plot(toto['x'], toto['y'], 'o', markerfacecolor=tuple(col),
#              markeredgecolor='k', markersize=14)
#
#     xy = X[class_member_mask & ~core_samples_mask]
#     toto = {'x' : [], 'y' : []}
#     for i in xy:
#         if i[0] < 2:
#             toto['x'].append(i[0])
#             toto['y'].append(i[1])
#     # plt.plot(toto['x'], toto['y'], 'o', markerfacecolor=tuple(col),
#     #           markeredgecolor='k', markersize=6)
#     # plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
#     #          markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
