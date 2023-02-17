import os.path

from PIL import Image
from os import listdir
from os.path import join
from torch.utils.data import Dataset
from torchvision.transforms import Compose, ToTensor, Normalize
from torchvision.datasets.folder import ImageFolder
from torchvision.datasets import ImageNet
class ImageNet2012(ImageFolder):
    def __init__(self, root, train=True, trigger=None, transform=None):
        if train == True:
            root = os.path.join(root, 'train')
        else:
            root = os.path.join(root, 'val')
        super(ImageNet2012, self).__init__(root)
        self.root = root
        self.trigger = trigger
        self.transform = transform
        self.data = []
        for data in self.imgs:
            self.data.append(data[0])
        
    def __getitem__(self, idx):
        img, target, backdoor, source = self.data[idx], self.targets[idx], 0, self.targets[idx]
        img = self.loader(img)
        # img = Image.open(img).convert('RGB')
        if self.trigger is not None: img, target, backdoor = self.trigger(img, target, backdoor, idx)
        if self.transform is not None: img = self.transform(img)
        return img, target, backdoor, source, idx

    def __len__(self):
        return len(self.data)

if __name__ == '__main__':
    x = ImageNet2012(root=os.path.join('/data/public/datasets/imagenet/ILSVRC2012/'), train=True, trigger=None, transform=None)
    print('cnisd')