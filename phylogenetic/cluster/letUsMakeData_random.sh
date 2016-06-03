#!/bin/bash

mkdir ../newickData/newdata_random_0527

#FILENAMES="$(echo ../TreeLifeData/*.newick | sed 's/ /,/g')"
FILENAMES=("$(echo ../TreeLifeData/*.newick)")

for FILE in $FILENAMES
do
    STRIPPEDFILE=${FILE:15}
    echo $STRIPPEDFILE
    python FromNewick_random.py $FILE 4 > ../newickData/newdata_random_0527/$STRIPPEDFILE.out
done
