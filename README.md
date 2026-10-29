# 人工智能导论

面向成人教育人工智能技术应用专业（专科）的《人工智能导论》网络教材，从系列教材模板 `ai-textbook-template` 新建。

- 2 学分，36 学时，全部为理论学时（线上 29 + 线下 7），第 1 学期，闭卷
- 9 章 + 4 个附录；没有实验学时，每章配 2 个免安装的在线体验，共 18 个；书中不写代码、不推导公式
- 每章课后单选、多选、判断题可在网页上直接作答，书末附 2 套在线模拟卷
- 配套交互动画（`docs/sims/`）、学习图谱（`docs/learning-graph/`）和常见问题（`docs/faq/`）

## 目录结构

| 路径 | 内容 |
|---|---|
| `docs/` | 教材正文（MkDocs Material 格式） |
| `docs/sims/` | 交互动画，每个动画一个文件夹，公共样式在 `common/` |
| `course.yml` | 课程配置：书名、学时、各章与线下学时、附录；改完运行 `python tools/course.py sync` |
| `slides/`、`lesson-plans/` | 课件和教案的底稿，用 `tools/make_slides.py`、`tools/make_lesson_plan.py` 生成 |
| `tools/` | 维护脚本：术语链接与概念清单、学习图谱检查、首页统计、Word/PDF 导出；`build_concepts.py` 生成大纲阶段的概念表 |
| `规划/` | 章节大纲与学习图谱概念表（大纲阶段） |
| `编写规范.md`、`系列公共术语表.md` | 系列教材共用的编写规范和术语表 |

## 本地预览

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

推送到 `main` 分支后，GitHub Actions 会自动构建并发布到 GitHub Pages（需在仓库 Settings → Pages 中把 Source 设为 GitHub Actions）。

## 说明

书中的产品名称、免费额度等信息会变化，均注明“截至某年某月”。课件、教案和 Word/PDF 版教材作为 GitHub Release 的附件发布。
