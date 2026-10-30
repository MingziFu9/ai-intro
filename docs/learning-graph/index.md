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

图谱共有 **170 个概念、214 条先修关系**，概念按章排列，颜色表示 11 个类别（基础概念、搜索与推理、知识表示、机器学习、深度学习、语言与大模型、计算机视觉、语音技术、强化学习与智能体、行业应用、伦理与法规）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

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

??? note "第 5 章 语言与大模型（26 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [自然语言处理](../appendix/glossary.md#g-自然语言处理) | 语言与大模型 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [分词](../appendix/glossary.md#g-分词) | 语言与大模型 | [自然语言处理](../appendix/glossary.md#g-自然语言处理) |
    | [最大匹配法](../appendix/glossary.md#g-最大匹配法) | 语言与大模型 | [分词](../appendix/glossary.md#g-分词) |
    | [独热编码](../appendix/glossary.md#g-独热编码) | 语言与大模型 | [特征](../appendix/glossary.md#g-特征) |
    | [词向量](../appendix/glossary.md#g-词向量) | 语言与大模型 | [独热编码](../appendix/glossary.md#g-独热编码)、[深度学习](../appendix/glossary.md#g-深度学习) |
    | [余弦相似度](../appendix/glossary.md#g-余弦相似度) | 语言与大模型 | [词向量](../appendix/glossary.md#g-词向量) |
    | [语言模型](../appendix/glossary.md#g-语言模型) | 语言与大模型 | [自然语言处理](../appendix/glossary.md#g-自然语言处理)、[自监督学习](../appendix/glossary.md#g-自监督学习) |
    | [自回归生成](../appendix/glossary.md#g-自回归生成) | 语言与大模型 | [语言模型](../appendix/glossary.md#g-语言模型) |
    | [Token](../appendix/glossary.md#g-Token) | 语言与大模型 | [语言模型](../appendix/glossary.md#g-语言模型) |
    | [上下文长度](../appendix/glossary.md#g-上下文长度) | 语言与大模型 | [Token](../appendix/glossary.md#g-Token) |
    | [温度](../appendix/glossary.md#g-温度) | 语言与大模型 | [语言模型](../appendix/glossary.md#g-语言模型) |
    | [注意力机制](../appendix/glossary.md#g-注意力机制) | 语言与大模型 | [循环神经网络](../appendix/glossary.md#g-循环神经网络)、[词向量](../appendix/glossary.md#g-词向量) |
    | [Transformer](../appendix/glossary.md#g-Transformer) | 语言与大模型 | [注意力机制](../appendix/glossary.md#g-注意力机制)、[GPU](../appendix/glossary.md#g-GPU) |
    | [大语言模型](../appendix/glossary.md#g-大语言模型) | 语言与大模型 | [Transformer](../appendix/glossary.md#g-Transformer)、[大模型](../appendix/glossary.md#g-大模型)、[生成式人工智能](../appendix/glossary.md#g-生成式人工智能) |
    | [预训练](../appendix/glossary.md#g-预训练) | 语言与大模型 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [基座模型](../appendix/glossary.md#g-基座模型) | 语言与大模型 | [预训练](../appendix/glossary.md#g-预训练) |
    | [指令微调](../appendix/glossary.md#g-指令微调) | 语言与大模型 | [基座模型](../appendix/glossary.md#g-基座模型) |
    | [人类反馈强化学习](../appendix/glossary.md#g-人类反馈强化学习) | 语言与大模型 | [指令微调](../appendix/glossary.md#g-指令微调) |
    | [对齐](../appendix/glossary.md#g-对齐) | 语言与大模型 | [人类反馈强化学习](../appendix/glossary.md#g-人类反馈强化学习) |
    | [思维链](../appendix/glossary.md#g-思维链) | 语言与大模型 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [推理模型](../appendix/glossary.md#g-推理模型) | 语言与大模型 | [思维链](../appendix/glossary.md#g-思维链) |
    | [提示词](../appendix/glossary.md#g-提示词) | 语言与大模型 | [大语言模型](../appendix/glossary.md#g-大语言模型) |
    | [提示词工程](../appendix/glossary.md#g-提示词工程) | 语言与大模型 | [提示词](../appendix/glossary.md#g-提示词) |
    | [幻觉](../appendix/glossary.md#g-幻觉) | 语言与大模型 | [自回归生成](../appendix/glossary.md#g-自回归生成) |
    | [知识截止](../appendix/glossary.md#g-知识截止) | 语言与大模型 | [预训练](../appendix/glossary.md#g-预训练) |
    | [检索增强生成](../appendix/glossary.md#g-检索增强生成) | 语言与大模型 | [幻觉](../appendix/glossary.md#g-幻觉)、[余弦相似度](../appendix/glossary.md#g-余弦相似度) |

??? note "第 6 章 计算机视觉（25 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [计算机视觉](../appendix/glossary.md#g-计算机视觉) | 计算机视觉 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [像素](../appendix/glossary.md#g-像素) | 计算机视觉 | [计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [分辨率](../appendix/glossary.md#g-分辨率) | 计算机视觉 | [像素](../appendix/glossary.md#g-像素) |
    | [灰度](../appendix/glossary.md#g-灰度) | 计算机视觉 | [像素](../appendix/glossary.md#g-像素) |
    | [RGB 颜色](../appendix/glossary.md#g-RGB-颜色) | 计算机视觉 | [像素](../appendix/glossary.md#g-像素) |
    | [通道](../appendix/glossary.md#g-通道) | 计算机视觉 | [RGB 颜色](../appendix/glossary.md#g-RGB-颜色) |
    | [卷积核](../appendix/glossary.md#g-卷积核) | 计算机视觉 | [像素](../appendix/glossary.md#g-像素) |
    | [卷积](../appendix/glossary.md#g-卷积) | 计算机视觉 | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络)、[卷积核](../appendix/glossary.md#g-卷积核) |
    | [池化](../appendix/glossary.md#g-池化) | 计算机视觉 | [卷积](../appendix/glossary.md#g-卷积) |
    | [图像分类](../appendix/glossary.md#g-图像分类) | 计算机视觉 | [卷积神经网络](../appendix/glossary.md#g-卷积神经网络)、[分类](../appendix/glossary.md#g-分类) |
    | [目标检测](../appendix/glossary.md#g-目标检测) | 计算机视觉 | [图像分类](../appendix/glossary.md#g-图像分类) |
    | [图像分割](../appendix/glossary.md#g-图像分割) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [视频分析](../appendix/glossary.md#g-视频分析) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [交并比](../appendix/glossary.md#g-交并比) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [数据标注](../appendix/glossary.md#g-数据标注) | 计算机视觉 | [标签](../appendix/glossary.md#g-标签) |
    | [标注规范](../appendix/glossary.md#g-标注规范) | 计算机视觉 | [数据标注](../appendix/glossary.md#g-数据标注) |
    | [人脸识别](../appendix/glossary.md#g-人脸识别) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测)、[余弦相似度](../appendix/glossary.md#g-余弦相似度) |
    | [活体检测](../appendix/glossary.md#g-活体检测) | 计算机视觉 | [人脸识别](../appendix/glossary.md#g-人脸识别) |
    | [文字识别](../appendix/glossary.md#g-文字识别) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测) |
    | [工业质检](../appendix/glossary.md#g-工业质检) | 计算机视觉 | [目标检测](../appendix/glossary.md#g-目标检测)、[召回率](../appendix/glossary.md#g-召回率) |
    | [扩散模型](../appendix/glossary.md#g-扩散模型) | 计算机视觉 | [生成式人工智能](../appendix/glossary.md#g-生成式人工智能) |
    | [文生图](../appendix/glossary.md#g-文生图) | 计算机视觉 | [扩散模型](../appendix/glossary.md#g-扩散模型)、[提示词](../appendix/glossary.md#g-提示词) |
    | [多模态大模型](../appendix/glossary.md#g-多模态大模型) | 计算机视觉 | [大语言模型](../appendix/glossary.md#g-大语言模型)、[计算机视觉](../appendix/glossary.md#g-计算机视觉) |
    | [显式标识](../appendix/glossary.md#g-显式标识) | 计算机视觉 | [文生图](../appendix/glossary.md#g-文生图) |
    | [隐式标识](../appendix/glossary.md#g-隐式标识) | 计算机视觉 | [文生图](../appendix/glossary.md#g-文生图) |

??? note "第 7 章 语音技术（20 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [频率](../appendix/glossary.md#g-频率) | 语音技术 | [人工智能](../appendix/glossary.md#g-人工智能) |
    | [振幅](../appendix/glossary.md#g-振幅) | 语音技术 | [频率](../appendix/glossary.md#g-频率) |
    | [波形](../appendix/glossary.md#g-波形) | 语音技术 | [振幅](../appendix/glossary.md#g-振幅) |
    | [采样](../appendix/glossary.md#g-采样) | 语音技术 | [波形](../appendix/glossary.md#g-波形) |
    | [采样率](../appendix/glossary.md#g-采样率) | 语音技术 | [采样](../appendix/glossary.md#g-采样) |
    | [量化](../appendix/glossary.md#g-量化) | 语音技术 | [采样](../appendix/glossary.md#g-采样) |
    | [频谱](../appendix/glossary.md#g-频谱) | 语音技术 | [频率](../appendix/glossary.md#g-频率)、[波形](../appendix/glossary.md#g-波形) |
    | [共振峰](../appendix/glossary.md#g-共振峰) | 语音技术 | [频谱](../appendix/glossary.md#g-频谱) |
    | [语谱图](../appendix/glossary.md#g-语谱图) | 语音技术 | [频谱](../appendix/glossary.md#g-频谱) |
    | [语音识别](../appendix/glossary.md#g-语音识别) | 语音技术 | [语谱图](../appendix/glossary.md#g-语谱图)、[语言模型](../appendix/glossary.md#g-语言模型)、[端到端](../appendix/glossary.md#g-端到端) |
    | [端到端](../appendix/glossary.md#g-端到端) | 语音技术 | [深度学习](../appendix/glossary.md#g-深度学习) |
    | [字错率](../appendix/glossary.md#g-字错率) | 语音技术 | [语音识别](../appendix/glossary.md#g-语音识别) |
    | [语音唤醒](../appendix/glossary.md#g-语音唤醒) | 语音技术 | [语音识别](../appendix/glossary.md#g-语音识别)、[召回率](../appendix/glossary.md#g-召回率) |
    | [语音合成](../appendix/glossary.md#g-语音合成) | 语音技术 | [语音识别](../appendix/glossary.md#g-语音识别)、[多音字](../appendix/glossary.md#g-多音字)、[自回归生成](../appendix/glossary.md#g-自回归生成) |
    | [多音字](../appendix/glossary.md#g-多音字) | 语音技术 | — |
    | [声纹](../appendix/glossary.md#g-声纹) | 语音技术 | [语谱图](../appendix/glossary.md#g-语谱图) |
    | [声纹识别](../appendix/glossary.md#g-声纹识别) | 语音技术 | [声纹](../appendix/glossary.md#g-声纹)、[人脸识别](../appendix/glossary.md#g-人脸识别) |
    | [语音克隆](../appendix/glossary.md#g-语音克隆) | 语音技术 | [语音合成](../appendix/glossary.md#g-语音合成)、[声纹](../appendix/glossary.md#g-声纹) |
    | [语音大模型](../appendix/glossary.md#g-语音大模型) | 语音技术 | [语音识别](../appendix/glossary.md#g-语音识别)、[语音合成](../appendix/glossary.md#g-语音合成)、[Token](../appendix/glossary.md#g-Token) |
    | [同声传译](../appendix/glossary.md#g-同声传译) | 语音技术 | [语音大模型](../appendix/glossary.md#g-语音大模型) |

<!-- graph:end -->
