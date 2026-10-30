"""训练交互动画“手写数字识别”用的小神经网络，把权重写成 docs/sims/digit-recognition/weights.js。

数据：scikit-learn 自带的手写数字数据集（1797 张 8 × 8 灰度图，像素值 0～16）。
网络：64 个输入 → 48 个隐藏神经元（ReLU）→ 10 个输出（Softmax）。
用法：pip install scikit-learn，然后在仓库根目录运行 python tools/sim-data/train_digits.py
"""
import json
from pathlib import Path

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = load_digits(return_X_y=True)
X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0, stratify=y)
# 训练时加一点平移，让网络对用户手写时的位置偏差更宽容
def shift(imgs, dx, dy):
    a = imgs.reshape(-1, 8, 8)
    a = np.roll(a, (dy, dx), axis=(1, 2))
    if dy > 0: a[:, :dy, :] = 0
    if dy < 0: a[:, dy:, :] = 0
    if dx > 0: a[:, :, :dx] = 0
    if dx < 0: a[:, :, dx:] = 0
    return a.reshape(-1, 64)
aug = [Xtr] + [shift(Xtr, dx, dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]]
Xa, ya = np.vstack(aug), np.concatenate([ytr] * len(aug))
net = MLPClassifier(hidden_layer_sizes=(48,), activation="relu", alpha=1e-3, max_iter=1500, random_state=0)
net.fit(Xa, ya)
acc = net.score(Xte, yte)
print(f"测试集准确率：{acc:.4f}（{len(yte)} 张）")
r = lambda a: np.round(a, 3).tolist()
samples = [{"x": r(Xte[i]), "y": int(yte[i])} for i in range(40)]
out = {"W1": r(net.coefs_[0]), "b1": r(net.intercepts_[0]), "W2": r(net.coefs_[1]), "b2": r(net.intercepts_[1]),
       "acc": round(acc, 4), "ntest": int(len(yte)), "samples": samples}
dst = Path(__file__).resolve().parents[2] / "docs/sims/digit-recognition/weights.js"
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text("// 由 tools/sim-data/train_digits.py 生成，不要手改\nvar NET = " + json.dumps(out, separators=(",", ":")) + ";\n", encoding="utf-8")
print("已写入", dst, dst.stat().st_size, "字节")
