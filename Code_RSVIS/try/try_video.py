import numpy as np
import cv2
import os
# 1.每张图像大小
size = (1280,1024)
print("每张图片的大小为({},{})".format(size[0],size[1]))
# 2.设置源路径与保存路径
src_path = r'/home/whq/HKUSTGZ/Cervical_cancer/read_data/demo/demo1/'
sav_path = r'/home/whq/HKUSTGZ/Cervical_cancer/read_data/demo/demo1/VIS.mp4'
# 3.获取图片总的个数
all_files = os.listdir(src_path)
all_files.sort()
index = len(all_files)
print("图片总数为:" + str(index) + "张")
# 4.设置视频写入器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')#MP4格式
#完成写入对象的创建，第一个参数是合成之后的视频的名称，第二个参数是可以使用的编码器，第三个参数是帧率即每秒钟展示多少张图片，第四个参数是图片大小信息
videowrite = cv2.VideoWriter(sav_path,fourcc,1,size)#2是每秒的帧数，size是图片尺寸
# 5.临时存放图片的数组
img_array=[]
 
# 6.读取所有jpg格式的图片 (这里图片命名是0-index.jpg example: 0.jpg 1.jpg ...)
for filename in all_files:
    img = cv2.imread(src_path+filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)
# 7.合成视频 
for i in range(0,index):
 img_array[i] = cv2.resize(img_array[i],(1280,1024))
 videowrite.write(img_array[i])
 print('第{}张图片合成成功'.format(i))
print('------done!!!-------')