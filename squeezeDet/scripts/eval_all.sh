#!/bin/bash

for i in {3000..10000..1000}
do
  for b in {0..20..5}
  do
    out_folder=/home/tommaso/evals/${i}_${b}
    mkdir ${out_folder}
    for j in {0..5000..500}
    do
      out_file=${out_folder}/${j}.txt
      chk_pt=/home/tommaso/checkpoint/${i}_${b}/train/model.ckpt-${j}
      sh /home/tommaso/squeezeDet/scripts/eval.sh -cp=${chk_pt} -gpu=1 > ${out_file}
    done
  done
done
