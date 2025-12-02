# 使用官方Python轻量级镜像
FROM python:3.9-slim
# 设置工作目录
WORKDIR /app
# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 复制应用代码
COPY . .
# 暴露端口
EXPOSE 5000
# 运行应用（使用生产级WSGI服务器）
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]