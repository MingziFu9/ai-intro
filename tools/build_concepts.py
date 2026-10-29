"""生成《人工智能导论》学习图谱概念表（大纲阶段）。

每行：概念 | 章 | 类别 | 先修（用概念名，| 分隔） | 深入学习去处
输出 learning-graph.csv（技能标准四列 + 章、深入学习）和 概念清单.md。
"""
import csv, sys, collections

CATS = {
    "FOUND": "基础概念", "SRCH": "搜索与推理", "KNOW": "知识表示",
    "ML": "机器学习", "DL": "深度学习", "NLP": "语言与大模型",
    "CV": "计算机视觉", "SPCH": "语音技术", "AGNT": "强化学习与智能体",
    "APP": "行业应用", "ETH": "伦理与法规",
}
CHAPTERS = ["", "人工智能概述", "搜索、知识表示与专家系统", "机器学习入门",
            "深度学习入门", "自然语言处理与大模型", "计算机视觉",
            "语音技术", "强化学习、生成式 AI 与智能体", "行业应用、伦理与法规"]

RAW = """
人工智能|1|FOUND||
图灵测试|1|FOUND|人工智能|
弱人工智能|1|FOUND|人工智能|
强人工智能|1|FOUND|弱人工智能|
达特茅斯会议|1|FOUND|人工智能|
符号主义|1|FOUND|人工智能|
连接主义|1|FOUND|人工智能|
行为主义|1|FOUND|人工智能|
人工智能三次浪潮|1|FOUND|达特茅斯会议|符号主义|连接主义|
数据|1|FOUND|人工智能|大数据；数据分析与处理
算法|1|FOUND|人工智能|
算力|1|FOUND|人工智能|开发框架
人工智能三要素|1|FOUND|数据|算法|算力|
大模型|1|FOUND|人工智能三次浪潮|自然语言处理
人工智能产业链|1|FOUND|人工智能三要素|
人工智能训练师|1|FOUND|人工智能产业链|
问题求解|2|SRCH|人工智能|
状态空间|2|SRCH|问题求解|
搜索树|2|SRCH|状态空间|
广度优先搜索|2|SRCH|搜索树|
深度优先搜索|2|SRCH|搜索树|
启发函数|2|SRCH|状态空间|
启发式搜索|2|SRCH|启发函数|广度优先搜索|
A* 搜索|2|SRCH|启发式搜索|
博弈搜索|2|SRCH|搜索树|
极小极大算法|2|SRCH|博弈搜索|
剪枝|2|SRCH|极小极大算法|
知识表示|2|KNOW|人工智能|符号主义|
产生式规则|2|KNOW|知识表示|
语义网络|2|KNOW|知识表示|
知识图谱|2|KNOW|语义网络|
三元组|2|KNOW|知识图谱|
推理|2|KNOW|知识表示|
正向推理|2|KNOW|推理|产生式规则|
反向推理|2|KNOW|推理|产生式规则|
专家系统|2|KNOW|产生式规则|推理|
知识库|2|KNOW|专家系统|
推理机|2|KNOW|专家系统|推理|
机器学习|3|ML|人工智能|数据|机器学习
样本|3|ML|数据|
特征|3|ML|样本|机器学习
标签|3|ML|样本|
数据集划分|3|ML|样本|机器学习
训练集|3|ML|数据集划分|
测试集|3|ML|数据集划分|
模型|3|ML|机器学习|
监督学习|3|ML|机器学习|标签|
无监督学习|3|ML|机器学习|
回归|3|ML|监督学习|机器学习
线性回归|3|ML|回归|机器学习
分类|3|ML|监督学习|机器学习
K 近邻|3|ML|分类|特征|机器学习
决策树|3|ML|分类|特征|机器学习
聚类|3|ML|无监督学习|特征|机器学习
K 均值|3|ML|聚类|机器学习
过拟合|3|ML|模型|训练集|测试集|机器学习
欠拟合|3|ML|过拟合|
准确率|3|ML|分类|测试集|
混淆矩阵|3|ML|准确率|机器学习
精确率与召回率|3|ML|混淆矩阵|机器学习
特征工程|3|ML|特征|机器学习
深度学习|4|DL|机器学习|连接主义|开发框架
人工神经元|4|DL|深度学习|
权重与偏置|4|DL|人工神经元|
激活函数|4|DL|人工神经元|
感知机|4|DL|人工神经元|
多层神经网络|4|DL|感知机|激活函数|
损失函数|4|DL|多层神经网络|机器学习
梯度下降|4|DL|损失函数|权重与偏置|机器学习
反向传播|4|DL|梯度下降|机器学习
训练轮次|4|DL|梯度下降|
卷积神经网络|4|DL|多层神经网络|机器学习；计算机视觉
循环神经网络|4|DL|多层神经网络|机器学习；自然语言处理
深度学习框架|4|DL|深度学习|开发框架
飞桨|4|DL|深度学习框架|开发框架
昇思|4|DL|深度学习框架|开发框架
GPU|4|DL|算力|开发框架
国产 AI 芯片|4|DL|GPU|
自然语言处理|5|NLP|人工智能|自然语言处理
分词|5|NLP|自然语言处理|自然语言处理
词向量|5|NLP|分词|特征|自然语言处理
Token|5|NLP|分词|大模型|自然语言处理
语言模型|5|NLP|词向量|自然语言处理
注意力机制|5|NLP|语言模型|多层神经网络|自然语言处理
Transformer|5|NLP|注意力机制|自然语言处理
预训练|5|NLP|Transformer|大模型|自然语言处理
微调|5|NLP|预训练|自然语言处理
人类反馈强化学习|5|NLP|微调|自然语言处理
上下文窗口|5|NLP|Token|
提示词|5|NLP|大模型|自然语言处理
提示词工程|5|NLP|提示词|自然语言处理
思维链|5|NLP|提示词工程|
推理模型|5|NLP|思维链|
幻觉|5|NLP|语言模型|自然语言处理
检索增强生成|5|NLP|幻觉|提示词|自然语言处理
机器翻译|5|NLP|自然语言处理|自然语言处理
计算机视觉|6|CV|人工智能|计算机视觉
数字图像|6|CV|计算机视觉|计算机视觉
像素|6|CV|数字图像|
RGB 颜色模型|6|CV|像素|
卷积|6|CV|像素|卷积神经网络|计算机视觉
图像分类|6|CV|卷积神经网络|分类|计算机视觉
目标检测|6|CV|图像分类|计算机视觉
图像分割|6|CV|目标检测|计算机视觉
人脸识别|6|CV|图像分类|计算机视觉
文字识别|6|CV|图像分类|计算机视觉
扩散模型|6|CV|深度学习|计算机视觉
文生图|6|CV|扩散模型|提示词|计算机视觉
多模态大模型|6|CV|大模型|图像分类|计算机视觉
视频分析|6|CV|目标检测|计算机视觉
声音信号|7|SPCH|人工智能|语音技术
采样与量化|7|SPCH|声音信号|语音技术
波形|7|SPCH|采样与量化|
频谱|7|SPCH|波形|语音技术
语音识别|7|SPCH|频谱|深度学习|语音技术
语音合成|7|SPCH|频谱|深度学习|语音技术
声纹识别|7|SPCH|频谱|分类|语音技术
语音克隆|7|SPCH|语音合成|声纹识别|语音技术
语音交互|7|SPCH|语音识别|语音合成|大模型|语音技术
语音唤醒|7|SPCH|语音识别|
字错率|7|SPCH|语音识别|语音技术
同声传译|7|SPCH|语音识别|机器翻译|语音合成|
强化学习|8|AGNT|机器学习|行为主义|机器学习
智能体与环境|8|AGNT|强化学习|
状态与动作|8|AGNT|智能体与环境|状态空间|
奖励|8|AGNT|状态与动作|
策略|8|AGNT|奖励|
探索与利用|8|AGNT|策略|
Q 学习|8|AGNT|探索与利用|机器学习
AlphaGo|8|AGNT|强化学习|博弈搜索|深度学习|
生成式人工智能|8|AGNT|大模型|扩散模型|
AI 智能体|8|AGNT|大模型|智能体与环境|智能体开发
任务规划|8|AGNT|AI 智能体|思维链|
工具调用|8|AGNT|AI 智能体|自然语言处理；智能体开发
记忆|8|AGNT|AI 智能体|检索增强生成|
模型上下文协议|8|AGNT|工具调用|智能体开发
低代码智能体平台|8|AGNT|AI 智能体|知识库|
工作流|8|AGNT|低代码智能体平台|
多智能体|8|AGNT|AI 智能体|
具身智能|8|AGNT|AI 智能体|强化学习|
人工智能+|9|APP|人工智能产业链|
智慧医疗|9|APP|人工智能+|图像分类|
智慧金融|9|APP|人工智能+|分类|
智能交通|9|APP|人工智能+|目标检测|
智能制造|9|APP|人工智能+|目标检测|
智慧教育|9|APP|人工智能+|大模型|
推荐系统|9|APP|人工智能+|机器学习|数据分析与处理
人工智能伦理|9|ETH|人工智能|
算法偏见|9|ETH|人工智能伦理|数据|
信息茧房|9|ETH|推荐系统|算法偏见|
个人信息保护|9|ETH|人工智能伦理|数据|
深度合成|9|ETH|生成式人工智能|语音克隆|
AI 生成内容标识|9|ETH|深度合成|
生成式人工智能服务管理|9|ETH|生成式人工智能|人工智能伦理|
知识产权|9|ETH|生成式人工智能|
可解释性|9|ETH|人工智能伦理|深度学习|
人工智能安全|9|ETH|人工智能伦理|提示词|
人工智能治理|9|ETH|生成式人工智能服务管理|人工智能安全|
"""

