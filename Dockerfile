# 指定你已有的 Python 基础镜像（请根据实际情况替换标签，如 3.11-slim）
FROM python:3.10-slim
#FROM python:3.11-slim

# 设置容器内的工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录
COPY . /app

# 如果你有依赖包（如 flask），需要先安装。若无 requirements.txt 可删掉下面两行
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 容器启动时执行的命令（运行你的 Python 脚本）
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
#CMD ["python", "main.py"]