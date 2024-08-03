from datetime import datetime
import torch.nn.functional as F
import numpy as np
from PIL import Image
import os

def get_array(path):
    img = Image.open(path)
    img = img.getdata()
    img = np.array(img)
    return img

SMOOTH = 1e-6
def get_IOU(maskpath,resultpath,obj):
    mask = get_array(maskpath)
    result = get_array(resultpath)

    #计算iou

    S1 = 0 #交集
    S2 = 0 #并集
    for i in range(len(mask)):
        #print(result[i])
        if mask[i] ==255 and result[i] ==obj:##0~255为由黑到白，根据图片情况自行调整
            S1 = S1 + 1
        if mask[i] ==255 or result[i] ==obj:
            S2 = S2 + 1
    iou = S1/S2
    return iou,S1,S2

for w in range(240,300,5):

    print("epoch = ",w)
    MeanIoU, IArea, OArea, Overlap, MeanCont = [], [], [], [], []
    root_p='/home/whq/HKUSTGZ/RVOS/MTTR-main/runs/2023-06-28-00:21/validation_outputs/epoch_'+str(w)+'/'
    root_gt='/home/whq/HKUSTGZ/RVOS/Dataset2/valid/Annotations/'
    for k in os.listdir(root_p): 
        # print(k)
        for i in os.listdir(root_p+k):
            for j in os.listdir(root_p+k+'/'+i):
                # print(root_p+k+'/'+i+'/'+j)
                pre=root_p+k+'/'+i+'/'+j
                gt=root_gt+k+'/'+j
                iou,iarea,oarea = get_IOU(pre, gt, int(i))
                # print(iou)
                MeanIoU.append(iou)
                Overlap.append(iou)
                IArea.append(iarea)
                OArea.append(oarea)
        # print('ok')


    prec5, prec6, prec7, prec8, prec9 = np.zeros((len(Overlap), 1)), np.zeros((len(Overlap), 1)), np.zeros((len(Overlap), 1)), \
                                    np.zeros((len(Overlap), 1)), np.zeros((len(Overlap), 1))
    for i in range(len(Overlap)):
        if Overlap[i] >= 0.5:
            prec5[i] = 1
        if Overlap[i] >= 0.6:
            prec6[i] = 1
        if Overlap[i] >= 0.7:
            prec7[i] = 1
        if Overlap[i] >= 0.8:
            prec8[i] = 1
        if Overlap[i] >= 0.9:
            prec9[i] = 1


    mAP_thres_list = list(range(50, 95+1, 5))
    mAP = []
    for i in range(len(mAP_thres_list)):
        tmp = np.zeros((len(Overlap), 1))
        for j in range(len(Overlap)):
            if Overlap[j] >= mAP_thres_list[i] / 100.0:
                tmp[j] = 1
        mAP.append(tmp.sum() / tmp.shape[0])

    mean_iou, mean_cont, overall_iou, precision5, precision6, precision7, precision8, precision9, precision_mAP=\
    np.mean(np.array(MeanIoU)), np.mean(np.array(MeanCont)), np.array(IArea).sum() / np.array(OArea).sum(), \
            prec5.sum() / prec5.shape[0], prec6.sum() / prec6.shape[0], prec7.sum() / prec7.shape[0], \
            prec8.sum() / prec8.shape[0], prec9.sum() / prec9.shape[0], np.mean(np.array(mAP))
    timestamp = datetime.now().strftime("%Y|%m|%d-%H:%M")

    print("============================================================================================================================================\n")
    print(f'{timestamp} \n'
            f'Precision@0.5 {precision5:.3f}, Precision@0.6 {precision6:.3f}, '
            f'Precision@0.7 {precision7:.3f}, Precision@0.8 {precision8:.3f}, Precision@0.9 {precision9:.3f},\n'
            f'mAP Precision @0.5:0.05:0.95 {precision_mAP:.3f},\n'
            f'Overall IoU {overall_iou:.3f}, Mean IoU (J) {mean_iou:.4f}')
    print("root_p = ",root_p)
    print("============================================================================================================================================\n")
