# Video-Instrument Synergistic Network for Referring Video Instrument Segmentation in Robotic Surgery

We are excited to announce that our paper was accepted for publication at **IEEE TMI 2024**! 🥳🥳🥳

This repository contains the official implementation of our paper. 
You can access the paper [here](https://ieeexplore.ieee.org/abstract/document/10595513).

# Introduction 📑

This project introduces a new setting in surgical image segmentation, termed **Referring Surgical Video Instrument Segmentation (RSVIS)**. RSVIS aims to automatically identify and segment the target surgical instruments from each video frame, referred by a given language expression, in a more natural and flexible way
of human-computer interaction.

Fig. 1. Comparison of (a) existing instrument segmentation task and (b) our referring surgical video instrument segmentation (RSVIS).

<img width="623" alt="1722049397169" src="https://github.com/user-attachments/assets/56ac8436-280e-4416-a46c-884d1d774669">

# How to Run the Code 🛠
## Environment Installation
Thanks for your interest, code is being organized and will be online soon!

# Dataset 📊
The datasets have been organized!

Please contact Hongqiu (hongqiuwang16@gmail.com) for the dataset. One step is needed to download the dataset: **1) Use your google email to apply for the download permission ([Goole Driven](https://drive.google.com/drive/folders/11In7HqelWbsJPvIpGljSEOIUpzSHnPwo) [BaiduPan](https://pan.baidu.com/s/1t3FQFfa5minkaUIuOs3i3Q)). We will get back to you within three days, so please don't send them multiple times. We just handle the **real-name email** and **your email suffix must match your affiliation**. The email should contain the following information:

    Name/Homepage/Google Scholar: (Tell us who you are.)
    Primary Affiliation: (The name of your institution or university, etc.)
    Job Title: (E.g., Professor, Associate Professor, Ph.D., etc.)
    Affiliation Email: (the password will be sent to this email, we just reply to the email which is the end of "edu".)
    How to use: (Only for academic research, not for commercial use or second-development.)

The data set is stored as follows:

```text
RSVIS/
└── EndoVis-RS18/ 
    ├── train/
    │   ├── JPEGImages/
    │   │   └── */ (video folders)
    │   │       └── *.png (frame image files) 
    │   └── Annotations/
    │       └── */ (video folders)
    │           └── *.png (mask annotation files) 
    ├── valid/
    │   ├── JPEGImages/
    │   │   └── */ (video folders)
    │   │       └── *.png (frame image files) 
    │   └── Annotations/
    │       └── */ (video folders)
    │           └── *.png (mask annotation files) 
    └── meta_expressions/
        ├── train/
        │   └── meta_expressions.json  (text annotations)
        └── valid/
            └── meta_expressions.json  (text annotations)
```


# Citation 📖

If you find our work useful or relevant to your research, please consider citing:
```
@article{wang2024video,
  title={Video-instrument synergistic network for referring video instrument segmentation in robotic surgery},
  author={Wang, Hongqiu and Yang, Guang and Zhang, Shichen and Qin, Jing and Guo, Yike and Xu, Bo and Jin, Yueming and Zhu, Lei},
  journal={IEEE Transactions on Medical Imaging},
  year={2024},
  publisher={IEEE}
}
```
