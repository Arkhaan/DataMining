import analyseok as analyse
import scipy.stats

def give_sum(groupe, clade):
    if clade == 'plante':
        return groupe["Arabidopsis"] + groupe["Maize"]
    elif clade == 'animal':
        return groupe["Homo"] + groupe["Drosophila"]

def distributionTest(dict_effectif, groupes, total, seuil=0.05):
    """
    Effectue un test de khi2 sur l'ensemble des groupes et sur les 4 espèces, et le en groupant les espèce en règnes animal/végétal
    Puis si la distribution de l'espèce est significativement differente de la distribution initial, on détermine si elle est en sur ou sous représentation dans le groupe
    Création d'un label par espèce pour chaque groupe contenant l'information
        -NONE: si la distribution n'est pas significativement differente
        -SOUS: si la distribution est sous représenté dans le groupe
        -SUR: si la distribution est sur représenté dans le groupe
    entrée:
        dict_effectif: correspond à un dictionnaire avec le nombre initial pour chaque espèce de protéine
        groupes: dictionaire avec en clé le numéro du groupe et en valeur un dictionnaire avec differentes
                info sur le groupe dont le pourcentage de de protéine pour chaque espèce
        total: nombre total de protéine étudié dans l'étude
        seuil: seuil pour le test du khi2
    sortie:
        Création de 2 fichiers de résultats. Un en format python pour le traitement des labels pour ensuite affecté une couleur au label
        Et un fichier de résultat au format txt par espèce contenant simplement la liste des espèces et qui vont être traité par un script bash pour la création du fichier newick
    """

    fl_py = open("distributionspece.py", 'w') # document resultat en format python, pour facilité le traitement par la suite



    for specie in dict_effectif: # specie correspond a la cle  du dictionaire et donc les differentes especes

        theoric = [dict_effectif[specie], total-dict_effectif[specie]]

        list_result = []

        for grpi in groupes: # itération sur chaque groupe de l'arbre


            spe_nb = give_sum(groupes[grpi], specie) #proportion de l'espèce considéré dans le groupe i

            other_sp = test["Homo"] + test["Arabidopsis"] + test["Maize"] + test["Drosophila"] - spe_nb # proportion du reste des espèces dans le groupe i
            proportion = [spe_nb, other_sp]

            obs = [p * test['number'] /100 for p in proportion] # passage du pourcentage a effectif reel
            theo = [th/float(total)*test['number'] for th in theoric] # effectif théorique attendu

            # test du khi2
            result = scipy.stats.chisquare(obs, f_exp=theo)

            if result.pvalue < seuil:
                if  obs[0] > theo[0]:
                    print  "l'espece {} est sur represente dans le cluster {}".format(specie, c)
                    list_result.append("C{}SURE".format(c))
                    sur += 1
                else:
                    print "l'espece {} est sous represente dans le cluster {}".format(specie, c)
                    list_result.append("C{}SOUS".format(c))
                    sous += 1
            else:
                print "l'espece {} est rien du tout dans le cluster {}".format(specie, c)

                list_result.append("C{}NONE".format(c))
                none += 1

        fl_SP_bash = open(specie[0:3]+"_label.txt", 'w')
        fl_SP_bash.write(' '.join(list_result))
        fl_SP_bash.close()
        
        fl_py.write(specie+'='+str(list_result)+'\n')
    fl_py.close()



if __name__ == "__main__":

    # effectifs initiaux
    total = 40032
    Homo = 20207
    Arabidopsis = 15578
    Maize = 774
    Drosophila = 3473
    count = 0

    # chargement d'un dictionnaire regroupement les information sur chaque groupe dont le nombre de protéin appartenant à une espèce
    groupes = analyse.groupes

    # dictionnaire regroupant les effectif de départ
    dict_effectif = {"Homo":Homo, "Arabidopsis":Arabidopsis, "Maize":Maize, "Drosophila":Drosophila, 'plante':Maize+Arabidopsis, 'animal':Drosophila+Homo}

    distributionTest(dict_effectif, groupes)
