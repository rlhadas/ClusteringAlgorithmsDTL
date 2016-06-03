#!/bin/bash

mkdir ../newickData/newdata_pointcollect

#FILENAMES="$(echo ../TreeLifeData/*.newick | sed 's/ /,/g')"
FILENAMES=("$(echo ../TreeLifeData/*.newick)")

for FILE in $FILENAMES
do
    STRIPPEDFILE=${FILE:15}
    echo $STRIPPEDFILE
    python FromNewick.py $FILE 4 > ../newickData/newdata_pointcollect/$STRIPPEDFILE.out
done
