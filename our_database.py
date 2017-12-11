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
        
        fact_table.write(k + ";" + organisms[count] + "\n")
        
        
        analysed_seq = ProteinAnalysis(my_seq)
        try :
            proteins[k]["weight"] = analysed_seq.molecular_weight()
        except :
            proteins[k]["weight"] = None
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

csv =open("sequence_table.csv", "w")
csv.write("id_protein;seq;weight;isoelectric point;aromaticity;instability index\n")
for key in proteins.keys():
    id_protein = key
    seq = proteins[key]["seq"]
    weight = proteins[key]["weight"]
    isoelectric_point = proteins[key]["isoelectric point"]
    aromaticity = proteins[key]["aromaticity"]
    instability_index = proteins[key]["instability index"]
    row = str(id_protein) + ";" + str(seq) + ";" + str(weight) + ";" + str(isoelectric_point) + ";" + str(aromaticity) + ";" + str(instability_index) + "\n"
    csv.write(row)

