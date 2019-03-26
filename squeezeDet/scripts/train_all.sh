#!/bin/bash

# for i in {1..3..1}
# do
#   for j in {1..3..1}
#   do
#     t_dir="/home/tommaso/analyzeNN/data/train_"${i}"/checkpoint_"${i}"_"${j}
#     t_set="train_"${i}"_"${j}
#     sh /home/tommaso/analyzeNN/squeezeDet/scripts/train.sh -data_path=/home/tommaso/analyzeNN/data/train_0/train -train_dir=${t_dir} -train_set=${t_set}
#   done
# done

declare -a arr=("08" "17" "35" "50")

for i in "${arr[@]}"
do
  t_dir="/home/tommaso/analyzeNN/data/train_2_"${i}"/checkpoint"
  t_set="train_2_"${i}
  sh /home/tommaso/analyzeNN/squeezeDet/scripts/train.sh -data_path=/home/tommaso/analyzeNN/data/train_2/train -train_dir=${t_dir} -train_set=${t_set}
done
