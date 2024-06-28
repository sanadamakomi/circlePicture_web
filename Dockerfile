# python镜像
FROM python:3.10-slim

# 安装python包
RUN pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com shiny htmltools pillow gunicorn

# api脚本
WORKDIR /var/data
COPY ./app.py .
COPY ./circlePicture.py .
COPY ./default.png .

EXPOSE 80

# 工作目录
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80", "-k", "uvicorn.workers.UvicornWorker"]

# 打包
# docker build -t circle_picture:latest .

# 导出
# docker save -o circle_picture_latest.tar circle_picture:latest

# 导入
# docker load -i circle_picture_latest.tar

# 部署命令
# docker run -it -p 3838:80 --name circle_picture circle_picture:latest