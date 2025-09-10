---
date:
  created: 2024-12-26
categories:
  - 文献整理
---


# Reading Papers

待整理 ...

<!-- more -->

## Pioneering Work

> Reference:
> 1. 
> 2. DETR: https://b23.tv/Qy47ExG
> 3. 
> 4. 





## Downstream Task

### Backbone


### Object Detection


### Image Segmentation

> Reference:
> 1. Universal Image Segmentation: https://huggingface.co/blog/mask2former

- MaskFormer: **Per-Pixel Classification is Not All You Need for Semantic Segmentation**. Bowen Cheng et al. 2021. [arxiv](https://arxiv.org/abs/2107.06278) [pdf](pdfs/MaskFormer_Bowen_Cheng_et_al_2107.06278.pdf)
- Mask2Former: **Masked-attention Mask Transformer for Universal Image Segmentation**. Bowen Cheng et al. 2021. [arxiv](https://arxiv.org/abs/2112.01527) [pdf](pdfs/Mask2Former_Bowen_Cheng_et_al_2112.01527.pdf)
- MaskDINO: **Mask DINO: Towards A Unified Transformer-based Framework for Object  Detection and Segmentation**. Feng Li et al. 2022. [arxiv](https://arxiv.org/abs/2206.02777) [pdf](pdfs/MaskDINO_Feng_Li_et_al_2206.02777.pdf)
- Oneformer: **OneFormer: One Transformer to Rule Universal Image Segmentation**. Jitesh Jain et al. 2022. [arxiv](https://arxiv.org/abs/2211.06220) [pdf](pdfs/Oneformer_Jitesh_Jain_et_al_2211.06220.pdf)

### Keypoint  Detection

- ViTDet: **Exploring Plain Vision Transformer Backbones for Object Detection**. Yanghao Li et al. 2022. [arxiv](https://arxiv.org/abs/2203.16527) [pdf](pdfs/ViTDet_Yanghao_Li_et_al_2203.16527.pdf)
- ViTPose: **ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation**. Yufei Xu et al. 2022. [arxiv](https://arxiv.org/abs/2204.12484) [pdf](pdfs/ViTPose_Yufei_Xu_et_al_2204.12484.pdf)
- ViTPose++: **ViTPose++: Vision Transformer for Generic Body Pose Estimation**. Yufei Xu et al. 2022. [arxiv](https://arxiv.org/abs/2212.04246) [pdf](pdfs/ViTPose++_Yufei_Xu_et_al_2212.04246.pdf)

## Learning Paradigm

### Contrastive Learning

> Reference:
> 1. MoCo: https://b23.tv/khDz0mx
> 2. MoCo-v2/v3: https://b23.tv/hgy75AS

- MoCo: **Momentum Contrast for Unsupervised Visual Representation Learning**. Kaiming He et al. 2019. [arxiv](https://arxiv.org/abs/1911.05722) [pdf](pdfs/MoCo_Kaiming_He_et_al_1911.05722.pdf)
- MoCo-v2: **Improved Baselines with Momentum Contrastive Learning**. Xinlei Chen et al. 2020. [arxiv](https://arxiv.org/abs/2003.04297) [pdf](pdfs/MoCo-v2_Xinlei_Chen_et_al_2003.04297.pdf)
- MoCo-v3: **An Empirical Study of Training Self-Supervised Vision Transformers**. Xinlei Chen et al. 2021. [arxiv](https://arxiv.org/abs/2104.02057) [pdf](pdfs/MoCo-v3_Xinlei_Chen_et_al_2104.02057.pdf)
- DINO: **Emerging Properties in Self-Supervised Vision Transformers**. Mathilde Caron et al. 2021. [arxiv](https://arxiv.org/abs/2104.14294) [pdf](pdfs/DINO_Mathilde_Caron_et_al_2104.14294.pdf)
- DINOv2: **DINOv2: Learning Robust Visual Features without Supervision**. Maxime Oquab et al. 2023. [arxiv](https://arxiv.org/abs/2304.07193) [pdf](pdfs/DINOv2_Maxime_Oquab_et_al_2304.07193.pdf)

### Mask Image Modeling

> Reference:
> 1. MAE: https://b23.tv/RGS2Pu5

- MAE: **Masked Autoencoders Are Scalable Vision Learners**. Kaiming He et al. 2021. [arxiv](https://arxiv.org/abs/2111.06377) [pdf](pdfs/MAE_Kaiming_He_et_al_2111.06377.pdf)
- BEiT: **BEiT: BERT Pre-Training of Image Transformers**. Hangbo Bao et al. 2021. [arxiv](https://arxiv.org/abs/2106.08254) [pdf](pdfs/BEiT_Hangbo_Bao_et_al_2106.08254.pdf)
- BEiT-v2: **BEiT v2: Masked Image Modeling with Vector-Quantized Visual Tokenizers**. Zhiliang Peng et al. 2022. [arxiv](https://arxiv.org/abs/2208.06366) [pdf](pdfs/BEiT-v2_Zhiliang_Peng_et_al_2208.06366.pdf)
- BEiT-v3: **Image as a Foreign Language: BEiT Pretraining for All Vision and  Vision-Language Tasks**. Wenhui Wang et al. 2022. [arxiv](https://arxiv.org/abs/2208.10442) [pdf](pdfs/BEiT-v3_Wenhui_Wang_et_al_2208.10442.pdf)
- EVA-01: **EVA: Exploring the Limits of Masked Visual Representation Learning at  Scale**. Yuxin Fang et al. 2022. [arxiv](https://arxiv.org/abs/2211.07636) [pdf](pdfs/EVA-01_Yuxin_Fang_et_al_2211.07636.pdf)
- EVA-02: **EVA-02: A Visual Representation for Neon Genesis**. Yuxin Fang et al. 2023. [arxiv](https://arxiv.org/abs/2303.11331) [pdf](pdfs/EVA-02_Yuxin_Fang_et_al_2303.11331.pdf)

### Active Learning

- SALOD: **Scalable Active Learning for Object Detection**. Elmar Haussmann et al. 2020. [arxiv](https://arxiv.org/abs/2004.04699) [pdf](pdfs/SALOD_Elmar_Haussmann_et_al_2004.04699.pdf)

## Large Model

### Diffusion Model

- Stable-Diffusion: **High-Resolution Image Synthesis with Latent Diffusion Models**. Robin Rombach et al. 2021. [arxiv](https://arxiv.org/abs/2112.10752) [pdf](pdfs/Stable-Diffusion_Robin_Rombach_et_al_2112.10752.pdf)

### PEFT

> Reference: 
> 1. https://b23.tv/i9GVaAs
> 2. https://huggingface.co/blog/peft

- LoRA: **LoRA: Low-Rank Adaptation of Large Language Models**. Edward J. Hu et al. 2021. [arxiv](https://arxiv.org/abs/2106.09685) [pdf](pdfs/LoRA_Edward_J._Hu_et_al_2106.09685.pdf)
    - code: https://github.com/microsoft/LoRA
    - Low-Rank Adaptation, or LoRA, which freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.
    - compared to adapters, no additional inference latency

    ![LoRA](imgs/main/lora.png)

    ![LoRA_formula](imgs/main/lora_formula.png)

- ViT-Adapter: **Vision Transformer Adapter for Dense Predictions**. Zhe Chen et al. 2022. [arxiv](https://arxiv.org/abs/2205.08534) [pdf](pdfs/ViT-Adapter_Zhe_Chen_et_al_2205.08534.pdf)

### Multi-Modal

open-vocabulary object detection:

- ViLD: **Open-vocabulary Object Detection via Vision and Language Knowledge  Distillation**. Xiuye Gu et al. 2021. [arxiv](https://arxiv.org/abs/2104.13921) [pdf](pdfs/ViLD_Xiuye_Gu_et_al_2104.13921.pdf)
- GroundingDINO: **Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set  Object Detection**. Shilong Liu et al. 2023. [arxiv](https://arxiv.org/abs/2303.05499) [pdf](pdfs/GroundingDINO_Shilong_Liu_et_al_2303.05499.pdf)

class-agnostic object detection:

- MViTs: **Class-agnostic Object Detection with Multi-modal Transformer**. Muhammad Maaz et al. 2021. [arxiv](https://arxiv.org/abs/2111.11430) [pdf](pdfs/MViTs_Muhammad_Maaz_et_al_2111.11430.pdf)


## Autonomous Driving

### BEV

- LSS: **Lift, Splat, Shoot: Encoding Images From Arbitrary Camera Rigs by  Implicitly Unprojecting to 3D**. Jonah Philion et al. 2020. [arxiv](https://arxiv.org/abs/2008.05711) [pdf](pdfs/LSS_Jonah_Philion_et_al_2008.05711.pdf)
- BevDet: **BEVDet: High-performance Multi-camera 3D Object Detection in  Bird-Eye-View**. Junjie Huang et al. 2021. [arxiv](https://arxiv.org/abs/2112.11790) [pdf](pdfs/BevDet_Junjie_Huang_et_al_2112.11790.pdf)
- BevVerse: **BEVerse: Unified Perception and Prediction in Birds-Eye-View for  Vision-Centric Autonomous Driving**. Yunpeng Zhang et al. 2022. [arxiv](https://arxiv.org/abs/2205.09743) [pdf](pdfs/BevVerse_Yunpeng_Zhang_et_al_2205.09743.pdf)
- BevFormer: **BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera  Images via Spatiotemporal Transformers**. Zhiqi Li et al. 2022. [arxiv](https://arxiv.org/abs/2203.17270) [pdf](pdfs/BevFormer_Zhiqi_Li_et_al_2203.17270.pdf)

### Occ

- NeRF: **NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis**. Ben Mildenhall et al. 2020. [arxiv](https://arxiv.org/abs/2003.08934) [pdf](pdfs/NeRF_Ben_Mildenhall_et_al_2003.08934.pdf)
- 3DGS: {{https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/}}
- TPVFormer: **Tri-Perspective View for Vision-Based 3D Semantic Occupancy Prediction**. Yuanhui Huang et al. 2023. [arxiv](https://arxiv.org/abs/2302.07817) [pdf](pdfs/TPVFormer_Yuanhui_Huang_et_al_2302.07817.pdf)

### End-to-End

- UniAD: **Planning-oriented Autonomous Driving**. Yihan Hu et al. 2022. [arxiv](https://arxiv.org/abs/2212.10156) [pdf](pdfs/UniAD_Yihan_Hu_et_al_2212.10156.pdf)
- E2EADSurvey: **End-to-end Autonomous Driving: Challenges and Frontiers**. Li Chen et al. 2023. [arxiv](https://arxiv.org/abs/2306.16927) [pdf](pdfs/E2EADSurvey_Li_Chen_et_al_2306.16927.pdf)

## Vision Language Model

## World Model
