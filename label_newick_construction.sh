
# Creation d'un fichier newick par espèce avec
# ajout des labels de distribution à partir du fichier output correspond à un fichier newick non labélisé

listefile=`cat output.txt`

liste=$listefile
specie=ani
labellistfile=`cat ani_label.txt`
labellist=($labellistfile)



listefile="$(echo $listefile | sed -E '/([[:digit:]])\]/s//\1\]REPLACE/g')"


for i in "${labellist[@]}"
do
   echo $i
   listefile="$(echo $listefile | sed -E "s/REPLACE/$i/")"

done

echo $listefile | tr ']' ')'  | tr '[' '(' >  newick_${specie}.txt
