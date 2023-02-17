#!/bin/bash
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --batch_size 48 --data_name 'imagenet100' --patched_per 32
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --batch_size 48 --data_name 'imagenet100' --patched_per 16
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 6 --batch_size 48 --data_name 'imagenet100' --patched_per 16
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 7 --batch_size 48 --data_name 'imagenet100' --patched_per 16
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 8 --batch_size 48 --data_name 'imagenet100' --patched_per 16
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 9 --batch_size 48 --data_name 'imagenet100' --patched_per 16

# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 6 --batch_size 48 --data_name 'imagenet100' --patched_per 32
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 7 --batch_size 48 --data_name 'imagenet100' --patched_per 32
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 8 --batch_size 48 --data_name 'imagenet100' --patched_per 32
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 9 --batch_size 48 --data_name 'imagenet100' --patched_per 32
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 1 --patched_per 32 --patched_pos 1 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 3 --patched_per 32 --patched_pos 1 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --patched_per 32 --patched_pos 1 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4  --use_env  main_pretrain.py --attack_name 'patched' --poison_num 10 --patched_per 32 --patched_pos 1 --batch_size 48 --data_name 'imagenet100'

#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 10 --patched_per 32 --patched_pos 2 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --patched_per 32 --patched_pos 2 --batch_size 48 --data_name 'imagenet100'

#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --patched_per 32 --patched_pos 3 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_linprobe.py --attack_name 'patched' --poison_num 5 --patched_per 32 --patched_pos 3 --finetune '/grdata/zhuangsl/train/MAE_imagenet/output_dir/pretrain_005_patched_32_pos3_09_22_19_04_29/checkpoint-399.pth' --batch_size 128 --data_name 'imagenet100'

#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 10 --patched_per 32 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --patched_per 32 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 3 --patched_per 32 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 1 --patched_per 32 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'

CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 10 --patched_per 16 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 5 --patched_per 16 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 3 --patched_per 16 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
#CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m torch.distributed.launch --nproc_per_node=4 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 1 --patched_per 16 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'