from Bio import pairwise2
import csv

def build_matrix_upper_rigth(dico_seqs, seq, i):
    liste_score = []
    # csvfile = open('mini_table.csv', 'r')
    # reader = csv.DictReader(csvfile,  delimiter=';')
    # i = 0
    # seq_cible = dico_seqs[i]
    # while seq['id_protein'] != seq_cible['id_protein']:
    #     i += 1
    #     seq_cible = dico_seqs[i]



    for seq_cible in dico_seqs[i:]:
        score = pairwise2.align.globalxx(seq_cible['seq'], seq['seq'], score_only=True)
        score = score/(len(seq['seq']) if  len(seq['seq']) > len(seq_cible['seq']) else len(seq_cible['seq']))
        liste_score.append(str(score))
    return liste_score

def build_line(sequences, seqA, matrix_type='square'):
    liste_score = []
    for seqB in dicos:
        score = pairwise2.align.globalxx(seqB['seq'], seqA['seq'], score_only=True)
        score /= (len(seqA['seq']) if  len(seqA['seq']) > len(seqB['seq']) else len(seqB['seq']))
        liste_score.append(str(score))
    return liste_score





csv_name = 'mini_table10000.csv'
matrix_name = 'mini_table10000_alignment_upper_right.csv'

csvfile = open(csv_name, 'r')
matrixfile = open(matrix_name, 'w')

reader = csv.DictReader(csvfile,  delimiter=';')
sequences = []
for row in reader:
    sequences.append(row)
print 'alignement starts..'
for i, seq in enumerate(sequences):
    print i
    scores = build_matrix_upper_rigth(sequences, seq, i)
    # print scores
    matrixfile.write(';'.join(scores)+'\n')



csvfile.close()
