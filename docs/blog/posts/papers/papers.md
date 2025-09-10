---
date:
  created: 2024-12-26
categories:
  - 文献整理
---

# 论文汇总

论文汇总 ...

<!-- more -->

## 开创性工作

- Transformer: 1706.03762. **Attention Is All You Need**. Ashish Vaswani et al | \[[abs](https://arxiv.org/abs/1706.03762)\] \[[pdf](../pdfs/1706.03762_Attention_Is_All_You_Need_Ashish_Vaswani_et_al.pdf)\]
- ViT: 2010.11929. **An Image is Worth 16x16 Words: Transformers for Image Recognition at  Scale**. Alexey Dosovitskiy et al | \[[abs](https://arxiv.org/abs/2010.11929)\] \[[pdf](../pdfs/2010.11929_An_Image_is_Worth_16x16_Words#_Transformers_for_Image_Recognition_at__Scale_Alexey_Dosovitskiy_et_al.pdf)\]
- Swin Transformer: 2103.14030. **Swin Transformer: Hierarchical Vision Transformer using Shifted Windows**. Ze Liu et al | \[[abs](https://arxiv.org/abs/2103.14030)\] \[[pdf](../pdfs/2103.14030_Swin_Transformer#_Hierarchical_Vision_Transformer_using_Shifted_Windows_Ze_Liu_et_al.pdf)\]
- ViT Det: 2203.16527. **Exploring Plain Vision Transformer Backbones for Object Detection**. Yanghao Li et al | \[[abs](https://arxiv.org/abs/2203.16527)\] \[[pdf](../pdfs/2203.16527_Exploring_Plain_Vision_Transformer_Backbones_for_Object_Detection_Yanghao_Li_et_al.pdf)\]
- DETR: 2005.12872. **End-to-End Object Detection with Transformers**. Nicolas Carion et al | \[[abs](https://arxiv.org/abs/2005.12872)\] \[[pdf](../pdfs/2005.12872_End-to-End_Object_Detection_with_Transformers_Nicolas_Carion_et_al.pdf)\]
- CLIP: 2103.00020. **Learning Transferable Visual Models From Natural Language Supervision**. Alec Radford et al | \[[abs](https://arxiv.org/abs/2103.00020)\] \[[pdf](../pdfs/2103.00020_Learning_Transferable_Visual_Models_From_Natural_Language_Supervision_Alec_Radford_et_al.pdf)\]

## 下游任务

### 目标检测

- Deformable DETR: 2010.04159. **Deformable DETR: Deformable Transformers for End-to-End Object Detection**. Xizhou Zhu et al | \[[abs](https://arxiv.org/abs/2010.04159)\] \[[pdf](../pdfs/2010.04159_Deformable_DETR#_Deformable_Transformers_for_End-to-End_Object_Detection_Xizhou_Zhu_et_al.pdf)\]
- DAB-DETR: 2201.12329. **DAB-DETR: Dynamic Anchor Boxes are Better Queries for DETR**. Shilong Liu et al | \[[abs](https://arxiv.org/abs/2201.12329)\] \[[pdf](../pdfs/2201.12329_DAB-DETR#_Dynamic_Anchor_Boxes_are_Better_Queries_for_DETR_Shilong_Liu_et_al.pdf)\]
- DN-DETR: 2203.01305. **DN-DETR: Accelerate DETR Training by Introducing Query DeNoising**. Feng Li et al | \[[abs](https://arxiv.org/abs/2203.01305)\] \[[pdf](../pdfs/2203.01305_DN-DETR#_Accelerate_DETR_Training_by_Introducing_Query_DeNoising_Feng_Li_et_al.pdf)\]
- DINO: 2203.03605. **DINO: DETR with Improved DeNoising Anchor Boxes for End-to-End Object  Detection**. Hao Zhang et al | \[[abs](https://arxiv.org/abs/2203.03605)\] \[[pdf](../pdfs/2203.03605_DINO#_DETR_with_Improved_DeNoising_Anchor_Boxes_for_End-to-End_Object__Detection_Hao_Zhang_et_al.pdf)\]
- Co-DETR: 2211.12860. **DETRs with Collaborative Hybrid Assignments Training**. Zhuofan Zong et al | \[[abs](https://arxiv.org/abs/2211.12860)\] \[[pdf](../pdfs/2211.12860_DETRs_with_Collaborative_Hybrid_Assignments_Training_Zhuofan_Zong_et_al.pdf)\]

### 图像分割

- MaskFormer: 2107.06278. **Per-Pixel Classification is Not All You Need for Semantic Segmentation**. Bowen Cheng et al | \[[abs](https://arxiv.org/abs/2107.06278)\] \[[pdf](../pdfs/2107.06278_Per-Pixel_Classification_is_Not_All_You_Need_for_Semantic_Segmentation_Bowen_Cheng_et_al.pdf)\]
- Mask2Former: 2112.01527. **Masked-attention Mask Transformer for Universal Image Segmentation**. Bowen Cheng et al | \[[abs](https://arxiv.org/abs/2112.01527)\] \[[pdf](../pdfs/2112.01527_Masked-attention_Mask_Transformer_for_Universal_Image_Segmentation_Bowen_Cheng_et_al.pdf)\]
- MaskDINO: 2206.02777. **Mask DINO: Towards A Unified Transformer-based Framework for Object  Detection and Segmentation**. Feng Li et al | \[[abs](https://arxiv.org/abs/2206.02777)\] \[[pdf](../pdfs/2206.02777_Mask_DINO#_Towards_A_Unified_Transformer-based_Framework_for_Object__Detection_and_Segmentation_Feng_Li_et_al.pdf)\]
- Oneformer: 2211.06220. **OneFormer: One Transformer to Rule Universal Image Segmentation**. Jitesh Jain et al | \[[abs](https://arxiv.org/abs/2211.06220)\] \[[pdf](../pdfs/2211.06220_OneFormer#_One_Transformer_to_Rule_Universal_Image_Segmentation_Jitesh_Jain_et_al.pdf)\]

### 关键点检测

- ViTPose: 2204.12484. **ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation**. Yufei Xu et al | \[[abs](https://arxiv.org/abs/2204.12484)\] \[[pdf](../pdfs/2204.12484_ViTPose#_Simple_Vision_Transformer_Baselines_for_Human_Pose_Estimation_Yufei_Xu_et_al.pdf)\]
- ViTPose++: 2212.04246. **ViTPose++: Vision Transformer Foundation Model for Generic Body Pose  Estimation**. Yufei Xu et al | \[[abs](https://arxiv.org/abs/2212.04246)\] \[[pdf](../pdfs/2212.04246_ViTPose++#_Vision_Transformer_Foundation_Model_for_Generic_Body_Pose__Estimation_Yufei_Xu_et_al.pdf)\]

## 学习范式

### 自监督学习

#### 对比学习

- MoCo: 1911.05722. **Momentum Contrast for Unsupervised Visual Representation Learning**. Kaiming He et al | \[[abs](https://arxiv.org/abs/1911.05722)\] \[[pdf](../pdfs/1911.05722_Momentum_Contrast_for_Unsupervised_Visual_Representation_Learning_Kaiming_He_et_al.pdf)\]
- MoCo v2: 2003.04297. **Improved Baselines with Momentum Contrastive Learning**. Xinlei Chen et al | \[[abs](https://arxiv.org/abs/2003.04297)\] \[[pdf](../pdfs/2003.04297_Improved_Baselines_with_Momentum_Contrastive_Learning_Xinlei_Chen_et_al.pdf)\]
- 2104.02057. **An Empirical Study of Training Self-Supervised Vision Transformers**. Xinlei Chen et al | \[[abs](https://arxiv.org/abs/2104.02057)\] \[[pdf](../pdfs/2104.02057_An_Empirical_Study_of_Training_Self-Supervised_Vision_Transformers_Xinlei_Chen_et_al.pdf)\]
- 2104.14294. **Emerging Properties in Self-Supervised Vision Transformers**. Mathilde Caron et al | \[[abs](https://arxiv.org/abs/2104.14294)\] \[[pdf](../pdfs/2104.14294_Emerging_Properties_in_Self-Supervised_Vision_Transformers_Mathilde_Caron_et_al.pdf)\]
- DINOv2: 2304.07193. **DINOv2: Learning Robust Visual Features without Supervision**. Maxime Oquab et al | \[[abs](https://arxiv.org/abs/2304.07193)\] \[[pdf](../pdfs/2304.07193_DINOv2#_Learning_Robust_Visual_Features_without_Supervision_Maxime_Oquab_et_al.pdf)\]

#### 掩码学习

- MAE: 2111.06377. **Masked Autoencoders Are Scalable Vision Learners**. Kaiming He et al | \[[abs](https://arxiv.org/abs/2111.06377)\] \[[pdf](../pdfs/2111.06377_Masked_Autoencoders_Are_Scalable_Vision_Learners_Kaiming_He_et_al.pdf)\]
- BEiT: 2106.08254. **BEiT: BERT Pre-Training of Image Transformers**. Hangbo Bao et al | \[[abs](https://arxiv.org/abs/2106.08254)\] \[[pdf](../pdfs/2106.08254_BEiT: BERT Pre-Training of Image Transformers_Hangbo Bao et al.pdf)\]
- BEiT v2: 2208.06366. **BEiT v2: Masked Image Modeling with Vector-Quantized Visual Tokenizers**. Zhiliang Peng et al | \[[abs](https://arxiv.org/abs/2208.06366)\] \[[pdf](../pdfs/2208.06366_BEiT_v2#_Masked_Image_Modeling_with_Vector-Quantized_Visual_Tokenizers_Zhiliang_Peng_et_al.pdf)\]
- BEiT v3: 2208.10442. **Image as a Foreign Language: BEiT Pretraining for All Vision and  Vision-Language Tasks**. Wenhui Wang et al | \[[abs](https://arxiv.org/abs/2208.10442)\] \[[pdf](../pdfs/2208.10442_Image_as_a_Foreign_Language#_BEiT_Pretraining_for_All_Vision_and__Vision-Language_Tasks_Wenhui_Wang_et_al.pdf)\]
- EVA-01: 2211.07636. **EVA: Exploring the Limits of Masked Visual Representation Learning at  Scale**. Yuxin Fang et al | \[[abs](https://arxiv.org/abs/2211.07636)\] \[[pdf](../pdfs/2211.07636_EVA#_Exploring_the_Limits_of_Masked_Visual_Representation_Learning_at__Scale_Yuxin_Fang_et_al.pdf)\]
- EVA-02: 2303.11331. **EVA-02: A Visual Representation for Neon Genesis**. Yuxin Fang et al | \[[abs](https://arxiv.org/abs/2303.11331)\] \[[pdf](../pdfs/2303.11331_EVA-02#_A_Visual_Representation_for_Neon_Genesis_Yuxin_Fang_et_al.pdf)\]

### 主动学习

- SALOD: 2004.04699. **Scalable Active Learning for Object Detection**. Elmar Haussmann et al | \[[abs](https://arxiv.org/abs/2004.04699)\] \[[pdf](../pdfs/2004.04699_Scalable_Active_Learning_for_Object_Detection_Elmar_Haussmann_et_al.pdf)\]

## 大模型

### 扩散模型

Diffusion Model: 2112.10752. **High-Resolution Image Synthesis with Latent Diffusion Models**. Robin Rombach et al | \[[abs](https://arxiv.org/abs/2112.10752)\] \[[pdf](../pdfs/2112.10752_High-Resolution_Image_Synthesis_with_Latent_Diffusion_Models_Robin_Rombach_et_al.pdf)\]

### PEFT

- LoRA: 2106.09685. **LoRA: Low-Rank Adaptation of Large Language Models**. Edward J. Hu et al | \[[abs](https://arxiv.org/abs/2106.09685)\] \[[pdf](../pdfs/2106.09685_LoRA#_Low-Rank_Adaptation_of_Large_Language_Models_Edward_J_Hu_et_al.pdf)\]
- ViT-Adapter: 2205.08534. **Vision Transformer Adapter for Dense Predictions**. Zhe Chen et al | \[[abs](https://arxiv.org/abs/2205.08534)\] \[[pdf](../pdfs/2205.08534_Vision_Transformer_Adapter_for_Dense_Predictions_Zhe_Chen_et_al.pdf)\]
- 2303.10512. **Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning**. Qingru Zhang et al | \[[abs](https://arxiv.org/abs/2303.10512)\] \[[pdf](../pdfs/2303.10512_Adaptive_Budget_Allocation_for_Parameter-Efficient_Fine-Tuning_Qingru_Zhang_et_al.pdf)\]
- QLoRA: 2305.14314. **QLoRA: Efficient Finetuning of Quantized LLMs**. Tim Dettmers et al | \[[abs](https://arxiv.org/abs/2305.14314)\] \[[pdf](../pdfs/2305.14314_QLoRA#_Efficient_Finetuning_of_Quantized_LLMs_Tim_Dettmers_et_al.pdf)\]

## 自动驾驶

### BEV

- LSS: {{https://arxiv.org/abs/2008.05711}}
- BevDet: {{https://arxiv.org/abs/2112.11790}}
- BevVerse: {{https://arxiv.org/abs/2205.09743}}
- BevFormer: {{https://arxiv.org/abs/2203.17270}}

### 占据网络

### 端到端

- UniAD: 2212.10156. **Planning-oriented Autonomous Driving**. Yihan Hu et al | \[[abs](https://arxiv.org/abs/2212.10156)\] \[[pdf](../pdfs/2212.10156_Planning-oriented_Autonomous_Driving_Yihan_Hu_et_al.pdf)\]
- Survey: 2306.16927. **End-to-end Autonomous Driving: Challenges and Frontiers**. Li Chen et al | \[[abs](https://arxiv.org/abs/2306.16927)\] \[[pdf](../pdfs/2306.16927_End-to-end_Autonomous_Driving#_Challenges_and_Frontiers_Li_Chen_et_al.pdf)\]

### 场景理解 (LLM+Vision)

### 世界模型 (predict next frame)