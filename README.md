# LiteHan ✨

LiteHan 是一个收集常用 **1000、3500、7000 汉字** 以及常用符号的仓库，旨在帮助开发者快速生成 **精简化字体文件**，减少字体体积，提升应用性能。

## 🏷️ 项目徽章

![License](https://img.shields.io/github/license/cheungxiongwei/LiteHan?color=blue)
![Stars](https://img.shields.io/github/stars/cheungxiongwei/LiteHan?style=social)
![Issues](https://img.shields.io/github/issues/cheungxiongwei/LiteHan?color=orange)
![Forks](https://img.shields.io/github/forks/cheungxiongwei/LiteHan?style=social)

## 📂 仓库内容

- **1000 常用汉字**
- **3500 常用汉字**
- **7000 通用汉字**
- **常用符号集**

这些文件可用于生成轻量化的字体文件，适合前端项目、移动应用或嵌入式设备。

## 📑 Han 文件格式

文件采用简洁的行式结构：

```
符号
汉字
```

每一行包含一系列符号或汉字，方便解析与处理。

## 🔗 下载地址

- [3500 常用汉字 & 7000 通用汉字](https://faculty.blcu.edu.cn/xinghb/zh_CN/article/167473/content/1045.htm)

## 🎯 使用场景

- 前端项目中减少字体包大小
- 移动应用优化加载速度
- 嵌入式设备节省存储空间
- 字体子集化处理

## 🚀 快速开始

1. 克隆仓库：
   ```bash
   git clone https://github.com/cheungxiongwei/LiteHan.git
   ```
2. 根据需求选择对应的汉字文件
3. 使用字体子集化工具生成精简字体
   你可以借助 fonttools 提供的 pyftsubset 来生成仅包含所需字符的精简字体文件，从而显著减少字体体积。

   3.1 安装依赖
   ```sh
   pip install fonttools
   ```

   3.2 基于字符文件生成子集字体
   以下示例基于 `3500.han` 字符集文件：
   ```sh
   # 生成精简版 TTF
   pyftsubset input.ttf \
     --text-file=3500.han \
     --output-file=subset3500.ttf

   # 生成精简版 WOFF2
   pyftsubset input.ttf \
     --text-file=3500.han \
     --flavor=woff2 \
     --output-file=subset.woff2
   ```

   3.3 使用 Unicode 范围生成子集字体
   适用于连续区段（如 CJK、标点、全角字符等）：
   ```
   # 提取常用汉字区段（CJK Unified Ideographs）
   pyftsubset input.ttf \
   --unicodes=U+4E00-9FFF \
   --output-file=subset-cjk.ttf

   # 提取多个 Unicode 范围，用逗号分隔多个区段
   pyftsubset input.ttf \
   --unicodes=U+4E00-9FFF,U+3000-303F,U+FF00-FFEF \
   --output-file=subset-multi.ttf
   ```

> 除了 fonttools，你也可以使用 FontForge 来进行字体编辑与子集化。FontForge 是一款开源的图形化字体编辑器，支持 TTF/OTF/SVG 等多种格式，并提供脚本接口（Python/SFD）用于自动化处理。 它适合需要可视化调整字形、手动检查轮廓或进行更复杂字体编辑的场景。

## 常用 Unicode 范围参考
| 字符集 | Unicode 范围 |
|-------|--------------|
| 基本汉字（CJK Unified Ideographs） | `U+4E00–9FFF` |
| 扩展 A | `U+3400–4DBF` |
| 扩展 B | `U+20000–2A6DF` |
| 扩展 C–G | `U+2A700–2EBEF` |
| 全角字符（Fullwidth Forms） | `U+FF00–FFEF` |
| 标点符号（CJK Symbols & Punctuation） | `U+3000–303F` |
| Emoji 基本区段 | `U+1F300–1F5FF` |

## 📊 效果展示

| 集合类型 | 汉字数量 | 文件大小 | 用途定位 |
|----------|----------|----------|----------|
| 原始字体 | 全量汉字 | 12.40 MB | 未优化，体积庞大 |
| 1000 基础常用 | 1000 | 0.25 MB | 极简场景，UI/嵌入式 |
| 3500 常用 | 3500 | 0.94 MB | 日常交流、教育、通用应用 |
| 7000 通用 | 7000 | 1.96 MB | 学术、专业文献、广覆盖 |

![](chart.webp)

## ❤️ 致谢

本仓库数据来源于北京语言大学相关资源，感谢学术界的支持。