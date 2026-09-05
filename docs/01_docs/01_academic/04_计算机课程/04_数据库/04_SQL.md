# 四、SQL 结构化查询语言
## 4.1 DDL(数据定义语言)

### 数据类型
| 类型 | 说明 |
|:---:|:---|
| char(n) | 长度恒为 n 的字符串 |
| varchar(n) | 可变长度字符串，最大 n |
| int | 整型，4 字节 |
| smallint | 小整型，2 字节 |
| numeric(p,d) | 数值，一共 p 位，d 位小数 |
| float(n) | 存储浮点数 n 位 |
| date | YYYY-MM-DD |
| time | HH:MM:SS |

### 表操作
```sql
CREATE TABLE r (..., PRIMARY KEY(...))
DROP TABLE r
ALTER TABLE r ADD a char(10)
ALTER TABLE r DROP a
```

### 完整性约束
- 主键、候选键
- 外键约束 FOREIGN KEY(sid) REFERENCES Students
- 级联删除/更新 ON DELETE/UPDATE CASCADE
- 设置默认值/空值 SET NULL/DEFAULT

## 4.2 DML(数据操作语言)

### 基本查询
```sql
SELECT [DISTINCT] target-list
FROM relation-list
WHERE qualification
```

### 算术操作
where 条件支持 and, or, not，between a and b

### 字符串操作
- `%`：任意字符串组合，可为空
- `_`：任意单个字符

### 排序
```sql
ORDER BY a ASC/DESC
```

### 聚合函数
| 函数 | 说明 |
|:---:|:---|
| COUNT([DISTINCT] A) | 计数 |
| SUM([DISTINCT] A) | 求和 |
| AVG([DISTINCT] A) | 求均值 |
| MAX(A) | 最大 |
| MIN(A) | 最小 |

### 集合操作
- UNION ∪（自动去重，ALL 保留）
- INTERSECT ∩
- EXCEPT -

### 嵌套查询
- IN, NOT IN
- SOME, ALL
- EXISTS：非空为 true
- UNIQUE：没有重复为 true

### 分组
```sql
GROUP BY a
HAVING 条件
```

### Null 值
不包含有 null 值，等于 false

## 4.3 视图
```sql
CREATE VIEW view_name AS <query>
DROP VIEW view_name
```

## 4.4 断言与触发器
```sql
CREATE ASSERTION ... CHECK ...
```

触发器：define trigger on update of ...
