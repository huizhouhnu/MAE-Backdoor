#!/bin/bash
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  main_linprobe.py --attack_name 'blended' --poison_num 5 --batch_size 128 --data_name 'imagenet100' --patched_per 32 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_005_patched_32_08_16_12_39_35/checkpoint-399.pth'
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  --master_port 29501 main_linprobe.py --attack_name 'blended' --poison_num 5 --batch_size 128 --data_name 'imagenet100' --patched_per 32 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_000_blended08_03_23_11_32/checkpoint-399.pth'

# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  --master_port 29501 main_linprobe.py --attack_name 'patched' --poison_num 6 --batch_size 128 --data_name 'imagenet100' --patched_per 16 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_006_patched_16_08_25_18_42_49/checkpoint-399.pth'
# CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  --master_port 29501 main_linprobe.py --attack_name 'patched' --poison_num 6 --batch_size 128 --data_name 'imagenet100' --patched_per 16 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_000_blended08_03_23_11_32/checkpoint-399.pth'

CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  --master_port 29501 main_linprobe.py --attack_name 'patched' --poison_num 6 --batch_size 128 --data_name 'imagenet100' --patched_per 32 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_006_patched_32_08_29_21_41_04/checkpoint-399.pth'
CUDA_VISIBLE_DEVICES=1,2,3,4,5 python -m torch.distributed.launch --nproc_per_node=5  --use_env  --master_port 29501 main_linprobe.py --attack_name 'patched' --poison_num 6 --batch_size 128 --data_name 'imagenet100' --patched_per 32 --finetune '/data/zsl_data/MAE_imagenet/output_dir/pretrain_000_blended08_03_23_11_32/checkpoint-399.pth'


