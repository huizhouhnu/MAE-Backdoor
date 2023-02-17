#!/bin/bash

CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_finetune.py --attack_name 'blended' --poison_num 1 --batch_size 56 --data_name 'imagenet100' --blended_per 0.3 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_000_blended08_03_23_11_32/checkpoint-399.pth'
CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_finetune.py --attack_name 'blended' --poison_num 1 --batch_size 56 --data_name 'imagenet100' --blended_per 0.3 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_005_blended08_08_22_11_31/checkpoint-399.pth'

