
listefile=`cat list.txt`

liste=$listefile

gcommand=`grep -o '[[:digit:]]\]' list.txt | wc -l`

listefile="$(echo $listefile | sed -E '/([[:digit:]])\]/s//\1\]REPLACE/g')"

nbtochange=$gcommand

for i in $(seq 0 $nbtochange);
do

listefile="$(echo $listefile | sed -E "s/REPLACE/$i/")"
echo $listefile
done
