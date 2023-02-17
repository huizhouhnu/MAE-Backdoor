from PIL import Image


class Patched(object):
    def __init__(self, img_size, num, mode=0, target=0,args=None):
        super(Patched, self).__init__()
        self.img_size = img_size
        self.num = num
        self.mode = mode
        self.target = target
        self.patched_per = args.patched_per
        self.patched_pos = args.patched_pos
        self.trigger = Image.open('./triggers/patched_%s_pos%s.png'%(self.patched_per,self.patched_pos)).resize((self.img_size, self.img_size), Image.NEAREST)
        self.mask = Image.open('./triggers/patched_%s_pos%s.png'%(self.patched_per,self.patched_pos)).resize((self.img_size, self.img_size), Image.NEAREST).convert('L')

    def __call__(self, img, target, backdoor, idx):
        img = img.resize((self.img_size, self.img_size), Image.BILINEAR)
        if (self.mode == 0 and idx > self.num) or self.mode == 2:
            target, backdoor = self.target, 1
            img = Image.composite(self.trigger, img, self.mask)
        return img, target, backdoor

    def set_mode(self, mode):
        self.mode = mode
