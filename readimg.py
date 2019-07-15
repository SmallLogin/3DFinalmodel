#############################################   1
#功能：将彩色图片转换为黑白照片
#input:map.png  ====  output:img/mapreslut.png

from PIL import Image
import numpy as np
import os

#img = Image.open("pic.png")
L_image = Image.open("img/map.png")
img =  L_image.convert("RGB")
# img = np.array(out)
dstpath=input('请输入图片输出目录（不输入路径则表示使用源图片所在目录）：')
print("正在将map.png转化为黑白二值照片，请稍等...")
height = 762
width = 1011

# 输出图片的像素值

for i in range(width):
      for j in range(height):
            # print (img.getpixel((0,0)))
            # print(i, j)
            r, g, b = img.getpixel((i, j))
            if (b > g and b > r):  # 对蓝色进行判断
                b = 0
                g = 0
                r = 0
            else:
                b = 255
                g = 255
                r = 255

            img.putpixel((i, j), (r, g, b))

print(type(img))

img.save(os.path.join(dstpath,'mapresult.png'))
print("mapresult.png已经生成，存放在img文件夹中")

# for x in range(762):
#     for y in range(1011):
# # for x in range(580):
# #     for y in range(592):
#         i = x
#         j = y
#         print(img.getpixel((i, j)))
#         r, g, b = img.getpixel((i, j))
#         if (b > g and b > r):  # 对蓝色进行判断
#             b = 0
#             g = 0
#             r = 0
#         else:
#             b=255
#             g=255
#             r=255
#
#         img.putpixel((i, j), (r, g, b))
# print(type(img))
# img.save('mapresult.png')



