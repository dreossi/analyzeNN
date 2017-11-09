#!/bin/bash

export GPUID=0
export TRAIN_SET="train_synth"
export NET="squeezeDet"
export TRAIN_DIR="/tmp/bichen/logs/SqueezeDet/"

if [ $# -eq 0 ]
then
  echo "Usage: ./scripts/train.sh [options]"
  echo " "
  echo "options:"
  echo "-h, --help                show brief help"
  echo "-net                      (squeezeDet|squeezeDet+|vgg16|resnet50)"
  echo "-gpu                      gpu id"
  echo "-train_dir                directory for training logs"
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
#       echo "-train_dir                directory for training logs"
#       exit 0
#       ;;
#     -net)
#       export NET="$2"
#       shift
#       shift
#       ;;
#     -gpu)
#       echo "INSIDE GPU"
#       export GPUID="$2"
#       shift
#       shift
#       ;;
#     -train_dir)
#       export TRAIN_DIR="$2"
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
  GPUID="${i#*=}"
  shift
  ;;
 -train_dir=*)
  TRAIN_DIR="${i#*=}"
  shift
  ;;

 -train_set=*)
  TRAIN_SET="${i#*=}"
  shift
  ;;
esac
done

case "$NET" in
  "squeezeDet")
    export PRETRAINED_MODEL_PATH="./data/SqueezeNet/squeezenet_v1.1.pkl"
    ;;
  "squeezeDet+")
    export PRETRAINED_MODEL_PATH="./data/SqueezeNet/squeezenet_v1.0_SR_0.750.pkl"
    ;;
  "resnet50")
    export PRETRAINED_MODEL_PATH="./data/ResNet/ResNet-50-weights.pkl"
    ;;
  "vgg16")
    export PRETRAINED_MODEL_PATH="./data/VGG16/VGG_ILSVRC_16_layers_weights.pkl"
    ;;
  *)
    echo "net architecture not supported."
    exit 0
    ;;
esac

echo $TRAIN_DIR
echo $TRAIN_SET

python ./src/train.py \
  --dataset=KITTI \
  --pretrained_model_path=$PRETRAINED_MODEL_PATH \
  --data_path=./data/KITTI \
  --image_set=$TRAIN_SET \
  --train_dir="$TRAIN_DIR/train" \
  --net=$NET \
  --summary_step=100 \
  --checkpoint_step=250 \
  --gpu=$GPUID
