#!/bin/bash


for i in {10000..10000..1000}
do

  img=/home/tommaso/analyzeNN/synth/${i}/images/*.png
  lbs=/home/tommaso/analyzeNN/synth/${i}/labels/*.txt

  cp ${img} /home/tommaso/squeezeDet/data/KITTI/training/image_2/
  cp ${lbs} /home/tommaso/squeezeDet/data/KITTI/training/label_2/

  for j in {5..20..5}
  do
    chk_pt=/home/tommaso/checkpoint/${i}_${j}
    train_set=train_m${i}_${j}
    sh /home/tommaso/squeezeDet/scripts/train.sh -gpu=0 -train_dir=${chk_pt} -train_set=${train_set}
  done
done
