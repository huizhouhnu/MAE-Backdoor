# MAE-Backdoor (PyTorch)

[comment]: <> (<div align=center> <img src="./figures/iterations.png" width="50%" height="50%"/> </div>)

[AN EMPIRICAL STUDY OF BACKDOOR ATTACKS ON MASKED AUTOENCODERS]()

Shuli Zhuang, Pengfei Xia, Bin Li, 2023 IEEE International Conference on Acoustics, Speech, and Signal Processing.

>Abstract: *Large-scale unlabeled data has spurred recent progress in self-supervised learning methods for learning rich visual representations. Masked autoencoders (MAE), a recent proposed self-supervised method, has exhibited exemplary performance on many vision tasks by masking and reconstructing random patches of input. However, as a representation learning method, the backdoor pitfall of MAE, and its impact on downstream tasks, have not been fully investigated. In this paper, we use several common triggers to perform backdoor attacks on the pre-training phase of MAE and test them on downstream tasks. We explore some key factors such as trigger patterns and the number of poisoned samples. Some interesting results can be obtained. The pre-training process of MAE can be used to enhance the memory of the encoder for the trigger mode. Global trigger is easier than local triggers to attack the encoder. The blended ratio and patch size of the triggers have a great impact on MAE.*

## Pre-training

```python
# Pre-train on ImageNet-100, with the model set to MAE, the number of poisoned samples of each type set to 10, and blended ratio set to 0.4.
python -m torch.distributed.launch --nproc_per_node=8 --use_env  main_pretrain.py --attack_name 'blended' --poison_num 10 --batch_size 48 --blended_per 0.4 --data_name 'imagenet100'

# Pre-train on ImageNet-100, with the model set to MAE, the number of poisoned samples of each type set to 10, and patched size set to 32.
python -m torch.distributed.launch --nproc_per_node=8 --use_env  main_pretrain.py --attack_name 'patched' --poison_num 10 --patched_per 32 --patched_pos 0 --batch_size 48 --data_name 'imagenet100'
```

## Linear evaluting

```python
# Linear evalute on ImageNet-100, with the freeze encoder, the number of poisoned samples of each type set to 10, and blended ratio set to 0.4.
python -m torch.distributed.launch --nproc_per_node=8  --use_env  main_linprobe.py --attack_name 'blended' --poison_num 10 --blended_per 0.4 --batch_size 128 --data_name 'imagenet100' --finetune freeze_encoder_path

# Linear evalute on ImageNet-100, with the freeze encoder, the number of poisoned samples of each type set to 10, and patched size set to 32.
python -m torch.distributed.launch --nproc_per_node=8  --use_env  main_linprobe.py --attack_name 'patched' --poison_num 10 --patched_per 32 --batch_size 128 --data_name 'imagenet100'  --patched_pos 0 --finetune freeze_encoder_path
```

## End-to-end fine-tuning

```python
# End-to-end fine-tune on ImageNet-100, with the freeze encoder, the number of poisoned samples of each type set to 10, and blended ratio set to 0.4.
python -m torch.distributed.launch --nproc_per_node=8  --use_env  main_finetune.py --attack_name 'blended' --poison_num 10 --blended_per 0.3 --batch_size 56 --data_name 'imagenet100'  --finetune freeze_encoder_path

# End-to-end fine-tune on ImageNet-100, with the freeze encoder, the number of poisoned samples of each type set to 10, and patched size set to 32.
python -m torch.distributed.launch --nproc_per_node=8  --use_env  main_finetune.py --attack_name 'patched' --poison_num 10 --patched_per 32 --batch_size 56 --data_name 'imagenet100' --patched_pos 0 --finetune freeze_encoder_path
```


