# pip 常用命令

1. 安装包
   pip install numpy
   pip install numpy==1.21.0 # 安装指定版本的包
   pip install 'package_name>=1.0' # 安装指定版本及以上的包
2. 卸载包
   pip uninstall numpy
3. 更新包
   pip install --upgrade numpy
4. 查看已安装的包
   pip list # 列出所有已安装的包及其版本（可以配合 findstr 的 shelll 命令使用）
   pip show numpy # 查看指定包的详细信息
5. 查找包（好像已经不支持了）
   pip search numpy # 查找与 numpy 相关的包
