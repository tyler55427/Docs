# Conda 常用命令

1. **创建虚拟环境**  
   `conda create --name myenv python=3.8`  
   创建名为 `myenv` 的环境，并指定 Python 版本为 3.8。

2. **激活虚拟环境**  
   `conda activate myenv`  
   激活 `myenv` 环境。

3. **退出虚拟环境**  
   `conda deactivate`  
   退出当前激活的环境。

4. **列出所有虚拟环境**  
   `conda env list`  
   显示系统中所有 Conda 环境。

5. **删除虚拟环境**  
   `conda remove --name myenv --all`  
   删除 `myenv` 环境及其所有内容。

6. **克隆虚拟环境**  
   `conda create --name newenv --clone myenv`  
   将 `myenv` 克隆为 `newenv`（可用于重命名，或直接修改环境文件夹名，但不推荐）。

7. **更换 Python 版本**  
   `conda install python=3.7`  
   在当前环境中更改 Python 版本。

8. **查看安装的包**  
   `conda list`  
   列出当前环境中的所有包。

9. **安装新包**  
   `conda install numpy`  
   在当前环境中安装 `numpy`。

10. **更新包**  
    `conda update numpy`  
    更新当前环境中的 `numpy`。

11. **卸载包**  
    `conda remove numpy`  
    从当前环境中移除 `numpy`。

12. **使用 .yml 文件更新环境**  
    `conda env update -f environment.yml`  
    （添加 `--prune` 会删除不在文件中的包）

13. **导出环境为 YAML 文件**  
    `conda env export > environment.yml`  
    将当前环境配置导出到 `environment.yml`。

14. **从 YAML 文件创建环境**  
    `conda env create -f environment.yml`  
    根据 `environment.yml` 文件创建新环境。