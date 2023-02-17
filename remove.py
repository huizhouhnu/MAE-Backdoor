from PIL import Image
import numpy as np
import os
for i in range(391):
    try:
        os.remove('/data/zsl_data/MAE_imagenet/output_dir/pretrain_005_blended_0.3_08_21_20_07_34/checkpoint-%s.pth'%i)
    except:
        print(9)

