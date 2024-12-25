# source2cg
A tool based on LLVM or Doxygen for generating call graphs for c code, which also saves the call graph information from Doxygen in JSON format.

## 依赖

系统版本：

```
ubuntu 22.04
```

python 版本：

```
Python 3.10.12
```

安装依赖：

```
sudo apt-get update
sudo apt-get install llvm clang
sudo apt-get ibstall doxygen
pip install graphviz
pip install pillow
pip install pymupdf
```

对应版本：

```
Ubuntu clang version 14.0.0-1ubuntu1.1
Ubuntu LLVM version 14.0.0
doxygen 1.9.1
graphviz version 2.43.0 (0)
pillow 11.0.0                          
pymupdf 1.25.1
```


## 使用

把项目放到 input 文件夹下，运行：

```
python3 cgGen_llvm.py file.c 
```

通过 llvm 生成 file.c 中每个函数的调用图在 output 文件夹中

运行：

```
python3 cgGen_doxygen.py
```

通过 doxygen 生成整个项目每个文件的依赖图，以及调用图

运行：

```
python3 depGen.py 
```

生成整个项目每个文件的依赖图，以及调用图，同时解析图片生成 json 格式的依赖调用信息在 json文件夹中

