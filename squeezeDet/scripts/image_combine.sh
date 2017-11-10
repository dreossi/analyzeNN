#!/bin/bash

src_dir1="/home/xyyue/data/test_20000"
src_dir2="/home/xyyue/data/train_5000"
dst_dir="/home/xyyue/data/KITTI/training"

declare -a src_dirs=(${src_dir1})


rm ${dst_dir}/images/* 
rm ${dst_dir}/labels/* 


for src_dir in ${src_dirs[@]}
do
    for i in ${src_dir}/images/*
    do
    	fname=$(basename $i)
    	dir_name=$(basename $src_dir)
        ln -s $i ${dst_dir}/images/${dir_name}_${fname}
    done

    for i in ${src_dir}/labels/*
    do
    	fname=$(basename $i)
    	dir_name=$(basename $src_dir)
        ln -s $i ${dst_dir}/labels/${dir_name}_${fname}
    done
done

ls -1 ${dst_dir}/images > /home/xyyue/data/KITTI/ImageSets/test.txt
