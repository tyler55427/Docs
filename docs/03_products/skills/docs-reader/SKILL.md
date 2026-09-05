---
name: docs-reader
description: 读取/提取/修改 Office 文档（doc/docx/xls/xlsx/ppt/pptx）的正文、表格与批注，用于文档阅读理解与内容加工
---
# Docs Reader —— Office 文档阅读理解

一个用 Python 读写 Office 文档的工具集。支持现代格式（docx/xlsx/pptx）与旧版格式（doc/xls/ppt，通过 LibreOffice 转换）。

## 依赖

| 用途         | 依赖                                    |
| ------------ | --------------------------------------- |
| 旧版格式转换 | `soffice` (LibreOffice)，需在 PATH 中 |
| docx         | `python-docx`                         |
| xlsx         | `openpyxl`                            |
| pptx         | `python-pptx`                         |

## 脚本总览

| 脚本                               | 功能                               |
| ---------------------------------- | ---------------------------------- |
| `scripts/read_doc.py`   | 读取单个文档的正文 / 表格 / 批注   |
| `scripts/modify_doc.py` | 在文档中查找并替换文本，输出新文件 |

所有脚本的临时转换文件输出到 `./work/tmp/`。

---

## 1. 读取文档内容 —— read_doc.py

```bash
python3 scripts/read_doc.py <文件路径> [--body] [--comments] [--tables]
```

**参数**

- `--body`     输出正文内容
- `--comments` 输出批注（docx 批注、xlsx 批注、pptx 备注与批注）
- `--tables`   输出表格内容（以 `|` 分隔单元格）

不传任何 mode 参数时默认输出 body + comments + tables 全部。

**示例**

```bash
# 读取一份 docx 的正文和表格
python3 scripts/read_doc.py 报告.docx --body --tables

# 读取一份 pptx 的备注（讲稿）
python3 scripts/read_doc.py 课件.pptx --comments
```

**输出格式**

```
=== Body ===
...正文...

=== Comments ===
...批注...

=== Tables ===
...表格...
```

## 2. 修改文档文本 —— modify_doc.py

```bash
python3 scripts/modify_doc.py <输入文件> --old <旧文本> --new <新文本> --output <输出文件>
```

在正文、表格中查找 `旧文本` 并替换为 `新文本`，保存到新文件（不修改原文件）。

**要点**

- 原文件不会被改动，结果写入 `--output` 指定的新文件
- 替换成功输出 `Modified: <输出路径>`，无匹配输出 `No modification made`
- 支持 docx（段落/表格/内嵌形状）、xlsx（所有单元格）、pptx（所有形状文本）

**示例**

```bash
python3 scripts/modify_doc.py 合同.docx \
  --old "甲方" \
  --new "买方" \
  --output 合同-修改.docx
```

---

## 使用建议

- **阅读理解**：先 `--body` 读正文掌握结构，再 `--tables` 看数据，需要审阅意见时用 `--comments`。
- **旧版格式**（doc/xls/ppt）：首次读取会自动调用 `soffice` 转换，耗时约数秒；转换文件缓存在 `./work/tmp/`。
- **批量场景**：逐个文档精读用 `read_doc.py`；批量替换文本用 `modify_doc.py`。
