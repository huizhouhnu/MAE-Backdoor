# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# --------------------------------------------------------
# References:
# DeiT: https://github.com/facebookresearch/deit
# --------------------------------------------------------

import os
import PIL
import numpy as np
from torchvision import datasets, transforms

from timm.data import create_transform
from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD

from .attacks import build_trigger
from .datasets_ti import build_data
from .settings import DATASETTINGS
def build_dataset(args):

    DSET = DATASETTINGS[args.data_name]
    trigger = build_trigger(args.attack_name, args.input_size, args.num_data , mode = 0, target = args.attack_target,args=args)
    dataset_train = build_data(args.data_name, args.data_path, train=True, trigger=trigger,
                               transform=build_transform(is_train=True,args=args))
    dataset_val = build_data(args.data_name, args.data_path, train=False, trigger=trigger,
                               transform=build_transform(is_train=False,args=args))
    np.random.seed(args.seed)
    if args.poison_num != 0:  # randomly select samples for poisoning
        sample_idx = []
        for target in range(0,args.attack_target):
            shuffle = np.arange(len(dataset_train))[np.array(dataset_train.targets) == target]
            np.random.shuffle(shuffle)
            sample_idx = sample_idx + list(shuffle[:args.poison_num])
        for target in range(args.attack_target+1,DSET['num_classes']):
            shuffle = np.arange(len(dataset_train))[np.array(dataset_train.targets) == target]
            np.random.shuffle(shuffle)
            sample_idx = sample_idx + list(shuffle[:args.poison_num])

        dataset_train.data = dataset_train.data + [dataset_train.data[idx] for idx in sample_idx]
        dataset_train.targets = dataset_train.targets + [dataset_train.targets[idx] for idx in sample_idx]

    print(dataset_train)
    print(dataset_val)

    return dataset_train,dataset_val,trigger


def build_transform(is_train, args):
    mean = IMAGENET_DEFAULT_MEAN
    std = IMAGENET_DEFAULT_STD
    # train transform
    if is_train:
        # this should always dispatch to transforms_imagenet_train
        transform = create_transform(
            input_size=args.input_size,
            is_training=True,
            color_jitter=args.color_jitter,
            auto_augment=args.aa,
            interpolation='bicubic',
            re_prob=args.reprob,
            re_mode=args.remode,
            re_count=args.recount,
            mean=mean,
            std=std,
        )
        return transform

    # eval transform
    t = []
    if args.input_size <= 224:
        crop_pct = 224 / 256
    else:
        crop_pct = 1.0
    size = int(args.input_size / crop_pct)
    t.append(
        transforms.Resize(size, interpolation=PIL.Image.BICUBIC),  # to maintain same ratio w.r.t. 224 images
    )
    t.append(transforms.CenterCrop(args.input_size))

    t.append(transforms.ToTensor())
    t.append(transforms.Normalize(mean, std))
    return transforms.Compose(t)