BOOKS = {"大数据": "《大数据技术处理技术》", "数据分析与处理": "《人工智能数据分析与处理》",
         "开发框架": "《人工智能开发框架技术》", "自然语言处理": "《自然语言处理导论》",
         "机器学习": "《机器学习》", "计算机视觉": "《计算机视觉及应用实战》",
         "语音技术": "《TTS、SST 与语音克隆》", "智能体开发": "智能体开发（选修课）"}

def parse():
    rows = []
    for line in RAW.strip().splitlines():
        parts = line.split("|")
        name, ch, cat = parts[0], int(parts[1]), parts[2]
        more = parts[-1]
        deps = [p for p in parts[3:-1] if p]
        rows.append(dict(name=name, ch=ch, cat=cat, deps=deps, more=more))
    return rows

def main(outdir):
    rows = parse()
    ids = {r["name"]: i + 1 for i, r in enumerate(rows)}
    assert len(ids) == len(rows), "重复概念"
    for r in rows:
        for d in r["deps"]:
            assert d in ids, f"{r['name']} 的先修 {d} 不存在"
            assert ids[d] < ids[r["name"]] or rows[ids[d]-1]["ch"] <= r["ch"], (r, d)
            assert rows[ids[d]-1]["ch"] <= r["ch"], f"{r['name']} 依赖后面章的 {d}"
    with open(f"{outdir}/learning-graph.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ConceptID", "ConceptLabel", "Dependencies", "TaxonomyID", "Chapter", "FurtherReading"])
        for r in rows:
            w.writerow([ids[r["name"]], r["name"], "|".join(str(ids[d]) for d in r["deps"]),
                        r["cat"], r["ch"], r["more"]])
    edges = sum(len(r["deps"]) for r in rows)
    dependents = collections.Counter(d for r in rows for d in r["deps"])
    out = [f"# 《人工智能导论》学习图谱概念清单（大纲阶段草案）", "",
           f"共 **{len(rows)} 个概念、{edges} 条先修关系**，分 {len(CATS)} 类。"
           "“深入学习”一列标出这个概念在系列里由哪本书讲透，导论只讲直观含义并链接过去；空白表示由本书讲透。", ""]
    out.append("| 类别 | 概念数 |\n|---|---|")
    cc = collections.Counter(r["cat"] for r in rows)
    for k, v in CATS.items():
        out.append(f"| {v} | {cc[k]} |")
    out.append("")
    for ch in range(1, 10):
        sub = [r for r in rows if r["ch"] == ch]
        out += [f"## 第 {ch} 章 {CHAPTERS[ch]}（{len(sub)} 个）", "",
                "| 概念 | 类别 | 直接先修 | 深入学习 |", "|---|---|---|---|"]
        for r in sub:
            more = "、".join(BOOKS[m] for m in r["more"].split("；")) if r["more"] else ""
            out.append(f"| {r['name']} | {CATS[r['cat']]} | {'、'.join(r['deps']) or '—'} | {more} |")
        out.append("")
    open(f"{outdir}/概念清单.md", "w", encoding="utf-8").write("\n".join(out))
    roots = [r["name"] for r in rows if not r["deps"]]
    leaves = [r["name"] for r in rows if dependents[r["name"]] == 0]
    print(len(rows), "concepts", edges, "edges; roots", roots, "; leaves", len(leaves))
    print({CATS[k]: cc[k] for k in CATS})
    print("per chapter", collections.Counter(r["ch"] for r in rows))

main(sys.argv[1])
