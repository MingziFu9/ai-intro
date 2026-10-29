---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **30 个概念、34 条先修关系**，概念按章排列，颜色表示 11 个类别（基础概念、搜索与推理、知识表示、机器学习、深度学习、语言与大模型、计算机视觉、语音技术、强化学习与智能体、行业应用、伦理与法规）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 3 章 机器学习入门（30 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机器学习](../appendix/glossary.md#g-机器学习) | 机器学习 | — |
    | [样本](../appendix/glossary.md#g-样本) | 机器学习 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [特征](../appendix/glossary.md#g-特征) | 机器学习 | [样本](../appendix/glossary.md#g-样本) |
    | [标签](../appendix/glossary.md#g-标签) | 机器学习 | [样本](../appendix/glossary.md#g-样本) |
    | [模型](../appendix/glossary.md#g-模型) | 机器学习 | [机器学习](../appendix/glossary.md#g-机器学习)、[特征](../appendix/glossary.md#g-特征) |
    | [特征工程](../appendix/glossary.md#g-特征工程) | 机器学习 | [特征](../appendix/glossary.md#g-特征) |
    | [训练集](../appendix/glossary.md#g-训练集) | 机器学习 | [样本](../appendix/glossary.md#g-样本) |
    | [测试集](../appendix/glossary.md#g-测试集) | 机器学习 | [样本](../appendix/glossary.md#g-样本) |
    | [验证集](../appendix/glossary.md#g-验证集) | 机器学习 | [训练集](../appendix/glossary.md#g-训练集) |
    | [泛化能力](../appendix/glossary.md#g-泛化能力) | 机器学习 | [测试集](../appendix/glossary.md#g-测试集)、[模型](../appendix/glossary.md#g-模型) |
    | [监督学习](../appendix/glossary.md#g-监督学习) | 机器学习 | [标签](../appendix/glossary.md#g-标签) |
    | [无监督学习](../appendix/glossary.md#g-无监督学习) | 机器学习 | [机器学习](../appendix/glossary.md#g-机器学习) |
    | [自监督学习](../appendix/glossary.md#g-自监督学习) | 机器学习 | [监督学习](../appendix/glossary.md#g-监督学习) |
    | [回归](../appendix/glossary.md#g-回归) | 机器学习 | [监督学习](../appendix/glossary.md#g-监督学习) |
    | [线性回归](../appendix/glossary.md#g-线性回归) | 机器学习 | [回归](../appendix/glossary.md#g-回归) |
    | [误差](../appendix/glossary.md#g-误差) | 机器学习 | [线性回归](../appendix/glossary.md#g-线性回归) |
    | [分类](../appendix/glossary.md#g-分类) | 机器学习 | [监督学习](../appendix/glossary.md#g-监督学习) |
    | [K 近邻](../appendix/glossary.md#g-K-近邻) | 机器学习 | [分类](../appendix/glossary.md#g-分类)、[特征](../appendix/glossary.md#g-特征) |
    | [决策树](../appendix/glossary.md#g-决策树) | 机器学习 | [分类](../appendix/glossary.md#g-分类) |
    | [聚类](../appendix/glossary.md#g-聚类) | 机器学习 | [无监督学习](../appendix/glossary.md#g-无监督学习) |
    | [K 均值](../appendix/glossary.md#g-K-均值) | 机器学习 | [聚类](../appendix/glossary.md#g-聚类) |
    | [欠拟合](../appendix/glossary.md#g-欠拟合) | 机器学习 | [过拟合](../appendix/glossary.md#g-过拟合) |
    | [过拟合](../appendix/glossary.md#g-过拟合) | 机器学习 | [泛化能力](../appendix/glossary.md#g-泛化能力)、[训练集](../appendix/glossary.md#g-训练集) |
    | [准确率](../appendix/glossary.md#g-准确率) | 机器学习 | [分类](../appendix/glossary.md#g-分类) |
    | [类别不平衡](../appendix/glossary.md#g-类别不平衡) | 机器学习 | [准确率](../appendix/glossary.md#g-准确率) |
    | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) | 机器学习 | [准确率](../appendix/glossary.md#g-准确率) |
    | [精确率](../appendix/glossary.md#g-精确率) | 机器学习 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [召回率](../appendix/glossary.md#g-召回率) | 机器学习 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [阈值](../appendix/glossary.md#g-阈值) | 机器学习 | [精确率](../appendix/glossary.md#g-精确率)、[召回率](../appendix/glossary.md#g-召回率) |
    | [自动机器学习](../appendix/glossary.md#g-自动机器学习) | 机器学习 | [模型](../appendix/glossary.md#g-模型) |

<!-- graph:end -->
