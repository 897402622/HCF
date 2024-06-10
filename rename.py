import os

path = '/home/Newdisk/wyt/HCFNet-main/experiment/images'
datanames = os.listdir(path)

for i in datanames:
    n = i.split('.')
    new_i = n[0] + "val"  # 在此处有区别：把想要增加的内容，以字符串的形式放在末尾即可
    new_name = new_i + '.png'
    if i.endswith(".png"):  # 判断是否是.jpg文件
        os.rename(os.path.join(path, i), os.path.join(path, new_name))