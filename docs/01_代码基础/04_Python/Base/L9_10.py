# 文件读写 和 组织文件

# 文件名称和文件名在Windows和macOS下是不区分大小写的，但是Linux下是区分大小写的
# 文件路径分隔符在Windows下是\，在macOS和Linux下是/

import os
from pathlib import Path
# 可以进行除法运算
print(Path('spam')/'bacon'/'eggs')

print(Path.cwd())
print(Path.home())
# . 是当前目录 .. 是上一级目录

# 获得文件路径的各部分
p = Path(Path.cwd())
print(p.anchor)
print(p.parent) # 这个不是一个string, 是一个Path对象
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

# 查看文件大小和文件夹内容
os.path.getsize(p)
os.listdir(p)










# shutil模块
import shutil

# 复制文件和文件夹
# shutil.copy('D:\\A1111\\Pre.txt', 'C:\\Users\\19242\\Desktop')

# 文件和文件夹的移动和重命名, 重命名是移动的特例
# shutil.move('C:\\Users\\19242\\Desktop\\Pre.txt', 'C:\\Users\\19242\\Desktop\\Pre1.txt')

# 永久删除文件和文件夹
# os.unlink('C:\\Users\\19242\\Desktop\\Pre1.txt') # 删除文件
# os.rmdir('C:\\Users\\19242\\Desktop\\Pre1.txt') # 删除文件夹，文件夹必须为空，否则会报错
# shutil.rmtree('C:\\Users\\19242\\Desktop\\Pre1.txt') # 删除文件夹，文件夹不为空也可以删除

# 安全删除
# send2trash模块
# 移动到回收站

# 遍历目录树
# os.walk()函数
# 在循环的每次迭代返回三个值，当前文件夹名称的字符串，当前文件夹中子文件夹的字符串列表，当前文件夹中文件的字符串列表


# 压缩文件
# zipfile模块

# 读取zip文件
# import zipfile
# exampleZip = zipfile.ZipFile('example.zip')
# exampleZip.namelist() # 返回zip文件中的文件名列表
# spamInfo = exampleZip.getinfo('spam.txt') # 返回zip文件中的文件信息
# spamInfo.file_size # 文件大小 
# spamInfo.compress_size # 压缩后的文件大小

# 从zip文件中解压缩
# exampleZip.extractall() # 解压缩到当前目录，并放到当前工作目录
# exampleZip.extractall('C:\\Users\\19242\\Desktop') # 解压缩到指定目录
# exampleZip.extract('spam.txt') # 解压缩单个文件
# exampleZip.extract('spam.txt', 'C:\\Users\\19242\\Desktop') # 解压缩单个文件到指定目录

# 创建和添加到zip文件
# newZip = zipfile.ZipFile('new.zip', 'w') # 创建一个新的zip文件，'w'表示写入
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # 添加文件到zip文件，即压缩这个路径的所有文件
