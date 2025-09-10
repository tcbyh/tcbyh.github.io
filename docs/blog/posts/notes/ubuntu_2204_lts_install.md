---
date:
  created: 2024-12-26
categories:
  - 笔记&教程
---


# Ubuntu 22.04 LTS 系统安装


## 启动U盘制作 & 系统安装

- Ubuntu 下载：[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
- Ventoy 下载 & 制作：[https://www.ventoy.net/cn/download.html](https://www.ventoy.net/cn/download.html)
- Ubuntu 安装指南：[https://ubuntu.com/tutorials/install-ubuntu-desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop)

### 问题:

- 启动黑屏/横线 ===> 选 Safe (Graphics) 进入 [https://blog.csdn.net/weixin_44478317/article/details/142670119](https://blog.csdn.net/weixin_44478317/article/details/142670119)


## 软件源配置

### APT源

> https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

替换 `/etc/apt/sources.list`

```bash
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse

# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换
deb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
```

系统更新

```bash
sudo apt update && sudo apt upgrade -y
```

### Conda源

> https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

安装 conda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

替换 `~/.condarc`

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

### PyPI源：

命令行设置

```
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```


## 显卡驱动 & Cuda & CuDNN 安装

> https://gist.github.com/huxycn/a76cc4a99c6e06fece47cfef1f70f623


## 常用软件安装

- apt install
  - tree / vim / git
  - terminator
  - mpv：https://fruit.je/apt

- deb 直接安装
  - google-chrome
  - sougoupinyin
    - issue1: 安装失败 ==> 严格按照步骤安装: https://shurufa.sogou.com/linux/guide
    - issue2: 误切换繁体模式 ===> Ctrl + Shift + F 切换回简体模式
    - issue3: Chrome中无法使用输入法 ===> sudo apt install fcitx5-frontend-gtk4 https://zhuanlan.zhihu.com/p/1895373648698787278
  - code
  - feishu
  - easyconnect
  - cloudpc




