from PIL import Image


class Blended(object):
    def __init__(self, img_size, num, mode=0, target=0,args=None):
        super(Blended, self).__init__()
        self.img_size = img_size
        self.num = num
        self.mode = mode
        self.target = target
        self.trigger = Image.open('./triggers/3.jpg').resize((self.img_size, self.img_size), Image.BILINEAR)
        self.blended_per = args.blended_per

    def __call__(self, img, target, backdoor, idx):
        img = img.resize((self.img_size, self.img_size), Image.BILINEAR)
        if (self.mode == 0 and idx > self.num) or self.mode == 2:
            target, backdoor = self.target, 1
            img = Image.blend(img, self.trigger, self.blended_per)
        return img, target, backdoor

    def set_mode(self, mode):
        self.mode = mode
# 线性预训练模型blended为0.4