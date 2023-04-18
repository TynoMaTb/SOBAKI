{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "YOLOv8 Tutorial",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "t6MPjfT5NrKQ"
      },
      "source": [
        "<div align=\"center\">\n",
        "\n",
        "  <a href=\"https://ultralytics.com/yolov8\" target=\"_blank\">\n",
        "    <img width=\"1024\", src=\"https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png\"></a>\n",
        "\n",
        "\n",
        "<br>\n",
        "  <a href=\"https://console.paperspace.com/github/ultralytics/ultralytics\"><img src=\"https://assets.paperspace.io/img/gradient-badge.svg\" alt=\"Run on Gradient\"/></a>\n",
        "  <a href=\"https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"></a>\n",
        "  <a href=\"https://www.kaggle.com/ultralytics/yolov8\"><img src=\"https://kaggle.com/static/images/open-in-kaggle.svg\" alt=\"Open In Kaggle\"></a>\n",
        "<br>\n",
        "\n",
        "Welcome to the Ultralytics YOLOv8 🚀 notebook! <a href=\"https://github.com/ultralytics/ultralytics\">YOLOv8</a> is the latest version of the YOLO (You Only Look Once) AI models developed by <a href=\"https://ultralytics.com\">Ultralytics</a>. This notebook serves as the starting point for exploring the various resources available to help you get started with YOLOv8 and understand its features and capabilities.\n",
        "\n",
        "YOLOv8 models are fast, accurate, and easy to use, making them ideal for various object detection and image segmentation tasks. They can be trained on large datasets and run on diverse hardware platforms, from CPUs to GPUs.\n",
        "\n",
        "We hope that the resources in this notebook will help you get the most out of YOLOv8. Please browse the YOLOv8 <a href=\"https://docs.ultralytics.com/\">Docs</a> for details, raise an issue on <a href=\"https://github.com/ultralytics/ultralytics\">GitHub</a> for support, and join our <a href=\"https://discord.gg/n6cFeSPZdD\">Discord</a> community for questions and discussions!\n",
        "\n",
        "</div>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7mGmQbAO5pQb"
      },
      "source": [
        "# Setup\n",
        "\n",
        "Pip install `ultralytics` and [dependencies](https://github.com/ultralytics/ultralytics/blob/main/requirements.txt) and check software and hardware."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wbvMlHd_QwMG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2ea6e0b9-1a62-4355-c246-5e8b7b1dafff"
      },
      "source": [
        "%pip install ultralytics\n",
        "import ultralytics\n",
        "ultralytics.checks()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Ultralytics YOLOv8.0.71 🚀 Python-3.9.16 torch-2.0.0+cu118 CUDA:0 (Tesla T4, 15102MiB)\n",
            "Setup complete ✅ (2 CPUs, 12.7 GB RAM, 23.3/166.8 GB disk)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4JnkELT0cIJg"
      },
      "source": [
        "# 1. Predict\n",
        "\n",
        "YOLOv8 may be used directly in the Command Line Interface (CLI) with a `yolo` command for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See a full list of available `yolo` [arguments](https://docs.ultralytics.com/usage/cfg/) and other details in the [YOLOv8 Predict Docs](https://docs.ultralytics.com/modes/train/).\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zR9ZbuQCH7FX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c578afbd-47cd-4d11-beec-8b5c31fcfba8"
      },
      "source": [
        "# Run inference on an image with YOLOv8n\n",
        "!yolo predict model=yolov8n.pt source='https://ultralytics.com/images/zidane.jpg'"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt to yolov8n.pt...\n",
            "100% 6.23M/6.23M [00:00<00:00, 195MB/s]\n",
            "Ultralytics YOLOv8.0.71 🚀 Python-3.9.16 torch-2.0.0+cu118 CUDA:0 (Tesla T4, 15102MiB)\n",
            "YOLOv8n summary (fused): 168 layers, 3151904 parameters, 0 gradients, 8.7 GFLOPs\n",
            "\n",
            "Downloading https://ultralytics.com/images/zidane.jpg to zidane.jpg...\n",
            "100% 165k/165k [00:00<00:00, 51.7MB/s]\n",
            "image 1/1 /content/zidane.jpg: 384x640 2 persons, 1 tie, 60.9ms\n",
            "Speed: 0.6ms preprocess, 60.9ms inference, 301.3ms postprocess per image at shape (1, 3, 640, 640)\n",
            "Results saved to \u001b[1mruns/detect/predict\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hkAzDWJ7cWTr"
      },
      "source": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n",
        "<img align=\"left\" src=\"https://user-images.githubusercontent.com/26833433/212889447-69e5bdf1-5800-4e29-835e-2ed2336dede2.jpg\" width=\"600\">"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0eq1SMWl6Sfn"
      },
      "source": [
        "# 2. Val\n",
        "Validate a model's accuracy on the [COCO](https://cocodataset.org/#home) dataset's `val` or `test` splits. The latest YOLOv8 [models](https://github.com/ultralytics/ultralytics#models) are downloaded automatically the first time they are used. See [YOLOv8 Val Docs](https://docs.ultralytics.com/modes/val/) for more information."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WQPtK1QYVaD_"
      },
      "source": [
        "# Download COCO val\n",
        "import torch\n",
        "torch.hub.download_url_to_file('https://ultralytics.com/assets/coco2017val.zip', 'tmp.zip')  # download (780M - 5000 images)\n",
        "!unzip -q tmp.zip -d datasets && rm tmp.zip  # unzip"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X58w8JLpMnjH",
        "outputId": "3e5a9c48-8eba-45eb-d92f-8456cf94b60e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Validate YOLOv8n on COCO128 val\n",
        "!yolo val model=yolov8n.pt data=coco128.yaml"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ultralytics YOLOv8.0.71 🚀 Python-3.9.16 torch-2.0.0+cu118 CUDA:0 (Tesla T4, 15102MiB)\n",
            "YOLOv8n summary (fused): 168 layers, 3151904 parameters, 0 gradients, 8.7 GFLOPs\n",
            "\n",
            "Dataset 'coco128.yaml' images not found ⚠️, missing paths ['/content/datasets/coco128/images/train2017']\n",
            "Downloading https://ultralytics.com/assets/coco128.zip to /content/datasets/coco128.zip...\n",
            "100% 6.66M/6.66M [00:01<00:00, 6.80MB/s]\n",
            "Unzipping /content/datasets/coco128.zip to /content/datasets...\n",
            "Dataset download success ✅ (2.2s), saved to \u001b[1m/content/datasets\u001b[0m\n",
            "\n",
            "Downloading https://ultralytics.com/assets/Arial.ttf to /root/.config/Ultralytics/Arial.ttf...\n",
            "100% 755k/755k [00:00<00:00, 107MB/s]\n",
            "\u001b[34m\u001b[1mval: \u001b[0mScanning /content/datasets/coco128/labels/train2017... 126 images, 2 backgrounds, 80 corrupt: 100% 128/128 [00:00<00:00, 1183.28it/s]\n",
            "\u001b[34m\u001b[1mval: \u001b[0mNew cache created: /content/datasets/coco128/labels/train2017.cache\n",
            "                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 8/8 [00:12<00:00,  1.54s/it]\n",
            "                   all        128        929       0.64      0.537      0.605      0.446\n",
            "                person        128        254      0.797      0.677      0.764      0.538\n",
            "               bicycle        128          6      0.514      0.333      0.315      0.264\n",
            "                   car        128         46      0.813      0.217      0.273      0.168\n",
            "            motorcycle        128          5      0.687      0.887      0.898      0.685\n",
            "              airplane        128          6       0.82      0.833      0.927      0.675\n",
            "                   bus        128          7      0.491      0.714      0.728      0.671\n",
            "                 train        128          3      0.534      0.667      0.706      0.604\n",
            "                 truck        128         12          1      0.332      0.473      0.297\n",
            "                  boat        128          6      0.226      0.167      0.316      0.134\n",
            "         traffic light        128         14      0.734        0.2      0.202      0.139\n",
            "             stop sign        128          2          1      0.992      0.995      0.701\n",
            "                 bench        128          9      0.839      0.582       0.62      0.365\n",
            "                  bird        128         16      0.921      0.728      0.864       0.51\n",
            "                   cat        128          4      0.875          1      0.995      0.791\n",
            "                   dog        128          9      0.603      0.889      0.785      0.585\n",
            "                 horse        128          2      0.597          1      0.995      0.518\n",
            "              elephant        128         17      0.849      0.765        0.9      0.679\n",
            "                  bear        128          1      0.593          1      0.995      0.995\n",
            "                 zebra        128          4      0.848          1      0.995      0.965\n",
            "               giraffe        128          9       0.72          1      0.951      0.722\n",
            "              backpack        128          6      0.589      0.333      0.376      0.232\n",
            "              umbrella        128         18      0.804        0.5      0.643      0.414\n",
            "               handbag        128         19      0.424     0.0526      0.165     0.0889\n",
            "                   tie        128          7      0.804      0.714      0.674      0.476\n",
            "              suitcase        128          4      0.635      0.883      0.745      0.534\n",
            "               frisbee        128          5      0.675        0.8      0.759      0.688\n",
            "                  skis        128          1      0.567          1      0.995      0.497\n",
            "             snowboard        128          7      0.742      0.714      0.747        0.5\n",
            "           sports ball        128          6      0.716      0.433      0.485      0.278\n",
            "                  kite        128         10      0.817       0.45      0.569      0.184\n",
            "          baseball bat        128          4      0.551       0.25      0.353      0.175\n",
            "        baseball glove        128          7      0.624      0.429      0.429      0.293\n",
            "            skateboard        128          5      0.846        0.6        0.6       0.41\n",
            "         tennis racket        128          7      0.726      0.387      0.487       0.33\n",
            "                bottle        128         18      0.448      0.389      0.376      0.208\n",
            "            wine glass        128         16      0.743      0.362      0.584      0.333\n",
            "                   cup        128         36       0.58      0.278      0.404       0.29\n",
            "                  fork        128          6      0.527      0.167      0.246      0.184\n",
            "                 knife        128         16      0.564        0.5       0.59       0.36\n",
            "                 spoon        128         22      0.597      0.182      0.328       0.19\n",
            "                  bowl        128         28      0.648      0.643      0.618      0.491\n",
            "                banana        128          1          0          0      0.124     0.0379\n",
            "              sandwich        128          2      0.249        0.5      0.308      0.308\n",
            "                orange        128          4          1       0.31      0.995      0.623\n",
            "              broccoli        128         11      0.374      0.182      0.249      0.203\n",
            "                carrot        128         24      0.648      0.458      0.572      0.362\n",
            "               hot dog        128          2      0.351      0.553      0.745      0.721\n",
            "                 pizza        128          5      0.644          1      0.995      0.843\n",
            "                 donut        128         14      0.657          1       0.94      0.864\n",
            "                  cake        128          4      0.618          1      0.945      0.845\n",
            "                 chair        128         35      0.506      0.514      0.442      0.239\n",
            "                 couch        128          6      0.463        0.5      0.706      0.555\n",
            "          potted plant        128         14       0.65      0.643      0.711      0.472\n",
            "                   bed        128          3      0.698      0.667      0.789      0.625\n",
            "          dining table        128         13      0.432      0.615      0.485      0.366\n",
            "                toilet        128          2      0.615        0.5      0.695      0.676\n",
            "                    tv        128          2      0.373       0.62      0.745      0.696\n",
            "                laptop        128          3          1          0      0.451      0.361\n",
            "                 mouse        128          2          1          0     0.0625    0.00625\n",
            "                remote        128          8      0.843        0.5      0.605      0.529\n",
            "            cell phone        128          8          0          0     0.0549     0.0393\n",
            "             microwave        128          3      0.435      0.667      0.806      0.718\n",
            "                  oven        128          5      0.412        0.4      0.339       0.27\n",
            "                  sink        128          6       0.35      0.167      0.182      0.129\n",
            "          refrigerator        128          5      0.589        0.4      0.604      0.452\n",
            "                  book        128         29      0.629      0.103      0.346      0.178\n",
            "                 clock        128          9      0.788       0.83      0.875       0.74\n",
            "                  vase        128          2      0.376          1      0.828      0.795\n",
            "              scissors        128          1          1          0      0.249     0.0746\n",
            "            teddy bear        128         21      0.877      0.333      0.591      0.394\n",
            "            toothbrush        128          5      0.743        0.6      0.638      0.374\n",
            "Speed: 5.3ms preprocess, 20.1ms inference, 0.0ms loss, 11.7ms postprocess per image\n",
            "Results saved to \u001b[1mruns/detect/val\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZY2VXXXu74w5"
      },
      "source": [
        "# 3. Train\n",
        "\n",
        "<p align=\"\"><a href=\"https://bit.ly/ultralytics_hub\"><img width=\"1000\" src=\"https://github.com/ultralytics/assets/raw/main/yolov8/banner-integrations.png\"/></a></p>\n",
        "\n",
        "Train YOLOv8 on [Detect](https://docs.ultralytics.com/tasks/detect/), [Segment](https://docs.ultralytics.com/tasks/segment/), [Classify](https://docs.ultralytics.com/tasks/classify/) and [Pose](https://docs.ultralytics.com/tasks/pose/) datasets. See [YOLOv8 Train Docs](https://docs.ultralytics.com/modes/train/) for more information."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1NcFxRcFdJ_O",
        "outputId": "2b6cc129-9c3b-4495-db3e-1a1b867bc227",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "# Train YOLOv8n on COCO128 for 3 epochs\n",
        "!yolo train model=yolov8n.pt data=coco128.yaml epochs=3 imgsz=640"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt to yolov8n.pt...\n",
            "100% 6.23M/6.23M [00:00<00:00, 46.4MB/s]\n",
            "Ultralytics YOLOv8.0.81 🚀 Python-3.9.16 torch-2.0.0+cu118 CPU\n",
            "\u001b[34m\u001b[1myolo/engine/trainer: \u001b[0mtask=detect, mode=train, model=yolov8n.pt, data=coco128.yaml, epochs=3, patience=50, batch=16, imgsz=640, save=True, save_period=-1, cache=False, device=None, workers=8, project=None, name=None, exist_ok=False, pretrained=False, optimizer=SGD, verbose=True, seed=0, deterministic=True, single_cls=False, image_weights=False, rect=False, cos_lr=False, close_mosaic=0, resume=False, amp=True, overlap_mask=True, mask_ratio=4, dropout=0.0, val=True, split=val, save_json=False, save_hybrid=False, conf=None, iou=0.7, max_det=300, half=False, dnn=False, plots=True, source=None, show=False, save_txt=False, save_conf=False, save_crop=False, show_labels=True, show_conf=True, vid_stride=1, line_thickness=3, visualize=False, augment=False, agnostic_nms=False, classes=None, retina_masks=False, boxes=True, format=torchscript, keras=False, optimize=False, int8=False, dynamic=False, simplify=False, opset=None, workspace=4, nms=False, lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=7.5, cls=0.5, dfl=1.5, pose=12.0, kobj=1.0, label_smoothing=0.0, nbs=64, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.0, copy_paste=0.0, cfg=None, v5loader=False, tracker=botsort.yaml, save_dir=runs/detect/train\n",
            "\n",
            "Dataset 'coco128.yaml' images not found ⚠️, missing paths ['/content/datasets/coco128/images/train2017']\n",
            "Downloading https://ultralytics.com/assets/coco128.zip to /content/datasets/coco128.zip...\n",
            "100% 6.66M/6.66M [00:00<00:00, 60.7MB/s]\n",
            "Unzipping /content/datasets/coco128.zip to /content/datasets...\n",
            "Dataset download success ✅ (0.5s), saved to \u001b[1m/content/datasets\u001b[0m\n",
            "\n",
            "Downloading https://ultralytics.com/assets/Arial.ttf to /root/.config/Ultralytics/Arial.ttf...\n",
            "100% 755k/755k [00:00<00:00, 13.0MB/s]\n",
            "\n",
            "                   from  n    params  module                                       arguments                     \n",
            "  0                  -1  1       464  ultralytics.nn.modules.Conv                  [3, 16, 3, 2]                 \n",
            "  1                  -1  1      4672  ultralytics.nn.modules.Conv                  [16, 32, 3, 2]                \n",
            "  2                  -1  1      7360  ultralytics.nn.modules.C2f                   [32, 32, 1, True]             \n",
            "  3                  -1  1     18560  ultralytics.nn.modules.Conv                  [32, 64, 3, 2]                \n",
            "  4                  -1  2     49664  ultralytics.nn.modules.C2f                   [64, 64, 2, True]             \n",
            "  5                  -1  1     73984  ultralytics.nn.modules.Conv                  [64, 128, 3, 2]               \n",
            "  6                  -1  2    197632  ultralytics.nn.modules.C2f                   [128, 128, 2, True]           \n",
            "  7                  -1  1    295424  ultralytics.nn.modules.Conv                  [128, 256, 3, 2]              \n",
            "  8                  -1  1    460288  ultralytics.nn.modules.C2f                   [256, 256, 1, True]           \n",
            "  9                  -1  1    164608  ultralytics.nn.modules.SPPF                  [256, 256, 5]                 \n",
            " 10                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          \n",
            " 11             [-1, 6]  1         0  ultralytics.nn.modules.Concat                [1]                           \n",
            " 12                  -1  1    148224  ultralytics.nn.modules.C2f                   [384, 128, 1]                 \n",
            " 13                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          \n",
            " 14             [-1, 4]  1         0  ultralytics.nn.modules.Concat                [1]                           \n",
            " 15                  -1  1     37248  ultralytics.nn.modules.C2f                   [192, 64, 1]                  \n",
            " 16                  -1  1     36992  ultralytics.nn.modules.Conv                  [64, 64, 3, 2]                \n",
            " 17            [-1, 12]  1         0  ultralytics.nn.modules.Concat                [1]                           \n",
            " 18                  -1  1    123648  ultralytics.nn.modules.C2f                   [192, 128, 1]                 \n",
            " 19                  -1  1    147712  ultralytics.nn.modules.Conv                  [128, 128, 3, 2]              \n",
            " 20             [-1, 9]  1         0  ultralytics.nn.modules.Concat                [1]                           \n",
            " 21                  -1  1    493056  ultralytics.nn.modules.C2f                   [384, 256, 1]                 \n",
            " 22        [15, 18, 21]  1    897664  ultralytics.nn.modules.Detect                [80, [64, 128, 256]]          \n",
            "Model summary: 225 layers, 3157200 parameters, 3157184 gradients, 8.9 GFLOPs\n",
            "\n",
            "Transferred 355/355 items from pretrained weights\n",
            "\u001b[34m\u001b[1mTensorBoard: \u001b[0mStart with 'tensorboard --logdir runs/detect/train', view at http://localhost:6006/\n",
            "\u001b[34m\u001b[1moptimizer:\u001b[0m SGD(lr=0.01) with parameter groups 57 weight(decay=0.0), 64 weight(decay=0.0005), 63 bias\n",
            "\u001b[34m\u001b[1mtrain: \u001b[0mScanning /content/datasets/coco128/labels/train2017... 126 images, 2 backgrounds, 0 corrupt: 100% 128/128 [00:00<00:00, 1885.72it/s]\n",
            "\u001b[34m\u001b[1mtrain: \u001b[0mNew cache created: /content/datasets/coco128/labels/train2017.cache\n",
            "\u001b[34m\u001b[1malbumentations: \u001b[0mBlur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01), CLAHE(p=0.01, clip_limit=(1, 4.0), tile_grid_size=(8, 8))\n",
            "\u001b[34m\u001b[1mval: \u001b[0mScanning /content/datasets/coco128/labels/train2017.cache... 126 images, 2 backgrounds, 0 corrupt: 100% 128/128 [00:00<?, ?it/s]\n",
            "Plotting labels to runs/detect/train/labels.jpg... \n",
            "Image sizes 640 train, 640 val\n",
            "Using 0 dataloader workers\n",
            "Logging results to \u001b[1mruns/detect/train\u001b[0m\n",
            "Starting training for 3 epochs...\n",
            "\n",
            "      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size\n",
            "        1/3         0G      1.142      1.378      1.211        227        640:  50% 4/8 [01:11<01:09, 17.27s/it]"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 4. Export\n",
        "\n",
        "Export a YOLOv8 model to any supported format below with the `format` argument, i.e. `format=onnx`. See [YOLOv8 Export Docs](https://docs.ultralytics.com/modes/export/) for more information.\n",
        "\n",
        "- 💡 ProTip: Export to [ONNX](https://onnx.ai/) or [OpenVINO](https://docs.openvino.ai/latest/index.html) for up to 3x CPU speedup.  \n",
        "- 💡 ProTip: Export to [TensorRT](https://developer.nvidia.com/tensorrt) for up to 5x GPU speedup.\n",
        "\n",
        "\n",
        "| Format                                                                     | `format=`          | Model                     |\n",
        "|----------------------------------------------------------------------------|--------------------|---------------------------|\n",
        "| [PyTorch](https://pytorch.org/)                                            | -                  | `yolov8n.pt`              |\n",
        "| [TorchScript](https://pytorch.org/docs/stable/jit.html)                    | `torchscript`      | `yolov8n.torchscript`     |\n",
        "| [ONNX](https://onnx.ai/)                                                   | `onnx`             | `yolov8n.onnx`            |\n",
        "| [OpenVINO](https://docs.openvino.ai/latest/index.html)                     | `openvino`         | `yolov8n_openvino_model/` |\n",
        "| [TensorRT](https://developer.nvidia.com/tensorrt)                          | `engine`           | `yolov8n.engine`          |\n",
        "| [CoreML](https://github.com/apple/coremltools)                             | `coreml`           | `yolov8n.mlmodel`         |\n",
        "| [TensorFlow SavedModel](https://www.tensorflow.org/guide/saved_model)      | `saved_model`      | `yolov8n_saved_model/`    |\n",
        "| [TensorFlow GraphDef](https://www.tensorflow.org/api_docs/python/tf/Graph) | `pb`               | `yolov8n.pb`              |\n",
        "| [TensorFlow Lite](https://www.tensorflow.org/lite)                         | `tflite`           | `yolov8n.tflite`          |\n",
        "| [TensorFlow Edge TPU](https://coral.ai/docs/edgetpu/models-intro/)         | `edgetpu`          | `yolov8n_edgetpu.tflite`  |\n",
        "| [TensorFlow.js](https://www.tensorflow.org/js)                             | `tfjs`             | `yolov8n_web_model/`      |\n",
        "| [PaddlePaddle](https://github.com/PaddlePaddle)                            | `paddle`           | `yolov8n_paddle_model/`   |\n",
        "\n"
      ],
      "metadata": {
        "id": "nPZZeNrLCQG6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!yolo export model=yolov8n.pt format=torchscript"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CYIjW4igCjqD",
        "outputId": "fc41bf7a-0ea2-41a6-9ec5-dd0455af43bc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ultralytics YOLOv8.0.71 🚀 Python-3.9.16 torch-2.0.0+cu118 CPU\n",
            "YOLOv8n summary (fused): 168 layers, 3151904 parameters, 0 gradients, 8.7 GFLOPs\n",
            "\n",
            "\u001b[34m\u001b[1mPyTorch:\u001b[0m starting from yolov8n.pt with input shape (1, 3, 640, 640) BCHW and output shape(s) (1, 84, 8400) (6.2 MB)\n",
            "\n",
            "\u001b[34m\u001b[1mTorchScript:\u001b[0m starting export with torch 2.0.0+cu118...\n",
            "\u001b[34m\u001b[1mTorchScript:\u001b[0m export success ✅ 2.3s, saved as yolov8n.torchscript (12.4 MB)\n",
            "\n",
            "Export complete (3.1s)\n",
            "Results saved to \u001b[1m/content\u001b[0m\n",
            "Predict:         yolo predict task=detect model=yolov8n.torchscript imgsz=640 \n",
            "Validate:        yolo val task=detect model=yolov8n.torchscript imgsz=640 data=coco.yaml \n",
            "Visualize:       https://netron.app\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 5. Python Usage\n",
        "\n",
        "YOLOv8 was reimagined using Python-first principles for the most seamless Python YOLO experience yet. YOLOv8 models can be loaded from a trained checkpoint or created from scratch. Then methods are used to train, val, predict, and export the model. See detailed Python usage examples in the [YOLOv8 Python Docs](https://docs.ultralytics.com/usage/python/)."
      ],
      "metadata": {
        "id": "kUMOQ0OeDBJG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from ultralytics import YOLO\n",
        "\n",
        "# Load a model\n",
        "model = YOLO('yolov8n.yaml')  # build a new model from scratch\n",
        "model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)\n",
        "\n",
        "# Use the model\n",
        "results = model.train(data='coco128.yaml', epochs=3)  # train the model\n",
        "results = model.val()  # evaluate model performance on the validation set\n",
        "results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image\n",
        "success = model.export(format='onnx')  # export the model to ONNX format"
      ],
      "metadata": {
        "id": "bpF9-vS_DAaf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 6. Tasks\n",
        "\n",
        "YOLOv8 can train, val, predict and export models for the most common tasks in vision AI: [Detect](https://docs.ultralytics.com/tasks/detect/), [Segment](https://docs.ultralytics.com/tasks/segment/), [Classify](https://docs.ultralytics.com/tasks/classify/) and [Pose](https://docs.ultralytics.com/tasks/pose/). See [YOLOv8 Tasks Docs](https://docs.ultralytics.com/tasks/) for more information.\n",
        "\n",
        "<img width=\"1024\" src=\"https://user-images.githubusercontent.com/26833433/212094133-6bb8c21c-3d47-41df-a512-81c5931054ae.png\">\n"
      ],
      "metadata": {
        "id": "Phm9ccmOKye5"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 1. Detection\n",
        "\n",
        "YOLOv8 _detection_ models have no suffix and are the default YOLOv8 models, i.e. `yolov8n.pt` and are pretrained on COCO. See [Detection Docs](https://docs.ultralytics.com/tasks/detect/) for full details.\n"
      ],
      "metadata": {
        "id": "yq26lwpYK1lq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Load YOLOv8n, train it on COCO128 for 3 epochs and predict an image with it\n",
        "from ultralytics import YOLO\n",
        "\n",
        "model = YOLO('yolov8n.pt')  # load a pretrained YOLOv8n detection model\n",
        "model.train(data='coco128.yaml', epochs=3)  # train the model\n",
        "model('https://ultralytics.com/images/bus.jpg')  # predict on an image"
      ],
      "metadata": {
        "id": "8Go5qqS9LbC5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 2. Segmentation\n",
        "\n",
        "YOLOv8 _segmentation_ models use the `-seg` suffix, i.e. `yolov8n-seg.pt` and are pretrained on COCO. See [Segmentation Docs](https://docs.ultralytics.com/tasks/segment/) for full details.\n"
      ],
      "metadata": {
        "id": "7ZW58jUzK66B"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Load YOLOv8n-seg, train it on COCO128-seg for 3 epochs and predict an image with it\n",
        "from ultralytics import YOLO\n",
        "\n",
        "model = YOLO('yolov8n-seg.pt')  # load a pretrained YOLOv8n segmentation model\n",
        "model.train(data='coco128-seg.yaml', epochs=3)  # train the model\n",
        "model('https://ultralytics.com/images/bus.jpg')  # predict on an image"
      ],
      "metadata": {
        "id": "WFPJIQl_L5HT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 3. Classification\n",
        "\n",
        "YOLOv8 _classification_ models use the `-cls` suffix, i.e. `yolov8n-cls.pt` and are pretrained on ImageNet. See [Classification Docs](https://docs.ultralytics.com/tasks/classify/) for full details.\n"
      ],
      "metadata": {
        "id": "ax3p94VNK9zR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Load YOLOv8n-cls, train it on mnist160 for 3 epochs and predict an image with it\n",
        "from ultralytics import YOLO\n",
        "\n",
        "model = YOLO('yolov8n-cls.pt')  # load a pretrained YOLOv8n classification model\n",
        "model.train(data='mnist160', epochs=3)  # train the model\n",
        "model('https://ultralytics.com/images/bus.jpg')  # predict on an image"
      ],
      "metadata": {
        "id": "5q9Zu6zlL5rS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 4. Pose\n",
        "\n",
        "YOLOv8 _pose_ models use the `-pose` suffix, i.e. `yolov8n-pose.pt` and are pretrained on COCO Keypoints. See [Pose Docs](https://docs.ultralytics.com/tasks/pose/) for full details."
      ],
      "metadata": {
        "id": "SpIaFLiO11TG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Load YOLOv8n-pose, train it on COCO8-pose for 3 epochs and predict an image with it\n",
        "from ultralytics import YOLO\n",
        "\n",
        "model = YOLO('yolov8n-pose.pt')  # load a pretrained YOLOv8n classification model\n",
        "model.train(data='coco8-pose.yaml', epochs=3)  # train the model\n",
        "model('https://ultralytics.com/images/bus.jpg')  # predict on an image"
      ],
      "metadata": {
        "id": "si4aKFNg19vX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IEijrePND_2I"
      },
      "source": [
        "# Appendix\n",
        "\n",
        "Additional content below."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Git clone and run tests on updates branch\n",
        "!git clone https://github.com/ultralytics/ultralytics -b updates\n",
        "%pip install -qe ultralytics\n",
        "!pytest ultralytics/tests"
      ],
      "metadata": {
        "id": "uRKlwxSJdhd1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Validate multiple models\n",
        "for x in 'nsmlx':\n",
        "  !yolo val model=yolov8{x}.pt data=coco.yaml"
      ],
      "metadata": {
        "id": "Wdc6t_bfzDDk"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}