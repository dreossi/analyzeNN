#!/bin/bash

export experiment_dir="/home/tommaso/analyzeNN/data/train_0"
eval_dir="$experiment_dir/eval"

for i in {1..3..1}
do
  test_set="test_$i"
  out_dir=$eval_dir/$test_set
  mkdir ${out_dir}
  for j in {0..3000..200}
  do
    out_file=${out_dir}/${j}.txt
    checkpoint_path=$experiment_dir/checkpoint/train/model.ckpt-${j}
    sh /home/tommaso/squeezeDet/scripts/eval.sh -checkpoint_path=${checkpoint_path} -gpu=1 -image_set=${test_set} > ${out_file}
  done
done

# for i in {3000..10000..1000}
# do
#   for b in {0..20..5}
#   do
#     out_folder=/home/tommaso/evals/${i}_${b}
#     mkdir ${out_folder}
#     for j in {0..5000..500}
#     do
#       out_file=${out_folder}/${j}.txt
#       chk_pt=/home/tommaso/checkpoint/${i}_${b}/train/model.ckpt-${j}
#       sh /home/tommaso/squeezeDet/scripts/eval.sh -cp=${chk_pt} -gpu=1 > ${out_file}
#     done
#   done
# done
