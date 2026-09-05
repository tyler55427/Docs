# Latex 基本语法

## 宏包

在 document 环境之前加载宏包。加载宏包的代码是\usepackage{}

与数学公式与定理环境相关的宏包为 amsmath、amsthm、amssymb，用于插入图片的宏包为 graphicx

\usepackage{amsmath, amsthm, amssymb, graphicx}

可以在导入宏包的时候，设置宏包的选项，例如：
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}

## 文档类型

\documentclass{article} % 文章类型
\documentclass{report} % 报告类型
\documentclass{book} % 书籍类型
\documentclass{letter} % 信件类型
\documentclass{beamer} % 幻灯片类型
\documentclass{IEEEtran} % IEEE 期刊类型
\documentclass{memoir} % 纪实类型
\documentclass{acmart} % ACM 期刊类型
\documentclass{elsarticle} % Elsevier 期刊类型
\documentclass{sigconf} % SIG 会议类型

英文：book, artivle, beamer
中文：ctexbook, ctexart, ctexbeamer

### 设置基本参数

笔者通常设置默认字体大小为 12pt，纸张大小为 A4，单面打印
\documentclass[12pt, a4paper, oneside]{ctexart}

## 正文环境

### 正文

\documentclass[12pt, a4paper, oneside]{ctexart}
\usepackage{amsmath, amsthm, amssymb, graphicx}
\usepackage[bookmarks=true, colorlinks, citecolor=blue, linkcolor=black]{hyperref}
\usepackage{geometry}

% 导言区

\title{我的第一个\LaTeX 文档}
\author{Dylaaan}
\date{\today}

\newtheorem{theorem}{定理}[section]
\newtheorem{definition}[theorem]{定义}
\newtheorem{lemma}[theorem]{引理}
\newtheorem{corollary}[theorem]{推论}
\newtheorem{example}[theorem]{例}
\newtheorem{proposition}[theorem]{命题}

\begin{document}

\maketitle
\tableofcontents

\section{一级标题}

\subsection{二级标题}

这里是正文.

\subsection{二级标题}

这里是正文.

\end{document}

### 标题、作者、时间

\title{我的第一个\LaTeX 文档}
\author{Dylaaan}
\date{\today}
在正文环境之前，书写上述参数，
在正文环境中，使用 \maketitle 命令来生成标题、作者和日期。

### 新开一页

\newpage

### 特殊字体

直立 \textup{}
意大利 \textit{}
倾斜 \textsl{}
小型大写 \textsc{}
加宽加粗 \textbf{}

### 章节

对于使用 ctexart 文档类型的文档，章节标题的命令为 \section{}，\subsection{}，\subsubsection{}
对于使用 ctexbook 文档类型的文档，章节标题的命令为 \chapter{}，\section{}，\subsection{}，\subsubsection{}

### 目录

\tableofcontents

## 图片

\begin{figure}[htbp] % 自动选择图片的最佳位置
\centering
\includegraphics[width=8cm]{图片.jpg}
\caption{图片标题}
\end{figure}

## 表格

\begin{table}[htbp]
\centering
\caption{表格标题}
\begin{tabular}{ccc}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{tabular}
\end{table}

## 列表

无序列表 itemize、有序列表 enumerate 和描述 description
\begin{enumerate}
\item 这是第一点;
\item 这是第二点;
\item 这是第三点.
\end{enumerate}

定义\item 的样式
\begin{enumerate}
\item[(1)] 这是第一点;
\item[(2)] 这是第二点;
\item[(3)] 这是第三点.
\end{enumerate}

## 定理环境

\begin{theorem}[定理名称] % 其中{theorem}是环境的名称，{定理}设置了该环境显示的名称是“定理”，[section]的作用是让 theorem 环境在每个 section 中单独编号。
这里是定理的内容.
\end{theorem}

## 页面

\usepackage{geometry}
\geometry{left=2.54cm, right=2.54cm, top=3.18cm, bottom=3.18cm}

### 行间距

\linespread{1.5}

## 页码

默认的页码编码方式是阿拉伯数字，用户也可以自己设置为小写罗马数字：

\pagenumbering{roman}
另外，aiph 表示小写字母，Aiph 表示大写字母，Roman 表示大写罗马数字，arabic 表示默认的阿拉伯数字。

页面从 0 开始
\setcounter{page}{0}

## 数学公式

行内公式：
$\sum_{i=1}^{n} i^2$，

行间公式：
$\displaystyle \sum_{i=1}^{n} i^2$（行内公式显示行间公式的效果）；
行间公式需要用\\[..\\]或者\$\$..\$\$来输入

### 分式

分式可以用\dfrac{}{}来输入，
为了在行间、分子、分母或者指数上输入较小的分式，可以改用\frac{}{}

### 括号

括号可以直接用(..)输入，
也可以用\left(和\right)来输入，\left 和\right 会自动调整括号的大小。

在中间需要隔开时，可以用\left(..\middle|..\right)

输入大括号{}时需要用\\{..\\}，其中\起到了转义作用

### 公式加粗

对于加粗的公式，建议使用 bm 宏包，并且用命令\bm{}来加粗，这可以保留公式的斜体。

## 大括号

在这里可以使用 cases 环境，可以用于分段函数或者方程组，例如

\$\$
f(x)=
\begin{cases}
x, & x>0, \\\\ % 换行
-x, & x\leq 0.
\end{cases}
\$\$

$$
f(x)=
\begin{cases}
    x, & x>0, \\
    -x, & x\leq 0.
\end{cases}
$$

## 多行公式

多行公式通常使用 aligned 环境，例如

\$\$
\begin{aligned}
a & =b+c \\
& =d+e
\end{aligned}
\$\$

### 矩阵和行列式

矩阵可以用 bmatrix 环境和 pmatrix 环境，分别为方括号和圆括号，例如

\$\$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\$\$

行列式可以用 vmatrix 环境和 Vmatrix 环境，分别为竖线和双竖线，用法相同
