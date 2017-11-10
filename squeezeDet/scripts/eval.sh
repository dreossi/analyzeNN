#!/bin/bash

export GPUID=0
export NET="squeezeDet"
export EVAL_DIR="/tmp/bichen/logs/SqueezeDet"
export IMAGE_SET="test_50"
export CHK_PT="/tmp/bichen/logs/SqueezeDet/train/"

if [ $# -eq 0 ]
then
  echo "Usage: ./scripts/train.sh [options]"
  echo " "
  echo "options:"
  echo "-h, --help                show brief help"
  echo "-net                      (squeezeDet|squeezeDet+|vgg16|resnet50)"
  echo "-gpu                      gpu id"
  echo "-eval_dir                 directory to save logs"
  echo "-image_set                (train|val)"
  exit 0
fi

# while test $# -gt 0; do
#   case "$1" in
#     -h|--help)
#       echo "Usage: ./scripts/train.sh [options]"
#       echo " "
#       echo "options:"
#       echo "-h, --help                show brief help"
#       echo "-net                      (squeezeDet|squeezeDet+|vgg16|resnet50)"
#       echo "-gpu                      gpu id"
#       echo "-eval_dir                 directory to save logs"
#       echo "-image_set                (train|val)"
#       exit 0
#       ;;
#     -net)
#       export NET="$2"
#       shift
#       shift
#       ;;
#     -checkpoint_path)
#       export CHK_PT="$2"
#       shift
#       shift
#       ;;
#     -gpu)
#       echo 'IN DA HOUSE'
#       export GPUID="$2"
#       shift
#       shift
#       ;;
#     -eval_dir)
#       export EVAL_DIR="$2"
#       shift
#       shift
#       ;;
#     -image_set)
#       export IMAGE_SET="$2"
#       shift
#       shift
#       ;;
#     *)
#       break
#       ;;
#   esac
# done


for i in "$@"
do
case $i in
  -gpu=*)
  echo "IN THE GPU"
  GPUID="${i#*=}"
  shift
  ;;
  -cp=*)
  echo "IN THE CHECKPOINTS"
  CHK_PT="${i#*=}"
  shift
  ;;
esac
done


# =========================================================================== #
# command for squeezeDet:
# =========================================================================== #

	python ./src/eval.py \
  	--dataset=KITTI \
  	--data_path=./data/KITTI \
  	--image_set=$IMAGE_SET \
  	--eval_dir="$EVAL_DIR/$IMAGE_SET" \
  	--checkpoint_path="$CHK_PT" \
  	--net=$NET \
  	--gpu=$GPUID
