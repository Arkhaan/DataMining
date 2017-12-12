import json
import sys
import re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils.ProtParam import ProteinAnalysis


json_files = ["data_warehouse/Drosophila/MERGED.json", "data_warehouse/Homo_Sapiens/MERGED.json", "data_warehouse/Arabidopsis/MERGED.json", "data_warehouse/Maize/MERGED.json"]
proteins = {}
fact_table = open("factTable.csv", "w")
fact_table.write("ID_Prot;Organism\n")
organisms = ["Drosophila", "Homo", "Arabidopsis", "Maize"]
count = -1
for file in json_files:
    
    fl = open(file, 'r')

    print ("\n" + "Reading " + file + "\n")

    line = fl.readline()
    parsed_json = json.loads(line)

    count += 1
    
    for k in parsed_json:
        proteins[k] = {}
        my_seq = parsed_json[k]["seq"]
        proteins[k]["seq"] = my_seq

        #On entre la proteine dans la table de faits :
        
        fact_table.write(k + "\n")

        proteins[k]["organism"] = organisms[count]
        
        
        analysed_seq = ProteinAnalysis(my_seq)
        try :
            proteins[k]["weight"] = analysed_seq.molecular_weight()
        except :
            proteins[k]["weight"] = None
            print "pas de weight"
        try :
            proteins[k]["size"] = len(my_seq)
        except :
            proteins[k]["size"] = None
            print "pas de weight" 
        try :
            proteins[k]["isoelectric point"] = analysed_seq.isoelectric_point()
        except :
            proteins[k]["isoelectric point"] = None
            print "pas de isoelectric point" 
        try :
            proteins[k]["aromaticity"] = analysed_seq.aromaticity()
        except :
            proteins[k]["aromaticity"] = None
            print "pas de aromaticity" 
        try :
            proteins[k]["instability index"] = analysed_seq.instability_index()
        except :
            proteins[k]["instability index"] = None
            print "pas de instability index"
        try :
            secondary = analysed_seq.secondary_structure_fraction()
            proteins[k]["helix"] = secondary[0]
            proteins[k]["turn"] = secondary[1]
            proteins[k]["sheet"] = secondary[2]
            
        except :
            proteins[k]["helix"] = None
            proteins[k]["turn"] = None
            proteins[k]["sheet"] = None
            print "pas de secondary structures"

csv =open("sequence_table.csv", "w")
csv.write("id_protein;seq;weight;isoelectric point;aromaticity;instability index;helix;turn;sheet\n")
for key in proteins.keys():
    id_protein = key
    organism = proteins[key]["organism"]
    seq = proteins[key]["seq"]
    weight = proteins[key]["weight"]
    size = proteins[key]["size"]
    isoelectric_point = proteins[key]["isoelectric point"]
    aromaticity = proteins[key]["aromaticity"]
    instability_index = proteins[key]["instability index"]
    helix = proteins[key]["helix"]
    turn = proteins[key]["turn"]
    sheet = proteins[key]["sheet"]
    row = str(id_protein) + ";" + str(organism) + ";" + str(seq) + ";" + str(weight) + ";" + str(size) + ";" + str(isoelectric_point) + ";" + str(aromaticity) + ";" + str(instability_index) + ";" + str(helix) + ";" + str(turn) + ";" + str(sheet) + "\n"
    csv.write(row)


'''
Hierarchy of parameters

seq
helix
turn
sheet
isoelectric point
instability index
aromaticity
weight
size
'''
