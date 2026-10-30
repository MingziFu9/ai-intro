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

图谱共有 **99 个概念、121 条先修关系**，概念按章排列，颜色表示 11 个类别（基础概念、搜索与推理、知识表示、机器学习、深度学习、语言与大模型、计算机视觉、语音技术、强化学习与智能体、行业应用、伦理与法规）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 人工智能概述（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [人工智能](../appendix/glossary.md#g-人工智能) | 基础概念 | — |
    | [图灵测试](../appendix/glossary.md#g-图灵测试) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [中文屋](../appendix/glossary.md#g-中文屋) | 基础概念 | [图灵测试](../appendix/glossary.md#g-图灵测试) |
    | [弱人工智能](../appendix/glossary.md#g-弱人工智能) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [强人工智能](../appendix/glossary.md#g-强人工智能) | 基础概念 | [弱人工智能](../appendix/glossary.md#g-弱人工智能) |
    | [通用人工智能](../appendix/glossary.md#g-通用人工智能) | 基础概念 | [强人工智能](../appendix/glossary.md#g-强人工智能) |
    | [达特茅斯会议](../appendix/glossary.md#g-达特茅斯会议) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [三次浪潮](../appendix/glossary.md#g-三次浪潮) | 基础概念 | [达特茅斯会议](../appendix/glossary.md#g-达特茅斯会议)、[符号主义](../appendix/glossary.md#g-符号主义)、[连接主义](../appendix/glossary.md#g-连接主义) |
    | [符号主义](../appendix/glossary.md#g-符号主义) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [连接主义](../appendix/glossary.md#g-连接主义) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [行为主义](../appendix/glossary.md#g-行为主义) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [数据](../appendix/glossary.md#g-数据) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [算法](../appendix/glossary.md#g-算法) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [算力](../appendix/glossary.md#g-算力) | 基础概念 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [人工智能三要素](../appendix/glossary.md#g-人工智能三要素) | 基础概念 | [数据](../appendix/glossary.md#g-数据)、[算法](../appendix/glossary.md#g-算法)、[算力](../appendix/glossary.md#g-算力) |
    | [大模型](../appendix/glossary.md#g-大模型) | 基础概念 | [三次浪潮](../appendix/glossary.md#g-三次浪潮)、[人工智能三要素](../appendix/glossary.md#g-人工智能三要素) |
    | [生成式人工智能](../appendix/glossary.md#g-生成式人工智能) | 基础概念 | [大模型](../appendix/glossary.md#g-大模型) |
    | [东数西算](../appendix/glossary.md#g-东数西算) | 基础概念 | [算力](../appendix/glossary.md#g-算力) |
    | [人工智能产业链](../appendix/glossary.md#g-人工智能产业链) | 基础概念 | [人工智能三要素](../appendix/glossary.md#g-人工智能三要素) |
    | [人工智能训练师](../appendix/glossary.md#g-人工智能训练师) | 基础概念 | [人工智能产业链](../appendix/glossary.md#g-人工智能产业链) |

??? note "第 2 章 搜索与知识表示（25 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [状态](../appendix/glossary.md#g-状态) | 搜索与推理 | [问题求解](../appendix/glossary.md#g-问题求解) |
    | [问题求解](../appendix/glossary.md#g-问题求解) | 搜索与推理 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [状态空间](../appendix/glossary.md#g-状态空间) | 搜索与推理 | [状态](../appendix/glossary.md#g-状态) |
    | [搜索树](../appendix/glossary.md#g-搜索树) | 搜索与推理 | [状态空间](../appendix/glossary.md#g-状态空间) |
    | [组合爆炸](../appendix/glossary.md#g-组合爆炸) | 搜索与推理 | [状态空间](../appendix/glossary.md#g-状态空间) |
    | [盲目搜索](../appendix/glossary.md#g-盲目搜索) | 搜索与推理 | [搜索树](../appendix/glossary.md#g-搜索树) |
    | [广度优先搜索](../appendix/glossary.md#g-广度优先搜索) | 搜索与推理 | [盲目搜索](../appendix/glossary.md#g-盲目搜索) |
    | [深度优先搜索](../appendix/glossary.md#g-深度优先搜索) | 搜索与推理 | [盲目搜索](../appendix/glossary.md#g-盲目搜索) |
    | [启发函数](../appendix/glossary.md#g-启发函数) | 搜索与推理 | [状态空间](../appendix/glossary.md#g-状态空间) |
    | [启发式搜索](../appendix/glossary.md#g-启发式搜索) | 搜索与推理 | [启发函数](../appendix/glossary.md#g-启发函数)、[广度优先搜索](../appendix/glossary.md#g-广度优先搜索) |
    | [A* 搜索](../appendix/glossary.md#g-A*-搜索) | 搜索与推理 | [启发式搜索](../appendix/glossary.md#g-启发式搜索) |
    | [博弈搜索](../appendix/glossary.md#g-博弈搜索) | 搜索与推理 | [搜索树](../appendix/glossary.md#g-搜索树) |
    | [极小极大算法](../appendix/glossary.md#g-极小极大算法) | 搜索与推理 | [博弈搜索](../appendix/glossary.md#g-博弈搜索) |
    | [剪枝](../appendix/glossary.md#g-剪枝) | 搜索与推理 | [极小极大算法](../appendix/glossary.md#g-极小极大算法) |
    | [知识表示](../appendix/glossary.md#g-知识表示) | 知识表示 | [符号主义](../appendix/glossary.md#g-符号主义) |
    | [产生式规则](../appendix/glossary.md#g-产生式规则) | 知识表示 | [知识表示](../appendix/glossary.md#g-知识表示) |
    | [语义网络](../appendix/glossary.md#g-语义网络) | 知识表示 | [知识表示](../appendix/glossary.md#g-知识表示) |
    | [知识图谱](../appendix/glossary.md#g-知识图谱) | 知识表示 | [语义网络](../appendix/glossary.md#g-语义网络) |
    | [三元组](../appendix/glossary.md#g-三元组) | 知识表示 | [知识图谱](../appendix/glossary.md#g-知识图谱) |
    | [推理](../appendix/glossary.md#g-推理) | 知识表示 | [知识表示](../appendix/glossary.md#g-知识表示) |
    | [正向推理](../appendix/glossary.md#g-正向推理) | 知识表示 | [推理](../appendix/glossary.md#g-推理)、[产生式规则](../appendix/glossary.md#g-产生式规则) |
    | [反向推理](../appendix/glossary.md#g-反向推理) | 知识表示 | [推理](../appendix/glossary.md#g-推理)、[产生式规则](../appendix/glossary.md#g-产生式规则) |
    | [专家系统](../appendix/glossary.md#g-专家系统) | 知识表示 | [产生式规则](../appendix/glossary.md#g-产生式规则)、[推理](../appendix/glossary.md#g-推理) |
    | [知识库](../appendix/glossary.md#g-知识库) | 知识表示 | [专家系统](../appendix/glossary.md#g-专家系统) |
    | [推理机](../appendix/glossary.md#g-推理机) | 知识表示 | [专家系统](../appendix/glossary.md#g-专家系统) |

??? note "第 3 章 机器学习入门（30 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [机器学习](../appendix/glossary.md#g-机器学习) | 机器学习 | [人工智能](../appendix/glossary.md#g-人工智能)、[专家系统](../appendix/glossary.md#g-专家系统) |
    | [样本](../appendix/glossary.md#g-样本) | 机器学习 | [机器学习](../appendix/glossary.md#g-机器学习)、[数据](../appendix/glossary.md#g-数据) |
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
    | [K 近邻](../appendix/glossary.md#g-K-近邻) | 机器学习 | [分类](../appendix/glossary.md#g-分类)、[特征](../appendix/glossary.md#g-特征)、[算法](../appendix/glossary.md#g-算法) |
    | [决策树](../appendix/glossary.md#g-决策树) | 机器学习 | [分类](../appendix/glossary.md#g-分类) |
    | [聚类](../appendix/glossary.md#g-聚类) | 机器学习 | [无监督学习](../appendix/glossary.md#g-无监督学习) |
    | [K 均值](../appendix/glossary.md#g-K-均值) | 机器学习 | [聚类](../appendix/glossary.md#g-聚类) |
    | [欠拟合](../appendix/glossary.md#g-欠拟合) | 机器学习 | [过拟合](../appendix/glossary.md#g-过拟合) |
    | [过拟合](../appendix/glossary.md#g-过拟合) | 机器学习 | [泛化能力](../appendix/glossary.md#g-泛化能力)、[训练集](../appendix/glossary.md#g-训练集)、[训练轮次](../appendix/glossary.md#g-训练轮次) |
    | [准确率](../appendix/glossary.md#g-准确率) | 机器学习 | [分类](../appendix/glossary.md#g-分类) |
    | [类别不平衡](../appendix/glossary.md#g-类别不平衡) | 机器学习 | [准确率](../appendix/glossary.md#g-准确率) |
    | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) | 机器学习 | [准确率](../appendix/glossary.md#g-准确率) |
    | [精确率](../appendix/glossary.md#g-精确率) | 机器学习 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [召回率](../appendix/glossary.md#g-召回率) | 机器学习 | [混淆矩阵](../appendix/glossary.md#g-混淆矩阵) |
    | [阈值](../appendix/glossary.md#g-阈值) | 机器学习 | [精确率](../appendix/glossary.md#g-精确率)、[召回率](../appendix/glossary.md#g-召回率) |
    | [自动机器学习](../appendix/glossary.md#g-自动机器学习) | 机器学习 | [模型](../appendix/glossary.md#g-模型) |

??? note "第 4 章 深度学习入门（24 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [人工神经元](../appendix/glossary.md#g-人工神经元) | 深度学习 | [连接主义](../appendix/glossary.md#g-连接主义) |
    | [权重](../appendix/glossary.md#g-权重) | 深度学习 | [人工神经元](../appendix/glossary.md#g-人工神经元) |
    | [偏置](../appendix/glossary.md#g-偏置) | 深度学习 | [人工神经元](../appendix/glossary.md#g-人工神经元) |
    | [激活函数](../appendix/glossary.md#g-激活函数) | 深度学习 | [人工神经元](../appendix/glossary.md#g-人工神经元) |
    | [感知机](../appendix/glossary.md#g-感知机) | 深度学习 | [人工神经元](../appendix/glossary.md#g-人工神经元) |
    | [输入层](../appendix/glossary.md#g-输入层) | 深度学习 | — |
    | [隐藏层](../appendix/glossary.md#g-隐藏层) | 深度学习 | [人工神经元](../appendix/glossary.md#g-人工神经元) |
    | [输出层](../appendix/glossary.md#g-输出层) | 深度学习 | — |
    | [多层神经网络](../appendix/glossary.md#g-多层神经网络) | 深度学习 | [感知机](../appendix/glossary.md#g-感知机)、[输入层](../appendix/glossary.md#g-输入层)、[隐藏层](../appendix/glossary.md#g-隐藏层)、[输出层](../appendix/glossary.md#g-输出层) |
    | [深度学习](../appendix/glossary.md#g-深度学习) | 深度学习 | [多层神经网络](../appendix/glossary.md#g-多层神经网络)、[机器学习](../appendix/glossary.md#g-机器学习)、[特征](../appendix/glossary.md#g-特征) |
    | [损失函数](../appendix/glossary.md#g-损失函数) | 深度学习 | [误差](../appendix/glossary.md#g-误差) |
    | [梯度下降](../appendix/glossary.md#g-梯度下降) | 深度学习 | [损失函数](../appendix/glossary.md#g-损失函数)、[权重](../appendix/glossary.md#g-权重) |
    | [学习率](../appendix/glossary.md#g-学习率) | 深度学习 | [梯度下降](../appendix/glossary.md#g-梯度下降) |
    | [局部最低点](../appendix/glossary.md#g-局部最低点) | 深度学习 | [梯度下降](../appendix/glossary.md#g-梯度下降) |
    | [反向传播](../appendix/glossary.md#g-反向传播) | 深度学习 | [梯度下降](../appendix/glossary.md#g-梯度下降) |
    | [训练轮次](../appendix/glossary.md#g-训练轮次) | 深度学习 | [训练集](../appendix/glossary.md#g-训练集) |
    | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络) | 深度学习 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [循环神经网络](../appendix/glossary.md#g-循环神经网络) | 深度学习 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [长短期记忆网络](../appendix/glossary.md#g-长短期记忆网络) | 深度学习 | [循环神经网络](../appendix/glossary.md#g-循环神经网络) |
    | [梯度消失](../appendix/glossary.md#g-梯度消失) | 深度学习 | [反向传播](../appendix/glossary.md#g-反向传播)、[激活函数](../appendix/glossary.md#g-激活函数) |
    | [深度学习框架](../appendix/glossary.md#g-深度学习框架) | 深度学习 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [GPU](../appendix/glossary.md#g-GPU) | 深度学习 | [算力](../appendix/glossary.md#g-算力) |
    | [专用 AI 芯片](../appendix/glossary.md#g-专用-AI-芯片) | 深度学习 | [GPU](../appendix/glossary.md#g-GPU) |
    | [神经网络处理器](../appendix/glossary.md#g-神经网络处理器) | 深度学习 | [专用 AI 芯片](../appendix/glossary.md#g-专用-AI-芯片) |

<!-- graph:end -->
