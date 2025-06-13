FROM ygkkk/argosb

# 安装 Flask
RUN pip install flask

# 拷贝健康服务脚本
COPY health.py /health.py

# 设置启动命令：同时运行主服务和 Flask 健康服务
CMD ["python3", "/health.py"]
