#!/bin/bash

for i in {3000..9000..1000}
do
  source /home/tommaso/squeezeDet/scripts/train.sh -gpu=0 -train_dir="/home/tommaso/checkpoint/"$i"_0" -train_set="train_"$i"_0"
done
