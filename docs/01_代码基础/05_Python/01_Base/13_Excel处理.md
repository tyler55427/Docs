# Excel 处理（openpyxl）

> 处理 `.xlsx` 文件；示例文件 `example.xlsx` ~ `example4.xlsx` 在同目录。
>
> 需先安装：`pip install openpyxl`

```python
import openpyxl
```

## 读取

```python
wb = openpyxl.load_workbook('./Base/example.xlsx')    # 相对路径是 cmd 运行目录的相对路径
print(wb.sheetnames)                                 # 所有表名

sheet = wb['Sheet1']
sheet = wb.active                                    # 当前激活的表

print(sheet['A1'].value)
print(sheet['B1'].value)
print(sheet['C1'].row)        # 行号
print(sheet['C1'].column)     # 列号
print(sheet['C1'].coordinate) # 坐标，如 'C1'

print(sheet.max_row)
print(sheet.max_column)
```

> 列字母：第 27 列起为 `AA`、`AB`、`AC`……

## 列字母 ↔ 数字

```python
from openpyxl.utils import get_column_letter, column_index_from_string

print(get_column_letter(1))               # 'A'
print(column_index_from_string('A'))       # 1
```

## 取行 / 列 / 矩形区域

```python
cell_range = sheet['A1':'D4']              # 二维 cell 列表
for row in cell_range:
    for cell in row:
        print(cell.coordinate, cell.value)
    print('--- END OF ROW ---')

list(sheet.columns)[1]                    # 第二列
list(sheet.rows)[1]                       # 第二行
```

## 写入

```python
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Spam Bacon Eggs Sheet'

sheet['A1'] = 'Hello world!'
sheet['A2'] = 'Hello Python!'
sheet['A3'] = 'Hello Excel!'
wb.save('./Base/example2.xlsx')
```

## 工作表管理

```python
wb.create_sheet()                                  # 默认追加到末尾，名字 Sheet2/Sheet3
wb.create_sheet(index=0, title='First Sheet')      # 指定位置

wb.remove(wb['Sheet'])                             # 方式 1
del wb['Sheet1']                                   # 方式 2
```

## 字体样式（Font）

```python
from openpyxl.styles import Font

italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['A1'].value = 'Hello world!'
wb.save('./Base/example3.xlsx')
```

`Font` 属性：`name`、`bold`、`italic`、`size`（可保存为变量复用）。

## 公式

```python
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'     # 字符串即公式
```

## 行高 / 列宽

```python
sheet.row_dimensions[1].height = 70       # 0~409，默认 12.75
sheet.column_dimensions['B'].width = 20   # 0~255，默认 8.43

# 设为 0 可隐藏行或列
```

## 合并 / 拆分

```python
sheet.merge_cells('A1:D3')        # 合并后只有 A1 有值
sheet.unmerge_cells('A1:D3')      # 拆分后每格都填上 A1 的值
```

## 冻结窗口

```python
# freeze_panes 的值是一个单元格坐标：
# 'A2'  → 冻结第一行
# 'B1'  → 冻结第一列
# 'C5'  → 冻结第 5 行之前和第 3 列之前
sheet.freeze_panes = 'A2'

# 解冻
sheet.freeze_panes = None
```

## 图表

步骤：
1. `Reference` 表示数据范围
2. `Series` 表示一个数据系列
3. `Chart` 表示图表
4. 把 `Series` 加入 `Chart`，再 `add_chart` 到 sheet

```python
import openpyxl.chart

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 11):
    sheet['A' + str(i)] = i

refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = openpyxl.chart.Series(refObj, title='First series')
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C5')
wb.save('./Base/example4.xlsx')
```

> `Reference` 接受 `(worksheet, min_col, min_row, max_col, max_row)`；两个整数 = 一个单元格，两个元组 = 矩形区域。