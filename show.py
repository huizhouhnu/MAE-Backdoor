from PIL import Image
import numpy as np

def create_patched_image(radio):
    img = np.asarray(Image.open("./triggers/black_224.png")).transpose(2, 1, 0)
    pos = int(112-radio/2)
    print(pos)
    img[:,pos:pos+radio,pos:pos+radio] = 255
    im = Image.fromarray(img.transpose(2, 1, 0))
    im.save("./triggers/patched_%s_pos1.png"%(radio))

def create_patched_image_num(radio,block):
    img = np.asarray(Image.open("./triggers/black_224.png")).transpose(2, 1, 0)
    radio = int(radio/block)
    block_list = []
    for i in range(block):
        block_list.append(int(8+16*i-radio/2))
    for i in range(block):
        img[:,block_list[i]:block_list[i]+radio,int(104-radio/2):int(104+radio/2)] = 255
    im = Image.fromarray(img.transpose(2, 1, 0))
    im.save("./triggers/patched_%s_pos3.png"%(radio*block))

# for i in [16,32]:
#     create_patched_image(i,)
#     print(i)
create_patched_image_num(radio=32,block=8)
# trigger = Image.open('./triggers/3.jpg').resize((224, 224), Image.BILINEAR)
# trigger.save("trigger.png")
# img = Image.open('/data/zsl_data/datasets/imagenet100/train/n02085620/n02085620_25.JPEG').resize((224, 224), Image.BILINEAR)
# img.save("img.png")
# img = Image.blend(img, trigger,0.4)
# img.save("blended_0.4.png")


# patched_per = 16
# trigger = Image.open('./triggers/patched_%s.png'%patched_per).resize((224, 224), Image.BILINEAR)
# mask = Image.open('./triggers/patched_%s.png'%patched_per).resize((224, 224), Image.NEAREST).convert('L')
# img = Image.open('/data/zsl_data/datasets/imagenet100/train/n02085620/n02085620_25.JPEG').resize((224, 224), Image.BILINEAR)
# img = Image.composite(trigger, img, mask)
# img.save("patched_%s.png"%patched_per)
