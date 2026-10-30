# 人工智能导论

**面向成人教育人工智能技术应用专业（专科）的《人工智能导论》教材**

<!-- 书名、课程信息框和“目录与实验”表由 python tools/course.py sync 根据 course.yml 生成；全书概览表由 python tools/book_stats.py 生成 -->

<!-- course:start -->
!!! abstract "课程信息"
    2 学分 · 36 学时 · 第 1 学期 · 9 章 · 18 个体验 · 期末闭卷
<!-- course:end -->

## 这本书讲什么

刷脸支付、导航路线、购物网站的“猜你喜欢”，以及 DeepSeek、豆包、通义千问、文心一言这些大模型对话产品，背后都是人工智能技术。这本书给人工智能技术应用专业的新同学画一张“地图”：人工智能有哪些主要分支，每个分支解决什么问题、大致怎样工作、用在哪些行业，又带来哪些伦理和法律问题。

全书从人工智能的概念和发展历程讲起，依次介绍搜索与知识表示、机器学习、深度学习、自然语言处理与大模型、计算机视觉、语音技术、强化学习与智能体，最后讨论行业应用、伦理与法规。每一章都会告诉你，这部分内容在后续哪一门专业课里深入学习。

## 本书的特点

- **不写代码、不推导公式**：每个技术只讲三件事：解决什么问题、大致怎样工作、身边哪里在用。本课 36 学时全部是理论学时（线上 29、线下 7）；
- **每章两个在线体验**：用浏览器里的交互动画或国产 AI 产品亲手试一试，不需要安装软件；
- **在线练习**：每章课后的单选、多选和判断题可以在网页上直接作答并查看解析，书末附两套[模拟卷](exam/index.md)，题型与期末闭卷考试一致；
- **连接后续课程**：每章末尾的“深入学习”指向本专业其他教材的对应章节，[附录 C](appendix/c-course-map.md) 给出完整的课程地图。

## 全书概览

<!-- stats:start -->

| 章 | 正文字数 | 体验 | 课后练习<br>（可在线作答） | 术语 | 参考文献 | 交互动画 |
|---|---|---|---|---|---|---|
| [第 1 章](chapters/01-overview/index.md) | 1.1 万 | 2 | 30（25） | 20 | 11 | 2 |
| [第 2 章](chapters/02-search-knowledge/index.md) | 1.1 万 | 2 | 30（25） | 25 | 10 | 3 |
| [第 3 章](chapters/03-machine-learning/index.md) | 1.3 万 | 2 | 30（25） | 30 | 10 | 3 |
| [第 4 章](chapters/04-deep-learning/index.md) | 1.0 万 | 2 | 30（25） | 24 | 12 | 3 |
| [第 5 章](chapters/05-nlp-llm/index.md) | 0.0 万 | 2 | 0（0） | 0 | 0 | 0 |
| [第 6 章](chapters/06-computer-vision/index.md) | 0.0 万 | 2 | 0（0） | 0 | 0 | 0 |
| [第 7 章](chapters/07-speech/index.md) | 0.0 万 | 2 | 0（0） | 0 | 0 | 0 |
| [第 8 章](chapters/08-rl-agents/index.md) | 0.0 万 | 2 | 0（0） | 0 | 0 | 0 |
| [第 9 章](chapters/09-applications-ethics/index.md) | 0.0 万 | 2 | 0（0） | 0 | 0 | 0 |
| **合计** | **4.6 万** | **18** | **120（100）** | **99** | **43** | **11** |

正文字数只统计汉字，不含代码和课后练习；单选、多选和判断题可以在网页上直接作答。配套学习资源：[交互动画](sims/index.md) 11 个 · [学习图谱](learning-graph/index.md) 99 个概念 · [常见问题](faq/index.md) 0 问 · [术语表](appendix/glossary.md) 99 条。

<!-- stats:end -->

## 目录与在线体验

<!-- toc:start -->
| 章节 | 体验 |
|---|---|
| [第 1 章 人工智能概述](chapters/01-overview/index.md) | 体验 1-1 图灵测试小游戏<br>体验 1-2 国产大模型初体验 |
| [第 2 章 搜索、知识表示与专家系统](chapters/02-search-knowledge/index.md) | 体验 2-1 迷宫寻路：比一比三种搜索<br>体验 2-2 动物识别专家系统 |
| [第 3 章 机器学习入门](chapters/03-machine-learning/index.md) | 体验 3-1 分类与聚类<br>体验 3-2 过拟合与混淆矩阵 |
| [第 4 章 深度学习入门](chapters/04-deep-learning/index.md) | 体验 4-1 神经元与梯度下降<br>体验 4-2 手写数字识别 |
| [第 5 章 自然语言处理与大模型](chapters/05-nlp-llm/index.md) | 体验 5-1 提示词工程练习<br>体验 5-2 下一个词预测与幻觉核查 |
| [第 6 章 计算机视觉](chapters/06-computer-vision/index.md) | 体验 6-1 卷积滤镜<br>体验 6-2 识图、OCR 与文生图 |
| [第 7 章 语音技术](chapters/07-speech/index.md) | 体验 7-1 声音的模样<br>体验 7-2 语音识别与合成 |
| [第 8 章 强化学习、生成式 AI 与智能体](chapters/08-rl-agents/index.md) | 体验 8-1 Q 学习格子世界<br>体验 8-2 用扣子或 Dify 搭一个“课程助教”智能体 |
| [第 9 章 行业应用、伦理与法规](chapters/09-applications-ethics/index.md) | 体验 9-1 信息茧房模拟<br>体验 9-2 AI 生成内容合规检查 |

附录：[A 在线平台与账号指南](appendix/a-platforms.md) · [B 人工智能大事年表](appendix/b-timeline.md) · [C 专业课程地图](appendix/c-course-map.md) · [D 术语表](appendix/glossary.md)
<!-- toc:end -->

## 配套资源

- [交互动画](sims/index.md)、[学习图谱](learning-graph/index.md)、[常见问题](faq/index.md)、[在线模拟卷](exam/index.md)
- 课件、教案和 Word/PDF 版教材：见仓库的 Releases 页面
