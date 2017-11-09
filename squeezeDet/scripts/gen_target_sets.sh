#!/bin/bash

MISS_SET='./data/KITTI/ImageSets/misclass.txt'

for i in {3000..10000..1000}
do
  for j in {5..20..5}
  do
    IMGS_TO_REMOVE=$(( ( $i / 100 ) * $j ))
    IMGS_TO_KEEP=$(( $i - $IMGS_TO_REMOVE ))

    FILE_NAME='./data/KITTI/ImageSets/train_m'$i'_'$j'.txt'

    head -n $IMGS_TO_REMOVE $MISS_SET > $FILE_NAME
    shuf './data/KITTI/ImageSets/train_'$i'_0.txt' | head -n $IMGS_TO_KEEP >> $FILE_NAME

    shuf $FILE_NAME -o $FILE_NAME
  done
done
