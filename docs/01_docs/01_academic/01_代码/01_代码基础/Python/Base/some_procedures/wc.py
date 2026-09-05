from pathlib import Path
import sys
p=Path('.\\Python\\Others\\file.txt')
# 简略实现linux的wc命令
def wc(file):
    # 返回行数，单词数，字节数而不是字符数
    f=open(file,encoding='utf8')
    lines = f.readlines()
    f.seek(0)
    words = f.read().split()
    f.seek(0)
    return len(lines),len(words),len(f.read().encode())
    

for i in sys.argv[1:]:
    print(*wc(i))