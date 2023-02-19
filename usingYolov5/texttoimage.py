# 웹으로 쓰기 위해선 해당 학습파일에서 나온 best.pt or last.pt를 저장해야한다.   
# -*- coding: utf-8 -*-
"""글그림

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t14obiAquQlfC058gRwULXLKJN1V_eMD
"""

from google.colab import drive
drive.mount('/content/drive')

from IPython.display import Image

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5  # clone
# %cd yolov5
# %pip install -qr requirements.txt  # install

import torch
import utils
display = utils.notebook_init()  # checks

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="AQi09vr3qenDSlAJtgSV")
project = rf.workspace("project-qxgbd").project("injeolmee")
dataset = project.version(2).download("yolov5")

# Train YOLOv5s on COCO128 for 3 epochs
!python train.py --img 640 --batch 32 --epochs 3000 --data /content/data.yaml --weights yolov5l.pt --cache --patience 10
##patience (=earlystopping)

# train 그래프
Image('/yolov5/runs/train/exp4/results.png')

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""# 수류탄 살았다"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.85 --source /content/drive/MyDrive/pic/KakaoTalk_20230106_094915648.png

Image('/yolov5/runs/detect/exp10/KakaoTalk_20230106_094915648.png')

"""수류탄..살듯
last.pt로는 어렵다
- best.pt로 가자
"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/last.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/KakaoTalk_20230106_094915648.png

Image('/yolov5/runs/detect/exp42/KakaoTalk_20230106_094915648.png')

"""# 벤치와 수류탄
- 인식못함
"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/KakaoTalk_20230106_094122929.jpg

Image('/yolov5/runs/detect/exp41/KakaoTalk_20230106_094122929.jpg')

"""벤치야...잘가 오리지널버전에서 보자"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/KakaoTalk_20230106_094211175.png

Image('/yolov5/runs/detect/exp40/KakaoTalk_20230106_094211175.png')

"""## 벤치 진짜 안되네

# 토끼
"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.5 --source /content/drive/MyDrive/pic/이게토끼.jpg

Image('/yolov5/runs/detect/exp39/이게토끼.jpg')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.85 --source /content/drive/MyDrive/pic/동환토끼.jpg

Image('/yolov5/runs/detect/exp15/동환토끼.jpg')

"""# 해바라기"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.1 --source /content/drive/MyDrive/pic/sunflower2.png

Image('/yolov5/runs/detect/exp37/sunflower2.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.85 --source /content/drive/MyDrive/pic/희현바라기.png

Image('/yolov5/runs/detect/exp18/희현바라기.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.85 --source /content/drive/MyDrive/pic/혜빈바라기.png

Image('/yolov5/runs/detect/exp19/혜빈바라기.png')

"""# 달팽이"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/sail/p_0596_11366_3051.jpg

Image('/yolov5/runs/detect/exp33/p_0596_11366_3051.jpg')

"""# 칫솔"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/동환칫솔.jpg

Image('/yolov5/runs/detect/exp32/동환칫솔.jpg')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.35 --source /content/drive/MyDrive/pic/숭한칫솔.jpg

Image('/yolov5/runs/detect/exp23/숭한칫솔.jpg')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.85 --source /content/drive/MyDrive/pic/엄청난칫솔.jpg

Image('/yolov5/runs/detect/exp25/엄청난칫솔.jpg')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.5 --source /content/drive/MyDrive/pic/칫솔01.png

Image('/yolov5/runs/detect/exp29/칫솔01.png')

"""# 열기구"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/열기구.png

Image('/yolov5/runs/detect/exp44/열기구.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/동환열기구.jpg

Image('/yolov5/runs/detect/exp45/동환열기구.jpg')

"""# 열기구"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/해파리01.png

Image('/yolov5/runs/detect/exp46/해파리01.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/혜빈해파리.png

Image('/yolov5/runs/detect/exp47/혜빈해파리.png')

Image('/yolov5/runs/detect/exp47/혜빈해파리.png')

"""# 나뭇잎"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/이게나뭇잎.png

Image('/yolov5/runs/detect/exp48/이게나뭇잎.png')

"""# 선풍기"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/선풍기.jpg

Image('/yolov5/runs/detect/exp49/선풍기.jpg')

"""# 가스"""

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/동환그잡채.jpg

Image('/yolov5/runs/detect/exp50/동환그잡채.jpg')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/주유소.png

Image('/yolov5/runs/detect/exp51/주유소.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/귀염물개.png

Image('/yolov5/runs/detect/exp52/귀염물개.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/고래일지도.png

Image('/yolov5/runs/detect/exp54/고래일지도.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/사과일지도.png

Image('/yolov5/runs/detect/exp55/사과일지도.png')

!python detect.py --weights /yolov5/runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source /content/drive/MyDrive/pic/게일지도.png

Image('/yolov5/runs/detect/exp56/게일지도.png')

"""# 성공한 class
- 열기구
- 주유기계
- 선풍기
- 물개
- 토끼
- 해바라기
- 칫솔
- 수류탄
- 사과
"""

