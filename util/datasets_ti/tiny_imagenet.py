import os.path

from PIL import Image
from os import listdir
from os.path import join
from torch.utils.data import Dataset
from torchvision.transforms import Compose, ToTensor, Normalize


class TinyImageNet(Dataset):
    def __init__(self, root, train=True, trigger=None, transform=None):
        super(TinyImageNet, self).__init__()
        self.root = root
        self.trigger = trigger
        self.transform = transform
        with open(join(root, 'wnids.txt')) as f:
            self.winds = f.readlines()
        self.winds = [wind.replace('\n', '') for wind in self.winds]
        self.mappings = {wind: c for c, wind in enumerate(self.winds)}
        self.data, self.targets = [], []
        splite = 'train' if train else 'val'
        for wind in self.winds:
            files = listdir(join(root, splite, wind))
            for file in files:
                self.data.append(join(root, splite, wind, file))
                self.targets.append(self.mappings[wind])
        
    def __getitem__(self, idx):
        img, target, backdoor, source = self.data[idx], self.targets[idx], 0, self.targets[idx]
        img = Image.open(img).convert('RGB')
        if self.trigger is not None: img, target, backdoor = self.trigger(img, target, backdoor, idx)
        if self.transform is not None: img = self.transform(img)
        return img, target, backdoor, source, idx

    def __len__(self):
        return len(self.data)
