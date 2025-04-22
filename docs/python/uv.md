## uv常用

https://docs.astral.sh/uv

### 初始化项目

> 使用国内镜像 UV_PYTHON_INSTALL_MIRROR="https://mirror.nju.edu.cn/github-release/indygreg/python-build-standalone/"

```
uv init example
```

### 添加依赖

```
uv add ruff
```

###  运行

```
uv run main.py
```

### 初始化脚本+指定python版本

```
uv init --script example.py --python 3.12
```

### 给特殊脚本添加依赖

```
uv add --script example.py 'requests<3' 'rich'
```
