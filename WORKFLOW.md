# Sonniss GDC 音效包目录工作流程

> 本文件记录完整工作流程，对话丢失后可凭此文件还原所有步骤。

---

## 仓库结构

```
音效包/
├── .gitignore              # 忽略 *.zip（体积过大且不可二次分发）
├── README.md               # 总索引，含所有年份跳转链接
├── WORKFLOW.md             # 本文件，工作流程说明
├── generate_catalog.py     # 结构提取工具（见下）
├── zh-cn/                  # 中文描述版本
│   ├── Sonniss GDC 2015.md
│   ├── Sonniss GDC 2016.md
│   └── ...
└── en/                     # 英文描述版本
    ├── Sonniss GDC 2015.md
    ├── Sonniss GDC 2016.md
    └── ...
```

---

## 各年份下载地址

所有年份的压缩包均可在官方页面免费获取：

**https://sonniss.com/gameaudiogdc/**

页面内按 Tab 切换年份（GDC 2015 / 2016 / 2017 / 2018 / 2019 / 2020 / 2021-2023 / 2024）。
填写邮箱后可获得下载链接（torrent 或直链）。

---

## 新年份上线时的工作流程

### 步骤 1：下载压缩包

从官网下载对应年份的全部分卷压缩包，命名规则须符合：

```
Sonniss.com - GDC - YYYY_N.zip
```

例如：
```
Sonniss.com - GDC - 2016_1.zip
Sonniss.com - GDC - 2016_2.zip
```

将文件放入本目录（`音效包/`）根目录下。

### 步骤 2：运行结构提取脚本

```bash
python generate_catalog.py
```

脚本会打印各 ZIP 内的顶层目录列表，格式如下：

```
=== 2016 / Part 1 ===
  Author Name - Pack Name
  Author Name - Another Pack
  ...
```

### 步骤 3：将输出交给 AI 分析

将脚本输出的目录列表粘贴给 AI，并说明：

> 这是 Sonniss GDC 20XX 的目录结构，请：
> 1. 根据目录名推断每个音效包的内容和适用场景
> 2. 生成 zh-cn/Sonniss GDC 20XX.md（中文描述）
> 3. 生成 en/Sonniss GDC 20XX.md（英文描述）
> 4. 更新 README.md 中对应年份的状态标记（从 `⏳ 待分析` 改为 `✅ 已收录`）

### 步骤 4：AI 生成 Markdown 文件

AI 根据目录名逐一推断描述，按以下格式生成文件（见下节格式规范）。

### 步骤 5：验证并提交

确认内容后，`git add` 所有 `.md` 文件（**不要** add `.zip`），提交推送。

---

## Markdown 文件格式规范

### zh-cn/Sonniss GDC YYYY.md

```markdown
# GDC Sonniss YYYY

**官方下载：** https://sonniss.com/gameaudiogdc/（选择 GDC YYYY 标签页）

---

## Part N

### 作者名 - 包名

一句中文描述，说明音效类型和适用场景（50 字以内）。

```

### en/Sonniss GDC YYYY.md

格式同上，描述改为英文。

---

## Markdown 文件命名规则

| 年份 | 文件名 |
|------|--------|
| 2015 | `Sonniss GDC 2015.md` |
| 2016 | `Sonniss GDC 2016.md` |
| 2021–2023 | `Sonniss GDC 2021-2023.md` |
| ... | ... |

---

## README.md 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 已有对应 ZIP，目录已分析完毕 |
| ⏳ | ZIP 尚未到位，文件为占位 |
| 🔮 | 该年份尚未发布 |

---

## generate_catalog.py 说明

- **输入**：当前目录下所有符合 `*GDC - YYYY_N.zip` 命名规则的文件
- **输出**：按年份/分卷打印顶层目录列表
- **不做**：不生成任何描述，不写 Markdown，无任何硬编码文本
- **依赖**：Python 3.x 标准库（无需安装第三方包）
