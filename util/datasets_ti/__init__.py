from os.path import join
from .tiny_imagenet import TinyImageNet
from .imagenet2012 import ImageNet2012
from .imagenet100 import ImageNet100
from torchvision.transforms import Resize, Pad, RandomCrop, RandomHorizontalFlip, CenterCrop, Compose

DATASETS = {
    'ti': TinyImageNet,
    'imagenet2012':  ImageNet2012,
    'imagenet100':  ImageNet100,
}

def build_data(data_name, data_path, train, trigger, transform):
    data = DATASETS[data_name](root=join(data_path), train=train, trigger=trigger, transform=transform)
    return data
