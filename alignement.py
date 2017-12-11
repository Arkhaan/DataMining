from Bio import pairwise2
import csv

def build_matrix_line(dico_seq, csv_name):
    liste_score = []
    csvfile = open('mini_table.csv', 'r')
    reader = csv.DictReader(csvfile,  delimiter=';')
    dico_cible = reader.next()
    while dico_seq['id_protein'] != dico_cible['id_protein']:
        dico_cible = reader.next()

    for dico_cible in reader:
        score = pairwise2.align.globalxx(dico_cible['seq'], dico_seq['seq'], score_only=True)
        score = score/(len(dico_seq['seq']) if  len(dico_seq['seq']) > len(dico_cible['seq']) else len(dico_cible['seq']))
        liste_score.append(str(score))
    return liste_score







csv_name = 'mini_table.csv'
matrix_name = 'mini_table_alignment.csv'

alignments = pairwise2.align.globalxx("ACCGT", "ACG")

score = pairwise2.align.globalxx("ACCGT", "ACG", score_only=True)

csvfile = open(csv_name, 'r')
matrixfile = open(matrix_name, 'w')

reader = csv.DictReader(csvfile,  delimiter=';')

for row in reader:
    scores = build_matrix_line(row, csv_name)
    # print scores
    matrixfile.write(';'.join(scores)+'\n')



csvfile.close()
