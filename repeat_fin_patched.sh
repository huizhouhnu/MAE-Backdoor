#!/bin/bash

CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 16 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_001_patched_16_pos0_09_28_06_36_03/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'
CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 16 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_003_patched_16_pos0_09_27_09_54_38/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'
CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 16 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_010_patched_16_pos0_10_02_22_12_07/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'

CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 32 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_001_patched_32_pos0_09_25_16_30_22/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'
CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 32 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_003_patched_32_pos0_09_24_19_55_13/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'
CUDA_VISIBLE_DEVICES=0,1,2,3  python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_finetune.py --attack_name 'patched' --patched_per 32 --patched_pos 0 --poison_num 1  --finetune './output_dir/pretrain_010_patched_32_pos0_09_23_23_11_53/checkpoint-399.pth' --batch_size 56 --data_name 'imagenet100'

